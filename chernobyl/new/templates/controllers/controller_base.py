from .params import Params
from . import template

#https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/
change_case = lambda x: ''.join(['_'+i.lower() if i.isupper() else i for i in x]).lstrip('_')

class ControllerBase(object):
    def __init__(self):
        self.params = Params()

    def name(self):
        basename = self.__class__.__name__
        return change_case(basename.replace("Controller", ""))

    def index_base(self):
        if self.return_json(self.index):
            return self.index()
        return template(self.name(), "index")(self.index)()

    def show_base(self):
        if self.return_json(self.show):
            return self.show()
        return template(self.name(), "show")(self.show)()

    def edit_base(self):
        return self.edit()

    def default_path(self):
        return "/%s"%self.name()

    def show_path(self):
        return "%s/show"%self.default_path()

    def edit_path(self):
        return "%s/edit"%self.default_path()

    def return_json(self, func):
        """
        if the path returns dict, templates will be skipped
        """
        return "return" in func.__annotations__ and func.__annotations__["return"] == dict
