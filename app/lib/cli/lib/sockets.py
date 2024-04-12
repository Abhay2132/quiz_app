from sys import exit
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from types import SimpleNamespace
from threading import Thread
from socket import socket, SOCK_STREAM, AF_INET

magicKey = b"India"

class EventEmitter:
    __events = dict()
    __listen=None
    
    def __init__(self):
        pass

    def attach(self, listener:function):
        "Attach a global listener which will be called at every event"
        self.__listen = listener
    
    def on(self, name, callback):
        if not bool(self.__events.get(name)):
            self.__events[name] = list()
        self.__events[name].append(callback)
        
        return len(self.__events[name])-1

    def emit(self, name, *args):
        if self.__listen:
            self.__listen(name, args)
        if name not in self.__events:
            return

        for callback in self.__events[name]:
            callback(args)
        pass

    def off(self,name, index:int=None):
        if not self.__events.get(name):
            return 
        if index is None:
            self.__events[name].clear()
        
        if index < len(self.__events[name]):self.__events[name].pop(index)

class ServerSocket(EventEmitter):

    sel = DefaultSelector()
    clients = dict() # { portNumber<id[int]> : key<keySelector>}
    killThread = True
    eventThread = None
    ssock=None
    
    def __init__(self, addr) -> None:
        super().__init__()
        self.sel = DefaultSelector()
        self.addr = addr
        pass

    def start(self):
        self.killThread = False
        if self.eventThread:
            return
        self.ssock = socket(AF_INET, SOCK_STREAM)
        self.ssock.bind(self.addr)
        self.ssock.listen()
        print("server listening at", self.addr)
        self.sel.register(self.ssock, EVENT_READ, data=None)

        self.eventThread = Thread(target=self._server_event_loop, daemon=True)
        self.eventThread.start()
        pass

    def sendTo(self, message:bytes,client_id=None):
        if type(message) is str:
            message = bytes(message, encoding="utf-8")

        if client_id not in self.clients:
            raise Exception("Client ID not found")

        client_key = self.clients[client_id]
        data = client_key.data
        data.outb += message

    def broadcast(self, message:bytes):
        for clientID in self.clients:
            self.sendTo(message, clientID)

    def stop(self):
        while self.eventThread:
            self.killThread = True

    def handshake(self, data): # recieve handshake -> send handshake
        stage = data.handshakeStage
        if stage == 1:
            if data.inb == magicKey:
                data.inb = b""
            else:
                self.emit("handshake-failed", (stage, data.addr[1]))
                print("error : magicKey does not matches, recv:",data.inb)
        elif stage == 2:
            data.outb = magicKey
        pass

    def __add_connection(self, key):
        soc = key.fileobj
        conn, addr = soc.accept()
        clientID = addr[1]
        data = SimpleNamespace(addr=addr, outb=b"", inb=b"", clientID=clientID, handshakeStage=0)
        # HANDSHAKE STAGES # 1 -> Recieved | 2 -> Sent | 3 -> DONE
        self.sel.register(conn, EVENT_READ | EVENT_WRITE, data=data)
        self.emit("new-connection", clientID)
        self.clients[clientID] = SimpleNamespace(fileobj=conn, data=data)

    def __handle_RW_events(self, key, mask):
        soc = key.fileobj
        data = key.data
        if mask & EVENT_READ:
            recv = soc.recv(1024)
            if recv:
                data.inb += recv
                
                if data.handshakeStage == 0 :
                    data.handshakeStage = 1
                    self.handshake(data)
                    return
                self.emit("data-packet", recv)
                # print(f"recv {data.addr}: "+recv.decode("utf-8"))
                # print(f"clients : {len(self.clients)}")
        if mask & EVENT_WRITE:
            if data.handshakeStage == 1:
                data.handshakeStage = 2
                self.handshake(data)
            
            # emit the `data` event and flushes the `inb` (input buffer)
            
            if data.inb:
                self.emit("data", data.inb)
                data.inb = b""

            sent = 0
            if data.outb:
                sent = soc.send(data.outb)
            data.outb = data.outb[sent:]

            # verify handshake = no error after sending data (like client doesn't disconnected)
            if data.handshakeStage == 2:
                data.handshakeStage = 3 # handshake done
                print("HANDSHAKE DONE With", data.addr)
        
    def _server_event_loop(self):
        print("server event_loop started")
        while not self.killThread:
            lastConnKey = None
            try:
                events = self.sel.select(timeout=None)
                for key,mask in events:
                    lastConnKey = key
                    if key.data is None:
                        # add new client
                        self.__add_connection(key)
                        pass
                    else :
                        # read / write clients
                        self.__handle_RW_events(key=key, mask=mask)

            except KeyboardInterrupt:
                print("Exiting by Keyboard Interrupt")
                exit(1)
            except Exception as e:
                print("Exiting : ", e)
                self._disconnect(lastConnKey)
            finally:
                pass

        self.eventThread = None
        pass

    def _disconnect(self, key):
        sock = key.fileobj
        clientID = key.data.addr[1]

        self.sel.unregister(sock)
        sock.close()

        if clientID in self.clients:
            self.clients.pop(clientID)
        
        self.emit("disconnected", clientID)

class ClientSocket(EventEmitter):
    sel = None
    addr = None
    data = None
    eventThread = None
    csoc = None
    handshakeStage = 0 #  1 -> send | 2 -> recived | 3 -> DONE

    def __init__(self, addr) -> None:
        super().__init__()
        self.sel = DefaultSelector()
        self.addr = addr

    def handshake(self, recv=None): # to verify the connection with server
        if self.handshakeStage ==3:
            print("Handshake already DONE")
            return
        # socket is ready to write
        
        try:
            if self.handshakeStage == 1:
                self.csoc.send(magicKey)
                return
            
            if self.handshakeStage == 2:
                if recv == magicKey:
                    self.handshakeStage = 3
                    print("Handshake Done with", self.addr)
                else:
                    self.emit("handshake-error", Exception(f"MAGIC KEY DOES NOT MATCHES, {recv} != {magicKey}"))
            
        except Exception as e:
            self.emit("handshake-error", e)
        else:
            # self.handshakeDone = True
            pass
        finally:
            pass

    def connect(self):
        csoc = socket(AF_INET, SOCK_STREAM)
        csoc.setblocking(False)
        csoc.connect_ex(self.addr)
        events = EVENT_WRITE | EVENT_READ

        self.data = SimpleNamespace(inb = b"", outb=b"")
        self.sel.register(csoc, events, data=self.data)
        self.csoc = csoc

        self.eventThread = Thread(target=self._client_event_loop, daemon=True)
        self.eventThread.start()

    def disconnect(self):
        self.sel.unregister(self.csoc)
        self.csoc.close()
        self.csoc = None

    def send(self, message:bytes):
        self.data.outb += message

    def __handle_RW_events(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & EVENT_READ: # ready to read
            recv_data = sock.recv(1024)
            if recv_data:

                if self.handshakeStage == 1: # reveice magickey from server
                    self.handshakeStage = 2
                    self.handshake(recv_data)
                    return
                
                data.inb += recv_data
                self.emit("data-packet", recv_data)
        if mask & EVENT_WRITE: # ready to write
            if self.handshakeStage == 0: # sends handleshake magickey to server
                self.handshakeStage = 1
                self.handshake()
            if data.inb:
                self.emit("data", data.inb)
                data.inb = b"" # flush input buffer
            if data.outb:
                sent = sock.send(data.outb) 
                data.outb = data.outb[sent:]
        pass

    def _client_event_loop(self):
        print("Client EVENT LOOP STARTED")
        while True:
            try:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    self.__handle_RW_events(key, mask)
            except KeyboardInterrupt:
                print("exiting (client) by keyboard interrupt")
                exit(2)
            except Exception as e:
                print("Exiting (client): " , e)
                self.emit("error", e)
                self.sel.close()
            finally:
                pass
            
if __name__ == "__main__":
    ee = EventEmitter()
    ee.on("call", lambda arr : print(arr))
    ee.emit("call", 1,2,3,4)