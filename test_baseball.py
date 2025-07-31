import pytest
from baseball import BaseBall


@pytest.fixture
def baseball():
    return BaseBall()


def assert_illegal_argument(baseball, guess_number):
    try:
        baseball.guess(guess_number)
        pytest.fail()
    except TypeError:
        pass


def test_baseball_is_valid_input(baseball):
    assert_illegal_argument(baseball, None)
    assert_illegal_argument(baseball, '12')
    assert_illegal_argument(baseball, '1234')


