from time import sleep
from typing import List, Literal

from utils import Vector, average


class A2C():
    def __init__(
        self, 
        initial_velocities: Vector = {"x": 0, "y": 0, "z": 0},
        initial_xyz: Vector        = {"x": 0, "y": 0, "z": 0}
        ):
        
        self.velocities = initial_velocities
        self.xyz        = initial_xyz


    def update(self, accelerations: List[Vector], delta_t: float):
        def new_velocity(key: Literal["x","y","z"]):
            return self.calc_velocity(
                acceleration = average([a[key] for a in accelerations]), 
                delta_t      = delta_t, 
                v0           = self.velocities[key]
                )

        self.velocities = {
            "x": new_velocity("x"),
            "y": new_velocity("y"),
            "z": new_velocity("z")
            }

        def new_xyz(key: Literal["x","y","z"]):
            return self.calc_x(
                acceleration = average([a[key] for a in accelerations]), 
                delta_t      = delta_t, 
                v0           = self.velocities[key], 
                x0           = self.xyz[key]
                )  

        self.xyz = {
            "x": new_xyz("x"),
            "y": new_xyz("y"),
            "z": new_xyz("z")
            }


    def calc_velocity(
        self, 
        acceleration: float, 
        delta_t: float, 
        v0: float
        ) -> float:
        """
        v = (a * Δt) + v0 
        """
        return acceleration * delta_t + v0


    def calc_x(
        self, 
        acceleration: float, 
        delta_t: float, 
        v0: float, 
        x0: float
        ) -> float:
        """
        x = (1/2 * a * Δt^2) + (v0 * Δt) + x0 = (v * Δt) + v0
        """
        return 1/2 * acceleration * (delta_t ** 2) + (v0 * delta_t) + x0
