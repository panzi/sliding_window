from collections import deque

__all__ = ['window']

# Python 2 compatibility
try:
    xrange
except NameError:
    xrange = range

def window(seq, n=2, default=None):
    it = iter(seq)
    win = deque((next(it, default) for _ in xrange(n)), maxlen=n)
    yield tuple(win)
    append = win.append
    for e in it:
        append(e)
        yield tuple(win)
