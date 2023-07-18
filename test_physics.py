import unittest
import physics
import numpy as np

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
        self.assertEqual(physics.calculate_torque(1,-6, 5), -0.5226423163382673)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(100,4), 1600)
    
    def test_calculate_auv_acceleration(self):
        self.assertTrue(np.allclose((physics.calculate_auv_acceleration(100,np.pi/2), np.array([2*np.cos(np.pi/2),2*np.sin(np.pi/2)]))))
    
    def test_calculate_auv_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv_angular_acceleration(45,30), -22.23071154208939)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(-3,4), 5)
    
    def test_calculate_auv2_acceleration(self):
        self.assertEqual(physics.calculate_auv2_acceleration([3, 3, 3, 3], 10, 10), [0, 0])
        self.assertEqual(physics.calculate_auv2_acceleration([5, 6, 2, 9], 98, 0.76), [-0.0237, -0.02493])

        self.assertNotEqual(physics.calculate_auv2_acceleration([0, 3, 4.5, 9], 9, 72), [23.5, -0.2222])
        self.assertNotEqual(physics.calculate_auv2_acceleration([3, 1, 5.6, 0.2], 8, 3), [7, 0.00043])

    def test_calculate_auv2_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv2_angular_acceleration([3, 3, 3, 3], 4, 7, 5), 0)
        self.assertEqual(physics.calculate_auv2_angular_acceleration([5, 6, 2, 9], 2, 4.3, 0.4), 5.45578)

        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([0, 3, 4.5, 9], 23, 1, 2), 9)
        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([3, 1, 5.6, 0.2], 23, 9.88, 0.0002), -0.002)

        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 3, 3, 3], 23, -1, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [5, 6, 2, 9], 23, 0, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [0, 3, 4.5, 9], 23, 1, -1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, -1)
