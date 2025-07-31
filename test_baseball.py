import pytest
from baseball import BaseBall

def baseball():
    return BaseBall()

def test_baseball_none_input(baseball):
    with pytest.raises(TypeError):
        baseball.guess(None)