number_names = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    1e2: "Hundred",
    1e3: "Thousand",
    1e6: "Million",
    1e9: "Billion",
    1e12: "Trillion",
    1e15: "Quadrillion",
    1e18: "Quintillion",
    1e21: "Sextillion",
    1e24: "Septillion",
    1e27: "Octillion",
    1e30: "Nonillion",
    1e33: "Decillion",
    1e36: "Undecillion",
    1e39: "Duodecillion",
    1e42: "Tredecillion",
    1e45: "Quattuordecillion",
    1e48: "Quindecillion",
    1e51: "Sexdecillion",
    1e54: "Septendecillion",
    1e57: "Octodecillion",
    1e60: "Novemdecillion",
    1e63: "Vigintillion",
    1e66: "Unvigintillion",
    1e69: "Duovigintillion",
    1e72: "Trevigintillion",
    1e75: "Quattuorvigintillion",
    1e78: "Quinvigintillion",
    1e81: "Sexvigintillion",
    1e84: "Septenvigintillion",
    1e87: "Octovigintillion",
    1e90: "Novemvigintillion",
    1e93: "Trigintillion",
    1e96: "Untrigintillion",
    1e99: "Duotrigintillion",
    1e100: "Googol",
    1e102: "Tretrigintillion",
    1e105: "Quattuortrigintillion",
    1e108: "Quintrigintillion",
    1e111: "Sextrigintillion",
    1e114: "Septentrigintillion",
    1e117: "Octotrigintillion",
    1e120: "Novemtrigintillion",
    1e303: "Centillion",
}

numbers = list(names.keys())

class Solution:
    def numberToWords(self, n: int):
        if n == 0:
            return names[n]

        return " ".join(self.int_to_words(n))

    def int_to_words(self, n: int, i: int = 1) -> list[int]:
        global names, numbers
        words = []
        while i < len(numbers):
            number = numbers[-i]
            word = names[number]
            d, n = divmod(n, number)
            if d > 1:
                words.extend(self.int_to_words(d, i + 1))
                words.append(word)
            if d == 1:
                if number >= 1e2:
                    words.append("One")
                words.append(word)

            i += 1

        return words
