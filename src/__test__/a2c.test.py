import unittest
import os 
import sys
sys.path.append(os.path.abspath(".."))

from a2c import A2C


class A2Cのテスト(unittest.TestCase):

    def setUp(self):
        self.a2c = A2C()
        

    def test_加速度からグローバル直交座標を算出(self):
        self.a2c.update(
            accelerations = [
                {"x":1, "y":0, "z":0},
                {"x":2, "y":0, "z":0},
                {"x":3, "y":0, "z":0}
                ],
            delta_t = 3
            )
        received = self.a2c.xyz

        expected = {
            "x": self.a2c.calc_x(acceleration = 2, delta_t = 3, v0 = 0, x0 = 0),
            "y": 0,
            "z": 0,
            }
        self.assertEqual(received, expected)


    def test_加速度から速度を算出(self):
        """
        v = (a * Δt) + v0 
        """
        received = self.a2c.calc_velocity(acceleration=1.2,delta_t=1.0, v0=0.2)
        expected = 1.4
        self.assertEqual(received, expected)


    def test_加速度から位置を算出(self):
        """
        x = (1/2 * a * Δt^2) + (v0 * Δt) + x0 = (v * Δt) + v0
        """
        received = self.a2c.calc_x(acceleration=1.2, delta_t=1.0, v0=0.2, x0=3.0)
        expected = (1/2 * 1.2 * (1.0**2)) + (0.2*1.0) + 3.0
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
