import threading
import time



'''
a producer consumer program in python

following tutorial on: https://pymotw.com/2/threading/

this program has two threads: the producer and the consumer

The producer will keep producing resources for the consumer to consume
However, if the consumer is consuming resources faster than the producer can produce, it will
have to wait till the resources are available

if the producer is producing resources faster than the consumer can consume, it will put the
produced resource in a pool and continue producing
the consumer will then pick the resource from the pool of produced resources to consume
'''
queue = []
def consumer(cond):
    print "entered consumer ", threading.currentThread().getName()
    lock = threading.Lock()
    with cond:
        cond.wait()
        print "just got a notification that the resource has been made available to some consumer, ", threading.currentThread().getName()
        lock.acquire()
        if lock:
            while len(queue) > 0:
                data = queue.pop()
                print threading.currentThread().getName() + " has just popped: " + data
                lock.release()


def producer(cond):
    print "entered producer"
    i = 0
    for k in range(2):
        with cond:
            for i in range(4):
                print "i is now " + str(i)
                time.sleep(1)
                i += 1

            print "i is now 4, making condition available to the consumers"
            global queue
            queue.append("data that the producer has put")
            cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name='consumer 1', target=consumer, args=(condition, ))
c2 = threading.Thread(name='consumer 2', target=consumer, args=(condition, ))
c3 = threading.Thread(name='consumer 3', target=consumer, args=(condition, ))
p1 = threading.Thread(name='producer 1', target=producer, args=(condition, ))
c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
c3.start()
time.sleep(1)
p1.start()
time.sleep(2)