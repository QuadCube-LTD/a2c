from time import sleep
from typing import List, Tuple
import utils

Matrix1d = List[float]
Vector = Tuple[float,float,float]


class A2C():
    def __init__(
        self, 
        initial_velocities: Vector = (0, 0, 0),
        initial_xyz: Vector = (0, 0, 0)
        ):
        
        self.velocities = initial_velocities
        self.xyz = initial_xyz


    def update(self, accelerations: List[Vector], delta_t: float):
        accels: Tuple[Matrix1d,Matrix1d,Matrix1d] = utils.T(accelerations)

        new_v=[]
        new_xyz=[]

        for v0, x0, a in zip(self.velocities, self.xyz, accels):
            v = self.calc_velocity(acceleration=a, delta_t=delta_t, v0=v0)
            new_v.append(v)

            x = self.calc_x(acceleration=a, delta_t=delta_t, v0=v0, x0=x0)
            new_xyz.append(x)

        self.velocities = new_v
        self.xyz = new_xyz


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
