from datetime import datetime
from time import sleep
from typing import List

from a2c import A2C
import config
from log import setup_logger
from utils import join_number, Vector

# from sense_hat import SenseHat
from random import random
class SenseHat():
    def get_accelerometer_raw(self):
        return {"x": 1, "y": 2, "z": 3}

logger = setup_logger(
    filename = "log/a2c.csv",
    format = config.LOGGER_SEPPARATOR.join(["%(levelname)s","%(created)s","%(message)s"])
    )
    # LEVEL,CREATED,X,Y,Z,Vx,Vy,Vz

sense = SenseHat()

a2c = A2C()

def sense_accelerations(count: int, sleep_time: float) -> List[Vector]:
    def sense_acc() -> Vector:
        sleep(sleep_time)
        return sense.get_accelerometer_raw()

    return [sense_acc() for _ in range(count)]


def main():
    while True:
        old_time = datetime.now().timestamp()

        accelerations: List[Vector] = sense_accelerations(
            count = config.COUNT,
            sleep_time = config.SLEEP_TIME
        )
        
        now_time = datetime.now().timestamp()

        interval: float = now_time - old_time
        
        a2c.update(accelerations, interval)

        logger.info(join_number([
            a2c.xyz["x"], 
            a2c.xyz["y"], 
            a2c.xyz["z"]]),
            sep = config.LOGGER_SEPPARATOR
            )


if __name__ == "__main__":
    main()