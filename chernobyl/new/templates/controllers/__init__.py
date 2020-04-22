import os

from jinja2 import Template


VIEW_PATH = os.path.join(__package__.replace(".controllers", ""),"views")

def template(controller, name):
    def decorator(func):
        def wrapped_function(*args):
            template_path = os.path.join(VIEW_PATH, controller, "%s.html"%name)
            with open(template_path, "r") as f:
                template = Template(f.read())
            results = func(*args)
            return template.render(**results)
        return wrapped_function
    return decorator

from .controller_base import ControllerBase
