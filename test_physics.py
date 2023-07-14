import unittest
import physics

class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(100,10), 9800.0)
        self.assertEqual(physics.calculate_buoyancy(100,1), 980.0000000000001)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(200,30,10), False)
        self.assertEqual(physics.will_it_float(100,10,20), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(20), 196000.0 )
    def calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(20),34)
    