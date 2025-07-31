import pytest
from baseball import BaseBall

@pytest.fixture
def baseball():
    return BaseBall()

def test_baseball_none_input(baseball):
    with pytest.raises(TypeError):
        baseball.guess(None)

def test_baseball_not_three_digit(baseball):
    with pytest.raises(TypeError):
        baseball.guess('12')