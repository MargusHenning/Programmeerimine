#!/usr/bin/python
# coding: latin-1
# -*- coding: iso-8859-15 -*-
#Code by Margus Henning
# -*- coding: ascii -*-
import os
clear = os.system('clear');
#Mis on mis.
pealkiri = raw_input('Sisestage pealkiri: ')
if pealkiri.isalpha() == False:
	print 'Sisesta ainult tähed.'
else:
	pealkiri = pealkiri.center(35,' ')
tekst = raw_input('Sisestage tekst: ')
tekst = tekst.center(25,'=')
ylemine = raw_input('Sisestage siia oma Header: ')
ylemine = ylemine.center(60,'-')
alumine = raw_input('Sisestage siia oma Footer: ')
alumine = alumine.center(60,'-')
print ylemine
print pealkiri
print tekst
print alumine
