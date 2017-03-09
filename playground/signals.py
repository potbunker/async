import signal,time

def signal_handler(signum, stack):
    print 'Received:', signum

signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(15, signal_handler)

while True:
    print 'Waiting...try kill using signal 1(SIGHUP) or 2(SIGINT)'
    time.sleep(3)