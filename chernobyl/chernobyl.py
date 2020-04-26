from flask import Flask
import logging

logger = logging.getLogger(__name__)

class Chernobyl:
    def __init__(self, package):
        self.package = package
        self.app = Flask(__name__)

    def run(self, **args):
        for controller in self.controllers():
            logger.debug("Adding %s controller"%controller.name())
            logger.debug("Adding %s"%controller.default_path())
            logger.debug("Adding %s"%controller.show_path())
            logger.debug("Adding %s"%controller.edit_path())
            self.app.add_url_rule(controller.default_path(), controller.name(), controller.index_base, methods=["GET", "POST"])
            self.app.add_url_rule(controller.show_path(), controller.show_path(), controller.show_base, methods=["GET", "POST"])
            self.app.add_url_rule(controller.edit_path(), controller.edit_path(), controller.edit, methods=["POST"])

        logger.info(self.app.url_map)
        self.app.run(**args)

    def controllers(self):
        module = self.controller_module()
        for i in dir(module):
            item = getattr(module, i)
            if self.is_controller(module, item):
               yield item()

    def controller_module(self):
        return __import__("%s.controllers"%self.package).controllers

    def is_controller(self, module, item):
        return type(item) is type and issubclass(item, module.ControllerBase) and item is not self.controller_module().ControllerBase
