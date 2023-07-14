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
    
    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(20, 19),1.0526315789473684)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(1,3), 0.3333333333333333)
        self.assertEqual(physics.calculate_angular_acceleration(1,5), 0.2 )

    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(1,-6, 5), 1.3970774909946293)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(100,4), 1600)
