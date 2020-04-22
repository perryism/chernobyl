from . import ControllerBase
from flask import request

class {{ controller_name }}Controller(ControllerBase):
    ALPHABETS = ["a", "b", "c"]
    def index(self):
        return { "alphabets": enumerate(self.__class__.ALPHABETS) }

    def show(self):
        key = self.params["key"]
        return { "alphabet": self.__class__.ALPHABETS[int(key)] }

    def edit(self):
        pass
