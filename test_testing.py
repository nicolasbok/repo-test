import unittest
import testing

class testtesting(unittest.TestCase):
    def test_celsius_to_fahr(self):
        self.assertEqual(testing.celsius_to_fahr(32), 89.6 )


if __name__ == '__main__':
    unittest.main()



assertEqual(a,b)
assertNotEqual(a,b)
assertTrue(x)
assertFalse(x)
assertIs(a,b)
assertIsNot(a,b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a,b)
assertNotIn(a,b)
assertIsInstance(a,b)
assertNotIsInstance(a,b)

numbers = [1,2,3,4]
#numbers.

#Classes
#We use classes to define new types.
class Point:
 def __init__(self, x, y):
    self.x = x
    self.y = y
 def move(self):
    print("move") 