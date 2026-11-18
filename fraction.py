class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) and type(denominator) == int:
            if denominator > 0:
                self.numerator = numerator 
                self.denominator = denominator
            else: 
                raise ValueError
        else:
            raise ValueError
    