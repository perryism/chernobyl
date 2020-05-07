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
parser.add_argument('--bootstrap', action='store_const', const=True, help='install bootstrap')


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

if args.bootstrap:
    bootstrap_download = "https://github.com/twbs/bootstrap/releases/download/v4.4.1/bootstrap-4.4.1-dist.zip"
    import tempfile
    from urllib.request import urlopen
    import zipfile

    directory_to_extract_to = "/tmp"
    with tempfile.NamedTemporaryFile() as t:
        response = urlopen(bootstrap_download)
        print(t.name)
        with open(t.name, "wb") as f:
            f.write(response.read())

        with zipfile.ZipFile(t.name, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

    static = web.append("static")
    static.copy_from(Path("/tmp/bootstrap-4.4.1-dist"))
