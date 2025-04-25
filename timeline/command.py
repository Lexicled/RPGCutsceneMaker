import random

class Command:
    def __init__(self, start: int, end: int, parameters: dict = {}, specific_params: list = [],
                 requirements: list = [], tag: str = "", visible: bool = True):
        self.id = str("%05d" % (random.randint(0, 99999),))
        self.tag = tag
        self.visible = visible
        self.syntax = ""                    # Surround parameter names with '|', e.g. "functionName(|param1|, |param2|, |anotherParam|)"
        self.params = parameters            # Parameter names and values
        self.specific_param_indexes = {}    # Format: {"parameter_name": <parameter index: int>, "paramter_2_name": <parameter index 2} - pull parameter indexes from
                                            # specific_params
        self.requirements = requirements
        self.start = start
        self.end = end
    
    def duration(self):
        return self.end - self.start

    def action(self):
        pass # Modified in subclasses where relevant

# TODO add unit test