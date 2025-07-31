import pytest
from baseball import BaseBall


@pytest.fixture
def baseball():
    return BaseBall()


def assert_illegal_argument(baseball, guess_number):
    with pytest.raises(TypeError):
        baseball.guess(guess_number)


@pytest.mark.parametrize("invalid_input", [None, '12', '1234', '12s', '112'])
def test_baseball_is_valid_input(baseball, invalid_input):
    assert_illegal_argument(baseball, invalid_input)


