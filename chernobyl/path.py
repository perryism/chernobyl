import os
import pathlib
import shutil
import logging

logger = logging.getLogger(__name__)

class Path(object):
    def __init__(self, path, parent = None):
        self.path = path
        self.parent = parent
        self.absolute_path = path if parent is None else os.path.join(str(parent), path)

    def create(self, exist_ok=False):
        logger.debug("Creating %s"%self.absolute_path)
        pathlib.Path(self.absolute_path).mkdir(parents=True, exist_ok=exist_ok)

    def append(self, name):
        return Path(name, self)

    def file(self, name):
        return os.path.join(self.absolute_path, name)

    def copy_from(self, src_path, exist_ok=False):
        src_path = str(src_path)
        logger.debug("Copy from %s to %s"%(src_path, self.absolute_path))
        if os.path.isdir(src_path):
            shutil.copytree(src_path, self.absolute_path, dirs_exist_ok=exist_ok)
        else:
            dest_path = os.path.join(self.absolute_path, os.path.basename(src_path))
            if os.path.exists(dest_path):
                if not exist_ok:
                    raise FileExistsError(dest_path)
                logger.info("%s already exists"%dest_path)
            else:
                shutil.copy2(src_path, dest_path)

    def __str__(self):
        return self.absolute_path
