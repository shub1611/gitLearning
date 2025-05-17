from src.hello import say_hello
from unittest.mock import patch
from io import StringIO

def test_say_hello():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        say_hello()
        assert fake_out.getvalue().strip() == "Hello, World!"
