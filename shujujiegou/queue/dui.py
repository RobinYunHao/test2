from shujujiegou.queue.queue import Duilie
am = Duilie(10)
print(am.maxsize)
am.real, am.arr = am.addqueue(5, am.real, am.arr)
m = am.get()
print(m)
