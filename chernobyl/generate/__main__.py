import os
import logging
import argparse
import sys
import shutil
from chernobyl import Path, ControllerGenerator

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='New a simple web app')
parser.add_argument('module_name', type=str,
                    help='module name')

parser.add_argument('controller', type=str,
                    help='controller name')

args = parser.parse_args()

module_name = args.module_name
controller = args.controller

module = Path(module_name)
controller_templates = Path("chernobyl").append("new").append("controller").append("templates")
controllers = module.append("controllers")

c = ControllerGenerator(controller, module)
c.create_controller()
c.create_views()
