class MyError(Exception):
    pass


class Parent:
    def __init__(self, value: int) -> None:
        self.i = value
        self.__executed = False
    
    def _calc(self, first_val: int, second_val: int) -> int:
        if not self.__executed:
            self.__executed = True
            return first_val * second_val * self.i
        raise MyError("Error text")


class Child(Parent):
    def __init__(self, value: int) -> None:
        super().__init__(value)
        self._isSecond = None
        
    def isFirst(self) -> int:
        return int(not self._isSecond)

    @property
    def isSecond(self) -> int:
        return int(self._isSecond)


class First(Child):
    def __init__(self, value: int) -> None:
        super().__init__(value)
        self._isSecond = 0


class A(First):
    def __init__(self, value: int = 3) -> None:
        super().__init__(value)
    
    def fnc(self, first_val: int) -> int:
        return self._calc(first_val, first_val)
