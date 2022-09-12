from typing import Protocol


class Proto(Protocol):
    a: int = 2
    b: int = 3

    def parse(self) -> int:
        ...


class TestBase(Proto):
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b


class SubtractTestCase(TestBase):
    def parse(self) -> int:
        return self.subtract(self.a, self.b)


class AddTestCase(TestBase):
    def parse(self) -> int:
        return self.add(self.a, self.b)


class OneTestMixin(Proto):
    a = 3
    b = 3

    def test_parse(self):
        assert self.parse() in (0, 6)


class TestOneAdd(AddTestCase, OneTestMixin):
    ...

class TestOneSubstract(SubtractTestCase, OneTestMixin):
    ...