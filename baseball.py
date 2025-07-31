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

        pass