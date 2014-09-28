from ArgumentFileParser import ArgumentFileParser
from JsonArgumentFileParser import JsonArgumentFileParser
from PropertiesArgumentFileParser import PropertiesArgumentFileParser
from YamlArgumentFileParser import YamlArgumentFileParser

class ArgumentFileParserFactory(object):
    @classmethod
    def get_instance(clazz, filename):
        if filename.lower().endswith(".yaml"):
            return YamlArgumentFileParser(filename)
        elif filename.lower().endswith(".json"):
            return JsonArgumentFileParser(filename)
        elif filename.lower().endswith(".properties"):
            return PropertiesArgumentFileParser(filename)
        else:
            raise NotImplementedError("This file type is not supported")