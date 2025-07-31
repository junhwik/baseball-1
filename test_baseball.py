import pytest
from baseball import BaseBall


def test_baseball_none_input():
    bb = BaseBall()
    with pytest.raises(TypeError):
        bb.guess(None)