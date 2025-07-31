import pytest
from baseball import BaseBall, GameResult


@pytest.fixture
def baseball():
    return BaseBall()


def assert_illegal_argument(baseball, guess_number):
    with pytest.raises(TypeError):
        baseball.guess(guess_number)


@pytest.mark.parametrize("invalid_input", [None, '12', '1234', '12s', '112'])
def test_baseball_is_valid_input(baseball, invalid_input):
    assert_illegal_argument(baseball, invalid_input)


def test_baseball_if_matched_number(baseball):
    baseball.question = '123'
    result: GameResult = baseball.guess('123')
    assert result is not None
    assert result.solved == True
    assert result.strikes == 3
    assert result.balls == 0

def test_baseball_if_unmatched_number(baseball):
    baseball.question = '123'
    result: GameResult = baseball.guess('456')
    assert result is not None
    assert result.solved == False
    assert result.strikes == 0
    assert result.balls == 0
