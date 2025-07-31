from mimetypes import guess_type
from random import random

class BaseBall:
    def __init__(self):
        # Target Number is '159'
        ...

    def guess(self, guess_number):
        if not guess_number:
            raise TypeError("입력값이 없습니다.")
        if len(guess_number) !=3:
            raise TypeError("3자리 숫자 입력")

        for number in guess_number:
            if not ord('0')<=ord(number)<=ord('9'):
                raise TypeError("3자리 숫자 입력")

        if guess_number[0] == guess_number[1] or \
            guess_number[1] == guess_number[2] or \
            guess_number[2] == guess_number[0]:
            raise TypeError("중복 숫자 불가")

        pass