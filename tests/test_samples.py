from main import solve
from contextlib import redirect_stdout
import io

def utility(n):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        solve(n)
    return buffer.getvalue().strip()

def test_1():
    assert utility(1) == '#'

def test_2():
    assert utility(2) == '##\n##'

def test_9():
    ans = """#########
#.......#
#.#####.#
#.#...#.#
#.#.#.#.#
#.#...#.#
#.#####.#
#.......#
#########"""
    assert utility(9) == ans

def test_10():
    ans = """##########
#........#
#.######.#
#.#....#.#
#.#.##.#.#
#.#.##.#.#
#.#....#.#
#.######.#
#........#
##########"""
    assert utility(10) == ans
