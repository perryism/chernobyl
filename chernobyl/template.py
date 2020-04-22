import logging

logger = logging.getLogger(__name__)

def read(path):
    with open(path, 'r') as f:
        return f.read()

import jinja2
def jinja_reader(template, args):
    template = jinja2.Template(template)
    return template.render(**args)

def basic_reader(template, args):
    for k, v in args.items():
        template = template.replace("!!%s!!"%k, v)
    return template

class Template(object):
    def __init__(self, filepath, render=jinja_reader):
        logger.debug("Reading template from %s"%filepath)
        self.template = read(filepath)
        self.render = render

    def write(self, destpath, **args):
        logger.debug("Saving template to %s"%destpath)

        content = self.render(self.template, args)

        with open(destpath, "w") as f:
            f.write(content)
