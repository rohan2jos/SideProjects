import threading
import time
import random

class Counter():
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        print "[Counter.increment()] waiting to acquire lock"
        self.lock.acquire()
        try:
            print "[Counter.incremenet()] trying to increment"
            self.value += 1
            print "value is now " + str(self.value)
        finally:
            self.lock.release()


def worker(c):
    print "[worker()] entered worker"

    for i in range(0, 2):
        print "spawning and pausing in iteration " + str(i)
        pause = random.random()
        print "pausing for " + str(pause)
        time.sleep(pause)
        c.increment()
    print "done"

counter = Counter()
t1 = threading.Thread(target=worker, args=(counter, ))
t1.start()
t2 = threading.Thread(target=worker, args=(counter, ))
t2.start()
main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

print "final counter value = " + str(counter.value)