import os
clear = os.system('clear');
nimi = raw_input('Sisestage oma nimi: ')
perenimi = raw_input('Sisestage oma perenimi: ')
kumb = raw_input('Kas nimi v6i perenimi? ')
funktsioon = raw_input('Valige sobiv funktsioon: capitalize, swapcase, upper, lower, lstrip ')
if funktsioon == 'lstrip':
	lstrip_tahed = raw_input('Vali tahed: ')
if kumb == 'nimi':
	capitalize = nimi.capitalize()
	swapcase = nimi.swapcase()
	upper = nimi.upper()
	lower = nimi.lower()
	lstrip = nimi.lstrip(lstrip_tahed)
if kumb == 'perenimi':
	capitalize = perenimi.capitalize()
	swapcase = perenimi.swapcase()
	upper = perenimi.upper()
	lower = perenimi.lower()
	lstrip = perenimi.lstrip(lstrip_tahed)

if funktsioon == 'capitalize':
	print capitalize
if funktsioon == 'swapcase':
	print swapcase
if funktsioon == 'upper':
	print upper
if funktsioon == 'lower':
	print lower
if funktsioon == 'lstrip':
	print lstrip
