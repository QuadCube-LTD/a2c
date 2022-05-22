from logging import getLogger
from time import sleep
from sense_hat import SenseHat
from log import setup_logger
from utils import ceil

# class SenseHat():
#     def get_orientation_degrees(self):
#         return {"pitch": 1, "roll": 2, "yaw": 3}
#     def get_accelerometer_raw(self):
#         return {"x": 1, "y": 2, "z": 3}
#     def get_compass_raw(self):
#         return {"x": 1, "y": 2, "z": 3}
#     def get_gyroscope(self):
#         return {"x": 1, "y": 2, "z": 3}

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
        logger.info("compass", north)
        
        gyro = sense.get_gyroscope()
        logger.info("gyro", ceil_dict(gyro))
        
        sleep(1)
