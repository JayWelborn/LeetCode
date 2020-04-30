import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.e = threading.Lock()
        self.o = threading.Lock()
        self.z = threading.Lock()
        self.e.acquire()
        self.o.acquire()
        
           
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n + 1):
            self.z.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.e.release()
            else: 
                self.o.release()
        
          
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n + 1):
            if i % 2 == 0:
                self.e.acquire()
                printNumber(i)
                self.z.release()
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n + 1):
            if i % 2 == 1:
                self.o.acquire()
                printNumber(i)
                self.z.release()

