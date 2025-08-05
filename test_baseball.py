import pytest
from baseball import BaseBall, GameResult

#ssssss
@pytest.fixture
def baseball():
    return BaseBall()


def assert_illegal_argument(baseball, guess_number):
    with pytest.raises(TypeError):
        baseball.guess(guess_number)


def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls


@pytest.mark.parametrize("invalid_input", [None, '12', '1234', '12s', '112'])
def test_baseball_is_valid_input(baseball, invalid_input):
    assert_illegal_argument(baseball, invalid_input)


def test_baseball_if_matched_number(baseball):
    baseball.question = '123'
    assert_matched_number(baseball.guess('123'), solved=True, strikes=3, balls=0)


def test_baseball_if_unmatched_number(baseball):
    baseball.question = '123'
    assert_matched_number(baseball.guess('456'), solved=False, strikes=0, balls=0)

def test_baseball_if_strikes_number(baseball):
    baseball.question = '123'
    assert_matched_number(baseball.guess('126'), solved=False, strikes=2, balls=0)
    assert_matched_number(baseball.guess('163'), solved=False, strikes=2, balls=0)
    assert_matched_number(baseball.guess('823'), solved=False, strikes=2, balls=0)

def test_baseball_if_balls_number(baseball):
    baseball.question = '123'
    assert_matched_number(baseball.guess('321'), solved=False, strikes=1, balls=2)
    assert_matched_number(baseball.guess('132'), solved=False, strikes=1, balls=2)
    assert_matched_number(baseball.guess('213'), solved=False, strikes=1, balls=2)
    assert_matched_number(baseball.guess('572'), solved=False, strikes=0, balls=1)
