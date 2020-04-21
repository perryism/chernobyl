import logging, sys
from . import Chernobyl

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

c = Chernobyl(__package__)
c.run(host='0.0.0.0',port=5555)
