import hello
import unittest

class HelloTest(unittest.TestCase):

    def test_first_name(self):
        self.assertEqual("Hello, Konstantin!", hello.say("Konstantin"))

if __name__ == '__main__':
    unittest.main()
