
from .complex import __Complex
from math import sqrt

class CubicEquation:

    # constructor

    def __init__(self, coeff): 
        # assigning a copy of the cofficients to an attribute
        self.equation = coeff.copy()

        # reversing the list of coefficients, and assigning a copy of that list to an attribute variable
        coeff.reverse()
        self.coefficients = coeff.copy()

        # declaring and initializing dummy variables for future use
        self.__H, self.__G, self.__shift = -1, -1, -1
        self.answers = []

    def __depressedCubic(self):
        # determining the shift variable 
        shift = self.coefficients[2]/(3*self.coefficients[3])

        # determining H and G as per the coefficients of the polynomial
        H = (self.coefficients[1]-(self.coefficients[2]*self.coefficients[2])/(3*self.coefficients[3]))/3
        G = ((2*(self.coefficients[2] ** 3))/(27*(self.coefficients[3] ** 2))) - (self.coefficients[1]*self.coefficients[2])/(3*self.coefficients[3]) + self.coefficients[0]
        H /= self.coefficients[3]
        G /= self.coefficients[3]

        # assigning revised coefficients based on earlier results
        a_3 = 1
        a_2 = 0
        a_1 = (3*H)/self.coefficients[3]
        a_0 = G/self.coefficients[3]

        # assigning the results of the  
        self.coefficients, self.__H, self.__G, self.__shift = [[a_0, a_1, a_2, a_3].copy(), H, G, shift]

    @staticmethod
    def __quadratic(a, b, c):
        # determining the roots of a quadratic equation given the coefficients a, b, c

        return [(-1*b+(b*b-4*a*c).root())/(2*a), (-1*b-(b*b-4*a*c).root())/(2*a)]

    def __cardanoMethod(self):
        # finding u, v from Cardano's Method using a call to the static quadratic method
        u, v = CubicEquation.__quadratic(__Complex(1), __Complex(self.__G), __Complex(-(self.__H ** 3))) 

        # determining the first partial root
        first = u.root(3)

        # determining the second partial root
        second = __Complex(-self.__H)/u.root(3)

        # getting the values of the two constants omega and omegaSq
        omega, omegaSq = [round(i) for i in CubicEquation.quadratic(__Complex(1), __Complex(1), __Complex(1))]

        # determining the roots using the constants determined
        withoutShift = [first+second, omega*first+omegaSq*second, omegaSq*first+omega*second]
       
        # using list-comprehension to perform the necessary shift
        answers = [round(i-__Complex(self.__shift)) for i in withoutShift]

        return answers 

    def solve(self):
        # depressing the given cubic equation
        self.__depressedCubic()

        # using Cardano's method to get the roots of the cubic equation
        self.answers = self.__cardanoMethod()

        return self.answers.copy()

    def __repr__(self):
        info = ""

        # adding the coefficient of the x^3 term to the representation
        if (self.equation[0] != 1):
            info += str(self.equation[0])
        info += "x^3 + "

        # adding the coefficient of the x^2 term to the representation
        if (self.equation[1] != 1):
            info += str(self.equation[1])
        info += "x^2 + "

        # adding the coefficient of the x term to the representation
        if (self.equation[2] != 1):
            info += str(self.equation[2])

        # adding the coefficient of the constant term to the representation
        info += "x + " + str(self.equation[3])

        return info 
