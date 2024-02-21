import unittest

class MyTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual('FOO'.lower(), 'foo')

if __name__ == '__main__':
    unittest.main()
