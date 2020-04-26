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

args = parser.parse_args()
project_name = args.project_name

chernobyl = Path("chernobyl")
new_templates = chernobyl.append("new").append("templates")

project = Path(project_name)
module = project.append(project_name)
module.create()

module.copy_from(chernobyl.file("chernobyl.py"))
module.copy_from(new_templates.file("__init__.py"))
module.copy_from(new_templates.file("__main__.py"))
project.copy_from(new_templates.file("requirements.txt"))
project.copy_from(new_templates.file(".gitignore"))
project.copy_from(new_templates.file(".author"))
module.append("controllers").copy_from(new_templates.append("controllers"))

project.append("chernobyl").copy_from(chernobyl)
