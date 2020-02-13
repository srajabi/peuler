import math
import cProfile
from decimal import Decimal, getcontext
from fractions import Fraction


class CFraction(list):
    """
   A continued fraction, represented as a list of integer terms.
   """

    def __init__(self, value, maxterms=15, cutoff=1e-10):
        if isinstance(value, (int, float, Decimal)):
            value = Decimal(value)
            remainder = int(value)
            self.append(remainder)

            while len(self) < maxterms:
                value -= remainder
                if value > cutoff:
                    value = Decimal(1) / value
                    remainder = int(value)
                    self.append(remainder)
                else:
                    break
        elif isinstance(value, (list, tuple)):
            self.extend(value)
        else:
            raise ValueError("CFraction requires number or list")

    def fraction(self, terms=None):
        "Convert to a Fraction."

        if terms is None or terms >= len(self):
            terms = len(self) - 1

        frac = Fraction(1, self[terms])
        for t in reversed(self[1:terms]):
            frac = 1 / (frac + t)

        frac += self[0]
        return frac

    def __float__(self):
        return float(self.fraction())

    def __str__(self):
        return "[%s]" % ", ".join([str(x) for x in self])


def pells_equation(x, y, n):
    return x * x - n * y * y == 1


getcontext().prec = 100
candidates = []
for d in range(1, 1001):
    for terms in range(2, 120):
        cf = CFraction(Decimal(d).sqrt(), maxterms=terms, cutoff=1e-10)
        frac = cf.fraction()
        if pells_equation(frac.numerator, frac.denominator, d):
            if terms > 60:
                print(d, cf, frac, terms)
            candidates.append((frac.numerator, d))
            break

candidates.sort(key=lambda c: c[0])
print(candidates)
