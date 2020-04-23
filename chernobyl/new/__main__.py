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
parser.add_argument('--bootstrap', action='store_const', const=True,
                    help='bootstrap existing project')
args = parser.parse_args()
project_name = args.project_name
bootstrap = args.bootstrap
exist_ok = bootstrap

basepath = os.path.dirname(__file__)

chernobyl = Path(os.path.join(basepath, "..", "..", "chernobyl"))
new_templates = chernobyl.append("new").append("templates")

project = Path(project_name)
module = project.append(project_name)

module.create(exist_ok)

module.copy_from(chernobyl.file("chernobyl.py"), exist_ok)
module.copy_from(new_templates.file("__init__.py"), exist_ok)
module.copy_from(new_templates.file("__main__.py"), exist_ok)
project.copy_from(new_templates.file("requirements.txt"), exist_ok)
project.copy_from(new_templates.file(".gitignore"), exist_ok)
project.copy_from(new_templates.file(".author"), exist_ok)

if bootstrap:
    # not support
    # copy individual items
else:
    module.append("controllers").copy_from(new_templates.append("controllers"), exist_ok)
