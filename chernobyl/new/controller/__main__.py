import os
import logging
import argparse
import sys
import shutil
from chernobyl import Path, Controller

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='New a simple web app')
parser.add_argument('project_name', type=str,
                    help='project name')

parser.add_argument('controller', type=str,
                    help='controller name')

args = parser.parse_args()
project_name = args.project_name

controller = args.controller

module = Path(args.project_name).append(args.project_name)
controller_templates = Path("chernobyl").append("new").append("controller").append("templates")
controllers = module.append("controllers")

c = Controller(controller, module)
c.create_controller(controller_templates)
c.create_views(controller_templates)
