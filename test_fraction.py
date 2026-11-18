import pytest
from fraction import Fraction


def test_initialization():
    f = Fraction(1, 2)

    assert f.numerator == 1
    assert f.denominator == 2

    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_comparisons():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) < Fraction(3, 4)


def test_addition():
    assert Fraction(1, 2) + Fraction(1, 4) == Fraction(3, 4)