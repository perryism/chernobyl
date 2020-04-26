import argparse
import logging
import os
import sys
from chernobyl.path import Path

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='New a simple web app')
parser.add_argument('project_name', type=str,
                    help='project name')

parser.add_argument('--module_name', type=str, required=False, help='module name')

args = parser.parse_args()
project_name = args.project_name
module_name = args.module_name

chernobyl = Path(os.path.dirname(__file__)).append("..")
new_templates = chernobyl.append("new").append("templates")

project = Path(project_name)
module = project.append(module_name or project_name)
web = module.append("web")
web.create()

web.copy_from(chernobyl.file("chernobyl.py"))
web.copy_from(new_templates.file("__init__.py"))
web.copy_from(new_templates.file("__main__.py"))
project.copy_from(new_templates.file("requirements.txt"))
project.copy_from(new_templates.file(".gitignore"))
project.copy_from(new_templates.file(".author"))
module.append("controllers").copy_from(new_templates.append("controllers"))

project.append("chernobyl").copy_from(chernobyl)
