import pytest

from .text_to_number import UnrecognizedError, text_to_number


@pytest.mark.parametrize(
    "number, result",
    [
        ("one", 1),
        ("eleven", 11),
        ("twenty five", 25),
        ("one hundred", 100),
        ("two hundred thirty six", 236),
        ("one hundred thousands", 100_000),
        ("two hundred eleven thousands", 211_000),
        ("three hundred fifteen thousands three hundreds ninety five", 315_395),
        ("one million two hundred eleven thousands three hundreds ninety five", 1_211_395),
        ("one hundred million two hundred eleven thousands three hundreds ninety five", 100_211_395),
        ("one hundred hundred", 100),
        ("one one", 2)
    ]
)
def test_simple_numbers(number, result):
    assert text_to_number(number) == result


def test_mistake_value():
    with pytest.raises(UnrecognizedError):
        text_to_number("bilibirda")
