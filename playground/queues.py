from Queue import Queue
import signal


q = Queue()


def handler(signum, frame):
    print signum
    import traceback
    traceback.print_stack(frame)

    signals = [
        signal.SIGALRM,
        signal.SIGTERM,
        signal.SIGQUIT
    ]
    map(lambda sig: signal.signal(sig, handler), signals)


print q.get(timeout=5)
