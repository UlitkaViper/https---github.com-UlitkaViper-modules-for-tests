from ma import Child


class Second(Child):
    def __init__(self, value: int) -> None:
        super().__init__(value)
        self._isSecond = 1


class B(Second):
    def fnc(self, first_val: int, second_val: int) -> int:
        return self._calc(first_val, second_val)
