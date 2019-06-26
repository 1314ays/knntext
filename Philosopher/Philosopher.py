import threading
from time import sleep
import random

numPhilosophers = numForks = 5

class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index  
        self.leftFork = forks[self.index]
        self.rightFork = forks[(self.index + 1) % numForks]

    def run(self):
        while True:
            if self.leftFork.ke()==0 and self.rightFork.ke()==0:
                self.leftFork.pickup()
                self.rightFork.pickup()
                self.dining()
                self.rightFork.putdown()
                self.leftFork.putdown()
                self.thinking()
            

    def dining(self):
        print("Philosopher", self.index, " starts to eat.")
        sleep(random.uniform(1,3)/1000)
        print("Philosopher", self.index, " finishes eating and leaves to think.")

    def thinking(self):
        sleep(0)

class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()
        self.key = 0
        self.rkey = 1

    def ke(self):
        return self.key

    def pickup(self):
        self.key = 1
        self._lock.acquire()

    def putdown(self):
        self.key = 0
        self._lock.release()

if __name__ == '__main__':
    forks = [Fork(idx) for idx in range(numForks)]
    philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]
    for philosopher in philosophers:
            philosopher.start()

    try:
        while True: sleep(0.1)
    except Exception as e:
        raise e
