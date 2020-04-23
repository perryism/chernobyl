from chernobyl import Template, basic_reader
import logging

logger = logging.getLogger(__name__)

#https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/
change_case = lambda x: ''.join(['_'+i.lower() if i.isupper() else i for i in x]).lstrip('_')

class ControllerGenerator:
    def __init__(self, name, module_path):
        self.name = name
        self.module_path = module_path
        self.lower_name = name.lower()
        self.underscore_name = change_case(name)
        self.absolute_path = module_path.append("controllers").file("%s_controller.py"%self.underscore_name)

    def create_controller(self, controller_templates):
        template = Template(controller_templates.file("controller.py"))
        template.write(self.absolute_path, controller_name = self.name)

        controller_init = self.module_path.append("controllers").file("__init__.py")
        logger.debug("Add import statement to %s"%controller_init)
        with open(controller_init, "a+") as f:
            f.write("from .%s_controller import %sController\n"%(self.underscore_name, self.name))

    def create_views(self, controller_templates):
        template_view_path = controller_templates.append("views")
        views = self.module_path.append("views").append(self.underscore_name)
        views.create()
        template = Template(template_view_path.file("index.html"), basic_reader)
        template.write(views.file("index.html"), controller_name=self.underscore_name)
        views.copy_from(template_view_path.file("show.html"))
