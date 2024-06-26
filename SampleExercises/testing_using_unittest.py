import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("--------------------Before class method-------------")

    @classmethod
    def tearDownClass(cls):
        print("--------------------TearDown After class execution-----------")

    def setUp(self):
        print("---------------------Setup before each method----------------")

    def tearDown(self):
        print("----------------------tearDown after each method---------------------------- ")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("First case executed")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("Second case executed")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print("Third case excecuted")

if __name__ == '__main__':
    unittest.main()