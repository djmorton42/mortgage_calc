import locale

class OutputRenderer(object):
    def __init__(self):
        locale.setlocale(locale.LC_ALL, '')

    def render(self, table):
        raise NotImplementedError()
