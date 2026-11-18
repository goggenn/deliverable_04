import math

class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) == int and type(denominator) == int:
            if denominator > 0:
                self.numerator = numerator 
                self.denominator = denominator
            else: 
                raise ValueError
        else:
            raise ValueError

    def __eq__(self, comparison: Fraction):
        if (self.numerator * comparison.denominator) == (self.denominator * comparison.numerator):
            return True
        else:
            return False

    def __ne__(self, comparison: Fraction):
        if (self.numerator * comparison.denominator) != (self.denominator * comparison.numerator):
            return True
        else:
            return False

    def __lt__(self, comparison: Fraction):
        if (self.numerator * comparison.denominator) < (self.denominator * comparison.numerator):
            return True
        else:
            return False

    def __le__(self, comparison: Fraction):
        if (self.numerator * comparison.denominator) <= (self.denominator * comparison.numerator):
            return True
        else:
            return False

    def __gt__(self, comparison: Fraction):
        if (self.numerator * comparison.denominator) > (self.denominator * comparison.numerator):
            return True
        else:
            return False

    def __ge__(self, comparison: Fraction):
        if (self.numerator * comparison.denominator) >= (self.denominator * comparison.numerator):
            return True
        else:
            return False

    def __add__(self, add: Fraction):
        new_numerator = (self.numerator * add.denominator) + (self.denominator * add.numerator)
        new_denominator = self.denominator * add.denominator
        gcd = math.gcd(new_numerator, new_denominator)
        return Fraction(numerator = (new_numerator/gcd), denominator = (new_denominator/gcd))

    def __sub__(self, sub: Fraction):
        new_numerator = (self.numerator * sub.denominator) - (self.denominator * sub.numerator)
        new_denominator = self.denominator * sub.denominator
        gcd = math.gcd(new_numerator, new_denominator)
        return Fraction(numerator = (new_numerator/gcd), denominator = (new_denominator/gcd))

    def __mul__(self, mul: Fraction):
        new_numerator = self.numerator * mul.numerator
        new_denominator = self.denominator * mul.denominator
        gcd = math.gcd(new_numerator, new_denominator)
        return Fraction(numerator = (new_numerator/gcd), denominator = (new_denominator/gcd))

    def __truediv__(self, div: Fraction):
        new_numerator = self.numerator * div.denominator
        new_denominator = self.denominator * div.numerator
        gcd = math.gcd(new_numerator, new_denominator)
        return Fraction(numerator = (new_numerator/gcd), denominator = (new_denominator/gcd))
        
