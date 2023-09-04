from main import solve
from contextlib import redirect_stdout
import io


def test_1():
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        solve(1)
    out = buffer.getvalue().strip()
    assert out == '#'

def test_2():
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        solve(2)
    out = buffer.getvalue().strip()
    assert out == '##\n##'
