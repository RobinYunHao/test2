class Duilie():
    def __init__(self, maxsize):
        self.front = -1
        self.real = -1
        self.maxsize = maxsize
        self.arr = []
    def dui(self, arr):
        maxsize = arr
        ar = list(maxsize)
        print(ar)

    def full(self, real, maxsize):
        am = Duilie(10)
        if am.real == am.maxsize - 1:
            hr = 1
            return hr
        else:
            hr = 2
            return hr

    def empty(self, front, real):
        if front == real:
            n = 1
        else:
            n = 0
        return n


    def addqueue(self, n, real, arr,):
        ma = Duilie(10)
        h = ma.full(ma.real, ma.maxsize)
        if h == 1:
            print("is full")
            return
        else:
            t = ma.e()
            if t == 1:
                real += 1
                arr.append(n)
            else:
                real += 1
                arr[real] = n
        return real, arr
    def e(self):
        if Duilie(10).real == Duilie(10).front:
            u = 1
        else:
            u = 2
        return u
    def get(self):
        n = ma.empty(ma.front, ma.real)
        if n == 1:
            print("is empmy")
            return
        else:
            ma.front += 1
            return ma.arr[ma.front]

ma = Duilie(10)
real, arr = ma.addqueue(1, ma.real, ma.arr)
print(arr)
p = ma.full(ma.real, ma.maxsize)
