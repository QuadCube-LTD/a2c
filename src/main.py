from datetime import datetime
from time import sleep
from typing import List

from Array import Array
from a2c import A2C
import config
from log import setup_logger
from utils import  average, Vector, ceil

# from sense_hat import SenseHat
class SenseHat():
    def get_accelerometer_raw(self):
        return {"x": 1, "y": 2, "z": 3}

logger = setup_logger(
    filename = config.LOG_FILE_NAME,
    format = config.LOGGER_SEPARATOR.join(["%(levelname)s","%(message)s","%(created)s"])
    )
    # LEVEL,CREATED,X,Y,Z

sense = SenseHat()

a2c = A2C()

def sense_accelerations(
    repeat: int, 
    sleep_second: float,
    init_tolerances: Vector = {"x": 0, "y": 0, "z": 0}
    ) -> List[Vector]:

    def sense_acc() -> Vector:
        acc = sense.get_accelerometer_raw()
        sleep(sleep_second)
        return {
            "x": acc["x"] - init_tolerances["x"],
            "y": acc["y"] - init_tolerances["y"],
            "z": acc["z"] - init_tolerances["z"]
        }

    return [sense_acc() for _ in range(repeat)]

def get_initial_accelerations() -> Vector:
    accs = sense_accelerations(repeat = 10, sleep_second = 0.5)
    return { 
        "x": average([acc["x"] for acc in accs]),
        "y": average([acc["y"] for acc in accs]),
        "z": average([acc["z"] for acc in accs])
    }

def generate_log_message():
    return Array(a2c.xyz["x"], a2c.xyz["y"], a2c.xyz["z"])\
        .map_(lambda x: ceil(x, digit = config.NTH_DECIMAL_PLACE) )\
        .map_(lambda x: str(x))\
        .join_(config.LOGGER_SEPARATOR)

def main():
    initial_accelerations: Vector = get_initial_accelerations()

    while True:
        old_time = datetime.now().timestamp()

        accelerations: List[Vector] = sense_accelerations(
            repeat = config.REPEAT,
            sleep_second = config.SLEEP_SECOND,
            init_tolerances = initial_accelerations
        )
        
        now_time = datetime.now().timestamp()

        interval: float = now_time - old_time
        
        a2c.update(accelerations, interval)

        logger.info(generate_log_message())


if __name__ == "__main__":
    main()