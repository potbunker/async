import logging
import sys

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(threadName)s [%(filename)s:%(lineno)d] %(message)s')
logger =  logging.getLogger(__name__)

