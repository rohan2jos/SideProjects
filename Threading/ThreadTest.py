import threading
import time

def blockingThreadFunc(no, ev):
    print "entered blocking thread function, this thread will wait till the event has been set"
    event_set = ev.wait()
    print str(no) + ": event: %s", event_set


def nonBlockingThreadFunc(e, t):
    print "entered non-blocking thread function"
    while not e.isSet():
        print "nonBlockingThreadFunc will timeout for e, and continue its work till e is set"
        event_set = e.wait(t)
        print "event: %s", event_set
        if event_set:
            print "event set, will process event now"
        else:
            print "event is not set, will continue doing other work"

e = threading.Event()
t1 = threading.Thread(target=blockingThreadFunc, args=(1, e))
t1.start()

t3 = threading.Thread(target=blockingThreadFunc, args=(3, e))
t3.start()

t2 = threading.Thread(target=nonBlockingThreadFunc, args=(e, 2))
t2.start()

print "main will sleep 9 seconds before event is set"
time.sleep(9)
e.set()
print "event has been set"
