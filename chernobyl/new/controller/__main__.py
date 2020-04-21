import os
import logging

logger = logging.getLogger(__name__)
def create_folder(folder):
    if not os.path.exists(folder):
        logger.debug("Creating folder %s"% folder)
        os.makedirs(folder)
import argparse
import sys
import shutil
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
parser = argparse.ArgumentParser(description='New a simple web app')
parser.add_argument('project_name', type=str,
                    help='project name')

parser.add_argument('controller', type=str,
                    help='controller name')

args = parser.parse_args()
project_name = args.project_name
controller = args.controller
package_path = os.path.join(args.project_name, args.project_name)

#shutil.copytree(os.path.join("chernobyl", "new", "controller", "templates", "views"), os.path.join(package_path, "views", controller.lower()))

from jinja2 import Template

def read(path):
    with open(path, 'r') as f:
        return f.read()

def read_template(path):
    return Template(read(path))

template = read_template(os.path.join("chernobyl", "new", "controller", "templates", "controller.py"))
with open(os.path.join(package_path, "controllers", "%s_controller.py"%controller.lower()), 'w') as f:
    f.write(template.render(controller_name = controller))

create_folder(os.path.join(package_path, "views"))
create_folder(os.path.join(package_path, "views", controller.lower()))

template = read(os.path.join("chernobyl", "new", "controller", "templates", "views", "index.html"))
with open(os.path.join(package_path, "views", controller.lower(), "index.html"), 'w') as f:
    content = template.replace("%%controller_name%%", controller.lower())
    f.write(content)

shutil.copy2(os.path.join("chernobyl", "new", "controller", "templates", "views", "show.html"), os.path.join(package_path, "views", controller.lower(), "show.html"))

with open(os.path.join(package_path, "controllers", "__init__.py"), "a+") as f:
    f.write("from .%s_controller import %sController"%(controller.lower(), controller) )

