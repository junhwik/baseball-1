from random import random

class BaseBall:
    def __init__(self):
        # Target Number is '159'
        ...

    def guess(self, guess_number):
        if not guess_number:
            raise TypeError("입력값이 없습니다.")
        pass