class ArgumentFileParser(object):
    
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        raise NotImplementedError()

