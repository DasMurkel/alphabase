# Copyright (c) 2020 DasMurkel


"""
alphabase module to perform base conversions between the numeric alphabet ([0,9])
and an arbitrary alphabet to be selected by the user.
"""

class alphabase:
    """Converts an integer to a string using the provided alphabet."""

    def __init__(self, alphabet):
        self.__alphabet = alphabet
        self.alphabet_len = len(self.__alphabet)

    def to_alphabet(self, number):
        """Performs conversion from into to the provided alphabet."""
        if not isinstance(number, int):
            raise TypeError('number must be an integer')

        result = ''
        al_len = self.alphabet_len

        if 0 <= number < al_len:
            return self.__alphabet[number]

        while number != 0:
            number, i = divmod(number, al_len)
            result = self.__alphabet[i] + result

        return result

    def to_int(self, input):
        """Performs the conversion from the provided alphabet back to integer."""
        result = 0
        potence = 0

        while (len(input) > 0):
            result += self.decimal_value_of(input[-1]) * \
                pow(self.alphabet_len, potence)
            input = input[0:-1]
            potence += 1

        return result

    def decimal_value_of(self, char):
        """Find the decimal value of any character in the alphabet."""
        return self.__alphabet.find(char)

    def max_value(self, num_characters):
        """Returns the maximum value representable in the alphabet with a given number of characters."""
        return pow(self.alphabet_len, num_characters) - 1
