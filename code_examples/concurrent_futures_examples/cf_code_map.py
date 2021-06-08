from concurrent.futures import ThreadPoolExecutor
import re
from pprint import pprint
import time
import random
import logging


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(threadName)s %(name)s %(levelname)s: %(message)s", level=logging.DEBUG
)


def do_thing_1(thing_id):
    logging.debug(f"Start do_thing_1 {thing_id}")
    time.sleep(random.random() * 3)
    logging.debug(f"Stop  do_thing_1 {thing_id}")


def do_thing_2(thing_id):
    logging.debug(f"Start do_thing_2 {thing_id}")
    time.sleep(random.random())
    #logging.debug(f"Stop  do_thing_2 {thing_id}")


def do_things_in_threads(workers=5):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results1 = executor.map(do_thing_1, range(1, 11))
        results2 = executor.map(do_thing_2, range(101, 111))
        for _ in results1:
            pass
        for _ in results2:
            pass


if __name__ == "__main__":
    do_things_in_threads()
