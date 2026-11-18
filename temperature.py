class Temperature:
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

    def convert_to(self, target_unit: str) -> Temperature:
        if target_unit == "K":
            return Temperature(value = self.to_kelvin(), unit = target_unit)
        elif target_unit == "F":
            return Temperature(value = self.to_fahrenheit(), unit = target_unit)
        elif target_unit == "C":
            return Temperature(value = self.to_celsius(), unit = target_unit)
        else:
            return ValueError

    def __repr__(self) -> str:
        return f"Temperature({self._value}, {self._unit})"

    def __str__(self) -> str:
        if self._unit == "K":
            return f"{self._value:.2f} {self._unit}"
        else:
            return f"{self._value:.2f} °{self._unit}"

    def compare(self, temp: Temperature) -> str:
        if self._unit != temp._unit:
            temp.convert_to(self._unit)
        self_value = round(self._value, 9)
        temp_value = round(temp._value, 9)
        if self_value == temp_value:
            return f"{self.__repr__} == {temp.__repr__}"
        if self_value != temp_value:
            return f"{self.__repr__} != {temp.__repr__}"
        if self_value <= temp_value:
            return f"{self.__repr__} <= {temp.__repr__}"
        if self_value < temp_value:
            return f"{self.__repr__} < {temp.__repr__}"
        if self_value >= temp_value:
            return f"{self.__repr__} >= {temp.__repr__}"
        if self_value > temp_value:
            return f"{self.__repr__} > {temp.__repr__}"

    
        
        