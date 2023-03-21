import pytest

from .text_to_number import UnrecognizedError, text_to_number


@pytest.mark.parametrize(
    "number, result",
    [
        pytest.param("one", 1, id="simple number"),
        pytest.param("eleven", 11, id="a simple two-digit number"),
        pytest.param("twenty five", 25, id="combined two-digit number"),
        pytest.param("one hundred", 100, id="simple big number"),
        pytest.param("hundred", 0, id="big number without pre-digit"),
        pytest.param(
            "two hundred thirty six", 236, id="combined big number & simple number"
        ),
        pytest.param("one hundred thousands", 100_000, id="combined two big numbers"),
        pytest.param(
            "two hundred eleven thousands",
            211_000,
            id="combined big number & simple big number",
        ),
        pytest.param(
            "three hundred fifteen thousands three hundreds ninety five",
            315_395,
            id="combined big number & simple big number & simple number",
        ),
        pytest.param(
            "one million two hundred eleven thousands three hundreds ninety five",
            1_211_395,
            id="million test",
        ),
        pytest.param(
            "one hundred million two hundred eleven thousands three hundreds ninety five",
            100_211_395,
            id="one hundred million test",
        ),
        pytest.param(
            "one hundred hundred", 100, id="combined two eq big numbers with pre-digit"
        ),
        pytest.param(
            "hundred hundred", 0, id="combined two eq big numbers without pre-digit"
        ),
        pytest.param("one one", 2, id="combined two eq numbers"),
    ],
)
def test_simple_numbers(number, result):
    assert text_to_number(number) == result


def test_mistake_value():
    with pytest.raises(UnrecognizedError):
        text_to_number("bilibirda")
