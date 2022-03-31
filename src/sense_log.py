from logging import getLogger
from time import sleep
from sense_hat import SenseHat
from log import setup_logger
from utils import ceil


def ceil_dict(dict, digit = 0):
    return {
        key: ceil(val, digit) for key,val in dict.items()
    }

logger = setup_logger("log/sense_test.log")

if __name__ == '__main__':
    sense = SenseHat()

    while True:
        orientation_degrees = sense.get_orientation_degrees()
        logger.info("orientation", ceil_dict(orientation_degrees, 1))
        
        accelerometer = sense.get_accelerometer_raw()
        logger.info("accel", ceil_dict(accelerometer, 3))
        
        north = sense.get_compass()
        logger.info("compass", ceil(north, 2))
        
        gyro = sense.get_gyroscope()
        logger.info("gyro", ceil_dict(gyro))
        
        sleep(1)
