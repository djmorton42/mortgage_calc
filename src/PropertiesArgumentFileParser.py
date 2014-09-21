from ArgumentFileParser import ArgumentFileParser

class PropertiesArgumentFileParser(ArgumentFileParser):
    def __init(self, filename):
        super(PropertiesArgumentFileParser, self).__init__(filename)

    def parse(self):
        print("I'm parsing some properties from file " + self.filename)