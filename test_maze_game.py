import os.path as p
from subprocess import run

from maze import is_valid_move


PROJECT_ROOT_DIR = p.dirname(p.dirname(p.realpath(__file__)))


def test_is_valid_move_edge():
    assert not is_valid_move(0, 0, 'up')


def test_flake8():
    process = run(['flake8'], cwd=PROJECT_ROOT_DIR)
    assert process.returncode == 0
