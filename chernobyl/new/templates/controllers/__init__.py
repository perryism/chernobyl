import os

from jinja2 import Template


VIEW_PATH = os.path.join(__package__.replace(".controllers", ""),"views")

def template(controller, name):
    def decorator(func):
        def wrapped_function(*args):
            template_path = os.path.join(VIEW_PATH, controller, "%s.html"%name)
            print(template_path)
            with open(template_path, "r") as f:
                template = Template(f.read())
            results = func(*args)
            return template.render(**results)
        return wrapped_function
    return decorator

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
