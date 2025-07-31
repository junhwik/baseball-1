import dataclasses
from mimetypes import guess_type
from random import random
from wsgiref.util import guess_scheme


class GameResult:
    def __init__(self, solved, strikes, balls):
        self._solved = solved
        self._strikes = strikes
        self._balls = balls

    @property
    def solved(self):
        return self._solved

    @property
    def strikes(self):
        return self._strikes

    @property
    def balls(self):
        return self._balls


class BaseBall:
    def __init__(self):
        self._question = ""
        # Target Number is '123'
        ...

    @property
    def question(self):
        raise AttributeError("읽을 수 없음")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult:
        self._assert_invalid_input(guess_number)

        if guess_number == self._question:
            return GameResult(True, 3, 0)

        strikes_count = self.count_strikes(guess_number)

        balls_count = self.count_balls(guess_number)

        return GameResult(False, strikes_count, balls_count)

    def count_balls(self, guess_number):
        balls_count = 0
        for i in range(3):
            for j in range(3):
                if i != j and guess_number[i] == self._question[j]:
                    balls_count += 1
        return balls_count

    def count_strikes(self, guess_number):
        strikes_count = 0
        for i in range(3):
            if guess_number[i] == self._question[i]:
                strikes_count += 1
        return strikes_count

    def _assert_invalid_input(self, guess_number: str):
        if not guess_number:
            raise TypeError("입력값이 없습니다.")

        if len(guess_number) != 3:
            raise TypeError("3자리 숫자 입력")

        if not guess_number.isdigit():
            raise TypeError("3자리 숫자 입력")

        if self._is_not_duplicated_number(guess_number):
            raise TypeError("중복 숫자 불가")

    def _is_not_duplicated_number(self, guess_number):
        return len(set(guess_number)) != 3
