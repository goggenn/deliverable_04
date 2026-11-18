import pytest
from temperature import Temperature


def test_initialization():
    t = Temperature(20)
    assert t.unit == "C"
    assert Temperature(20, "f").unit == "F"

    with pytest.raises(AttributeError):
        t.value = 30


def test_validation():
    with pytest.raises(ValueError):
        Temperature(20, "X")
    with pytest.raises(ValueError):
        Temperature(-274, "C")
    with pytest.raises(ValueError):
        Temperature(-460, "F")
    with pytest.raises(ValueError):
        Temperature(-1, "K")


def test_conversions():
    assert Temperature(0, "C").to_fahrenheit() == pytest.approx(32)
    assert Temperature(32, "F").to_celsius() == pytest.approx(0)
    assert Temperature(0, "C").to_kelvin() == pytest.approx(273.15)
    assert Temperature(37, "C").to_fahrenheit() == pytest.approx(98.6)
    assert Temperature(100, "C").to_fahrenheit() == pytest.approx(212)


def test_round_trip():
    t = Temperature(25, "C")
    t = t.convert_to("F").convert_to("K").convert_to("C")

    assert t.value == pytest.approx(25)


def test_comparisons():
    t1 = Temperature(0, "C")
    t2 = Temperature(32, "F")
    t3 = Temperature(100, "C")

    assert "==" in t1.compare(t2)
    assert "!=" in t1.compare(t3)


def test_formatting():
    t = Temperature(25, "C")

    assert str(t) == "25.00 °C"
    assert repr(t) == "Temperature(25, 'C')"