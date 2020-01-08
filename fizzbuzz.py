"""
Regras do FizzBuzz:

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio nº
"""


def multiple_of_3(num):
	return num % 3 == 0


def multiple_of_5(num):
	return num % 5 == 0


def robot(num):
	say = str(num)

	if multiple_of_5(num) and multiple_of_3(num):
		say = 'fizzbuzz'

	elif multiple_of_5(num):
		say = 'buzz'
	
	elif multiple_of_3(num):
		say = 'fizz'

	return say

