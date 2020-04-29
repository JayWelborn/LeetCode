import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = threading.Lock()
        self.barLock = threading.Lock()
        self.fooLock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.barLock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.fooLock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.fooLock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.barLock.release()
