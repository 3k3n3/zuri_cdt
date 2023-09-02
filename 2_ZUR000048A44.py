"""Cascading Palindrome."""


class Palindrome:
    """Implementing cascading palindrome."""

    def __init__(self, param):
        self.param = str(param)

    def check(self):
        """
        Checks for part of given parameter that is a palindrome.

        The parameter is converted to a list and using list comprehension
        each item is checked for equality with the reversed version.
        Only palndromes are in the original parameter is returned.
        """
        palindromes = f'{" ".join((i for i in self.param.split() if i == i[::-1]))}'
        if palindromes != "":
            return palindromes
        else:
            return "--- No Palindromes Found."

    def __str__(self):
        return self.check()


param1 = "Smert madam fight git 0124210 1230321 abcd5dcba 09234 example burueir float 09390 asdfgfdsa"
# outputs: madam 0124210 1230321 abcd5dcba 09390 asdfgfdsa

param2 = 1230321
# outputs: 1230321

param3 = "1230321 09234 0124210"
# outputs: 1230321 0124210

param4 = "abcd5dcba 1230321 09234 0124210"
# outputs: abcd5dcba 1230321 0124210

param5 = "99 N39g2PP2g93N 193 220 LGtEXjjXEtGL sL55Ls 142 168 9QddQ9 Z5yOD393xOOx393DOy5Z xBIrcZwp MnsgGdA"
# ouputs: 99 N39g2PP2g93N LGtEXjjXEtGL sL55Ls 9QddQ9 Z5yOD393xOOx393DOy5Z

param6 = "1717 nt6eqlU7x 501vb105 AAGh8G  889 579"
# outputs: --- No Palindromes Found.

param7 = "GrEFFErG cwOlRoBkF 357 678876 V0pRkvOR9zz9ROvkRp0V 734 GAVR8 GD04y 854 nEzJt55tJzEn 248 dzDVR"
# outputs: GrEFFErG 678876 V0pRkvOR9zz9ROvkRp0V nEzJt55tJzEn

param8 = "6aGYq8P UdWXqCggCqXWdU 93 zy5mhF31zccz13Fhm5yz 9viWr iByTwOC 3NQ8yDXLo99oLXDy8QN3 755 5r1pPaWB VjuFWJQgy B7997B 324 w6u45bDW"
# output: UdWXqCggCqXWdU zy5mhF31zccz13Fhm5yz 3NQ8yDXLo99oLXDy8QN3 B7997B

param9 = "3uNrKuTo7 h9dz 473 356 hScYSh jH45UHj 334 KwI 8LmTCLzvZ izGFXxih"
# outputs: --- No Palindromes Found.

param10 = "390 2gnD9nNqZZqNn9Dng2 lmO7Sb5QqqQ5bS7Oml 1fkR2pp2Rkf1 324 537735 3buDDub3"
# outputs: 2gnD9nNqZZqNn9Dng2 lmO7Sb5QqqQ5bS7Oml 1fkR2pp2Rkf1 537735 3buDDub3

p = Palindrome

print(p(param1))
print(p(param2))
print(p(param3))
print(p(param4))
print(p(param5))
print(p(param6))
print(p(param7))
print(p(param8))
print(p(param9))
print(p(param10))
