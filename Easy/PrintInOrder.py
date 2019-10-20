import threading
class Foo:
    def __init__(self):
        self.second_lock = threading.Lock()
        self.third_lock = threading.Lock()
        self.second_lock.acquire()
        self.third_lock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.second_lock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.third_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
