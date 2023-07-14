import unittest
import hello



class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_div(self):
        self.assertEqual(hello.div(46,75), 0.6133333333333333)
        self.assertEqual(hello.div(1,1.5), 0.6666666666666666)
        self.assertNotEqual(hello.div(0,2),3)

    def test_mul(self):
        self.assertEqual(hello.mul(1,2), 2)
        self.assertEqual(hello.mul(3,4), 12)
        self.assertEqual(hello.mul(0,2),0)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)
        self.assertEqual(hello.sqrt(36),6)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(2),0.9092974268256817)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(2),-0.4161468365471424)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertEqual(hello.tan(2),-2.185039863261519)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertEqual(hello.cot(2),-0.45765755436028577)
    def add(self):
        self.assertEqual(hello.self(0,2), 2)
        self.assertEqual(hello.add(3,4), 7)
        self.assertEqual(hello.add(4,5), 9)
    def sub(self):
        self.assertEqual(hello.sub(3,4), -1)
        self.assertEqual(hello.sub(4,3), 1)
        self.assertEqual(hello.sub(10,5), 5)
    def power(self):
        self.assertEqual(hello.power(2,3), 8)
        self.assertEqual(hello.power(3,2), 9) 
        self.assertEqual(hello.power(4,2), 16)   
    def log(self):
        self.assertEqual(hello.log(7), 0.845098040014)
        self.assertEqual(hello.log(0), 1)
        self.assertEqual(hello.log(100),2)

    def exp(self):
        self.assertEqual(hello.exp(2),1)
        self.assertEqual(hello.exp(3),1)
        self.assertEqual(hello.exp(4),1)
    

if __name__ == "__main__":
    unittest.main()
