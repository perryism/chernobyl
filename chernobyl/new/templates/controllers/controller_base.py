from . import template

class ControllerBase(object):
    def name(self):
        basename = self.__class__.__name__
        return basename.replace("Controller", "").lower()

    def index_base(self):
        return template(self.name(), "index")(self.index)()

    def show_base(self):
        return template(self.name(), "show")(self.show)()

    def edit_base(self):
        return self.edit()

    def default_path(self):
        return "/%s"%self.name()

    def show_path(self):
        return "%s/show"%self.default_path()

    def edit_path(self):
        return "%s/edit"%self.default_path()
