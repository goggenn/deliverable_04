class temperature:
    tolerance = 1e-9

    def __init__(self, value, unit):
        self._value = value
        self._unit = unit

    def to_celsius(self) -> float:
        if self._unit == "K":
           return self._value - 273.15
        else:
            return (self._value - 32) * (5/9)

    def to_fahrenheit(self) -> float:
        if self._unit == "K":
           return (self._value - 273.15) * (9/5) + 32
        else:
            return self._value * (9/5) + 32

    def to_kelvin(self) -> float:
        if self._unit == "C":
            return self._value +273.15
        else:
            return (self._value - 32) * (5/9) + 273.15

    
        