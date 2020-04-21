import os
import logging

logger = logging.getLogger(__name__)
def create_folder(folder):
    if not os.path.exists(folder):
        logger.debug("Creating folder %s"% folder)
        os.makedirs(folder)
    else:
        raise "Folder exists"

import sys
import argparse
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
parser = argparse.ArgumentParser(description='New a simple web app')
parser.add_argument('project_name', type=str,
                    help='an integer for the accumulator')

args = parser.parse_args()
project_name = args.project_name
create_folder(project_name)
package_path = os.path.join(args.project_name, args.project_name)
create_folder(package_path)

import shutil
shutil.copy2(os.path.join("chernobyl", "chernobyl.py"), package_path)

from pathlib import Path
shutil.copy2(os.path.join("chernobyl", "new", "templates", "__init__.py"), package_path)
shutil.copy2(os.path.join("chernobyl", "new", "templates", "__main__.py"), package_path)
shutil.copy2(os.path.join("chernobyl", "new", "templates", "requirements.txt"), project_name)

shutil.copytree(os.path.join("chernobyl", "new", "templates", "controllers"), os.path.join(package_path, "controllers"))
