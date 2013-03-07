import unittest

from exersise import echo
from exersise.hoge import echo as echo2

class TestSequenceFunctions(unittest.TestCase):

    def test_exersise_hello(self):
        echo.echo("echo")
        self.assertEqual(echo.echo("hello"), "hello")

    def test_exersise_hoge_hello(self):
        echo.echo("echo")
        self.assertEqual(echo2.echo("hello"), "hello")

if __name__ == '__main__':
    unittest.main()


