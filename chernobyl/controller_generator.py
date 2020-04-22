from chernobyl import Template, basic_reader
import logging

logger = logging.getLogger(__name__)

class ControllerGenerator:
    def __init__(self, name, module_path):
        self.name = name
        self.module_path = module_path
        self.lower_name = name.lower()
        self.absolute_path = module_path.append("controllers").file("%s_controller.py"%self.lower_name)

    def create_controller(self, controller_templates):
        template = Template(controller_templates.file("controller.py"))
        template.write(self.absolute_path, controller_name = self.name)

        controller_init = self.module_path.append("controllers").file("__init__.py")
        logger.debug("Add import statement to %s"%controller_init)
        with open(controller_init, "a+") as f:
            f.write("from .%s_controller import %sController\n"%(self.lower_name, self.name))

    def create_views(self, controller_templates):
        template_view_path = controller_templates.append("views")
        views = self.module_path.append("views").append(self.lower_name)
        views.create()
        template = Template(template_view_path.file("index.html"), basic_reader)
        template.write(views.file("index.html"), controller_name=self.lower_name)
        views.copy_from(template_view_path.file("show.html"))
