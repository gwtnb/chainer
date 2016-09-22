from chainer import link


class DummyLink(link.Link):
    def __init__(self, func):
        self._func = func
        super(DummyLink, self).__init__()

    def __call__(self, *args):
        return self._func(*args)
