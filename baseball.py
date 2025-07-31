from mimetypes import guess_type
from random import random


class BaseBall:
    def __init__(self):
        # Target Number is '159'
        ...

    def guess(self, guess_number):
        self._assert_invalid_input(guess_number)

        pass

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
