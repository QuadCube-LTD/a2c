from datetime import datetime
from logging import getLogger
from sense_hat import SenseHat
from time import sleep
from typing import List, Tuple
from a2c import A2C
from log import setup_logger

Vector = Tuple[float,float,float]

SLEEP_TIME = 0.1
COUNT = 10

logger = setup_logger("log/a2c.log")
sense = SenseHat()


if __name__ == "__main__":
    a2c = A2C()

    while True:
        old_time = datetime.now().timestamp()

        accelerations: List[Vector] 
        for _ in range(COUNT):
            sleep(SLEEP_TIME)
            acc: Vector = sense.get_accelerometer_raw()
            accelerations.append(acc) 
        
        now_time = datetime.now().timestamp()

        interval: float = now_time - old_time
        
        a2c.update(accelerations, interval)

        logger.info("xyz:",a2c.xyz)
        logger.info("velocities:",a2c.velocities)
