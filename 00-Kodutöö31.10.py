import os
clear = os.system('clear');
nimi = raw_input('Sisestage oma nimi: ')
funktsioon = raw_input('Valige sobiv funktsioon: capitalize, swapcase, upper, lower, lstrip ')
capitalize = nimi.capitalize()
swapcase = nimi.swapcase()
upper = nimi.upper()
lower = nimi.lower()

if funktsioon == 'capitalize':
	print capitalize
if funktsioon == 'swapcase':
	print swapcase
if funktsioon == 'upper':
	print upper
if funktsioon == 'lower':
	print lower
if funktsioon == 'lstrip':
	lstrip_tahed = raw_input('Vali tahed: ')
	lstrip = nimi.lstrip(lstrip_tahed)
	print lstrip
