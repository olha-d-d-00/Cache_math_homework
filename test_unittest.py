import unittest


class MyMathFloatException(ValueError):
    pass


class MyMath():
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        if type(a) == float or type(b) == float:
            raise MyMathFloatException("accepting only int numbers")

        result = 0
        new_a = a
        if a < 0:
            new_a = a * -1

        new_b = b
        if b < 0:
            new_b = b * -1

        for i in range(1, new_b + 1):
            result = result + new_a

        if (a > 0 and b > 0) or (a < 0 and b < 0):
            return result
        else:
            return result * -1

    def div(self, a, b):
        return a / b



class TestA1(unittest.TestCase):
    def test_positive(self):
        mymath = MyMath()
        expected_result = 3
        self.assertEqual(mymath.add(1, 2), expected_result)
        self.assertEqual(mymath.add(5, 1), 6)

    def test_negative(self):
        mymath = MyMath()
        self.assertEqual(mymath.add(-1, 1), 0)
        self.assertEqual(mymath.add(-1, -1), -2)
        self.assertEqual(mymath.add(1, 1, ), 2)

    def test_by_zero(self):
        mymath = MyMath()
        self.assertEqual(mymath.add(0, 0), 0)
        self.assertEqual(mymath.add(0, 1), 1)
        self.assertEqual(mymath.add(0, -1), -1)


class TestA2(unittest.TestCase):
    def test_1(self):
        mymath = MyMath()
        self.assertEqual(mymath.mul(2, 2), 4)
        self.assertEqual(mymath.mul(10, 2), 20)
        self.assertEqual(mymath.mul(10, -2), -20)
        self.assertEqual(mymath.mul(10, 0), 0)
        self.assertEqual(mymath.mul(10, 1), 10)
        self.assertEqual(mymath.mul(-10, -1), 10)
        self.assertEqual(mymath.mul(-1, 0), 0)
        self.assertEqual(mymath.mul(0, 0), 0)

        with self.assertRaises(MyMathFloatException) as cm:
            mymath.mul(0.25, 8)
        self.assertEqual(str(cm.exception), "accepting only int numbers")


        with self.assertRaises(MyMathFloatException) as cm:
            mymath.mul(-0.25, -8)
        self.assertEqual(str(cm.exception), "accepting only int numbers")


        with self.assertRaises(MyMathFloatException) as cm:
            mymath.mul(-0.1, -0.1)
        self.assertEqual(str(cm.exception), "accepting only int numbers")


class TestA3(unittest.TestCase):
    def test_1(self):
        mymath = MyMath()
        self.assertEqual(mymath.div(2, 2), 1)
        self.assertEqual(mymath.div(10, 2), 5)
        self.assertEqual(mymath.div(10, -2), -5)


        with self.assertRaises(ZeroDivisionError) as div:
            mymath.div(10, 0)
        self.assertEqual(str(div.exception), "division by zero")



        self.assertEqual(mymath.div(10, 2.5), 4)
        self.assertEqual(mymath.div(-10, -2), 5)
        self.assertEqual(mymath.div(1, 10), 0.1)