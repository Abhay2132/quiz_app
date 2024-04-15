class A():
    p=1

    def destroy(self):
        del self

a = A()
print(a.p)
a.destroy()
print(a.p)
del a
print(a.p)