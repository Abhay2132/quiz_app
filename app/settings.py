# import netifaces
import subprocess

def cb (line:str):
    if line == "\r":
        return ""
    while '\r' in line:
        line = line.replace('\r','')
    while '  ' in line:
        line = line.replace('  ', ' ')
    return line

def extractInterfaces(line):
    target = "Dedicated"
    i = line.find(target)
    return line[i+len(target):].strip()

def getInterfaces():
    out = subprocess.check_output("netsh interface show interface").decode()
    out = out.split("\n")
    out = list(map(cb, out)) # filtering \r and double spaces
    out = list(filter(bool, out)) # filter empty strings

    out = out[2:]

    interfaces = list(map(extractInterfaces, out))

    return interfaces

def getHOTSPOT():

    interfaces = getInterfaces()
    interfaces = list(filter(lambda i : i.startswith("Local Area Connection"), interfaces))
    if len(interfaces) < 1:
        raise OSError("TURN ON HOTSPOT FIRST")
    hotspot_interface = interfaces[0]#"Local Area Connection* 2"

    output = subprocess.check_output(f'netsh interface ipv4 show config name="{hotspot_interface}"', shell=True, universal_newlines=True)
    output = output.split("\n")
    output = list(filter(lambda _ : _.strip().startswith("IP Address"), output))
    if len(output) == 0:
        return None
    output = output[0]
    while " " in output:
      output = output.replace(" ", "")
    output = output[10:]
    return (output)

def getWIFI():
    interfaces = getInterfaces()
    interfaces = list(filter(lambda i : i.startswith("Wi-Fi"), interfaces))
    if len(interfaces) < 1:
        raise OSError("SYSTEM does not have Wi-Fi supports")
    wifi_interface = interfaces[0]#"Local Area Connection* 2"

    coutput = subprocess.check_output(f'netsh interface ipv4 show config name="{wifi_interface}"', shell=True, universal_newlines=True)
    output = coutput.split("\n")
    output = list(filter(lambda _ : _.strip().startswith("Default Gateway:"), output))
    
    if len(output) < 1:
        for line in coutput.split("\n"):
            print(line)
        raise Exception("`DEFAULT GATEWAY` not found in WI-Fi")
    output = output[0]
    while " " in output:
      output = output.replace(" ", "")
    output = output[15:]
    return (output)

PORT = 5002  # Port to listen on (non-privileged ports are > 1023)
# HOST = "localhost"

if __name__ == "__main__": print((getWIFI(), getHOTSPOT(), PORT))

host = "localhost"
port = 4040

addr = (host, port)