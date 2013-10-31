#!/usr/bin/python
# coding: latin-1
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
import os
import sys
clear = os.system('clear');
#clear()
# Funktsioon
def kysimus_tekst():
	print 'Mis su nimi on ?'
def kysimus():
	return raw_input('Kirjuta vastus siia: ')
def kysimus_funk_tekst():
	print 'Millist funktsiooni tahad kasutada?'
def kysimus_funk():
	return raw_input('center/count/decode/encode/format/index/find/strip ')
def pikkused_t2idised():
		pikkus = raw_input('Sisesta pikkus: ')
		if pikkus.isdigit() == True: 
			pikkus_jah = 1
		#else:
		#	print 'Sa võid sisestada ainult numbreid'
		#	return
		#t2idis = raw_input('Sisestage täidis: ')

def funktsioonid(nimi):
	if pikkus_jah == 1:
		if kys_funk == 'center':
			print nimi.center(pikkus,'=')

		#if kysimus_funk() == 'count'
		#	nimi.count()
	
def vastus(nimi):
	if nimi == 'Madis' and 'madis':
		print 'See nimi ei sobi.'
		return 
	elif nimi == '':
		print 'Ära jäta seda välja tühjaks.'
		return
	else: 
		kysimus_funk_tekst()
		kysimus_funk()
		pikkused_t2idised()
		kys_funk = kysimus_funk()
		funktsioonid(nimi)



#Kuvab
kysimus_tekst()
nimi = kysimus()
vastus(nimi) 
#While
while True:
	mine_tagasi = raw_input('Kas sa tahad tagasi minna? Y/N ')
	if mine_tagasi == 'Y':
		kysimus_tekst()
		nimi = kysimus()
		vastus(nimi)
		pass
	else:
		if mine_tagasi == 'n' and 'y':
			print 'Sa ei kirjutanud õiget valikut.'
		elif mine_tagasi == 'N':
			print 'Äitäh kasutamast minu koodi', nimi ,'.'
			sys.exit(1)


