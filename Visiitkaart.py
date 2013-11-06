#!/usr/bin/python
# coding: latin-1
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
#Code by Margus Henning
import os
import sys
clear = os.system('clear');
visiitkaart = raw_input('Sisestage endale sobiv visiitkaardi nimi: ')
tyhjus = ' '
kriips = '-'
nimi = raw_input('Sisestage oma ees-ja perekonnanimi: ')
ettevote = raw_input('Sisestage oma ettevõtte nimi: ')
amet = raw_input('Sisestage oma amet: ')

print '/', visiitkaart.center(60,'-'), '/'
print '|', tyhjus.center(60,' '), '|'
print '|', nimi.center(60,' '), '|'
print '|', ettevote.center(60,' '), '|'
print '|', amet.center(60,' '), '|'
print '|', tyhjus.center(60,' '), '|'
print '/', kriips.center(60,'-'), '/'
