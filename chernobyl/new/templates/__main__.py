import logging, sys
import argparse
from . import Chernobyl

parser = argparse.ArgumentParser(description='New a simple web app')
parser.add_argument("--log", choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="INFO",
                    help="Log level")
parser.add_argument("--port", type=int, default=5555, help="Port")

args = parser.parse_args()

logging.basicConfig(level=getattr(logging, args.log), stream=sys.stdout)
logger = logging.getLogger(__name__)

c = Chernobyl(__package__.replace(".web", ""))
c.run(host='0.0.0.0',port=args.port)
