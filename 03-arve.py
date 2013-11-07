#!/usr/bin/python
# coding: latin-1
import os
clear = os.system('clear');
print '{:^80}'.format('Arve')
for x in xrange(1,3):
    print
    pass
rmb = '{:<30} {:<20} {:<20} {:>10}'
rmbf = '{:<30} {:<21} {:<21} {:>10}'
rmbs = '{:<29} {:<10}'
#rmbg = '{:<30} {:<20} {:<20} {:>10}'
rmbk = '{:<49}{:>19}{:>15}'
rmbks = '{:>50}{:>19}{:>15}'
#rmbksa = '{:>50}{:>15}'
rmbc = '{:<24}{:<15}'
print' ', rmb.format('Arve väljastaja', 'Arve saaja','Arve number:','0001')
print' ', rmbf.format('Madis Kõivupuu', 'Peeter Rätsep','Kuupäev:','10.02.2013')
print' ', rmbs.format('Oksa 1','Männi 2')
for x in xrange(1,3):
    print
    pass
print' ', rmb.format('Kaup','Hind','Kogus','Kokku')
print' ', rmb.format('Sokid','10','2','20')
print' ', rmb.format('Pastakas','1','1','1')
print' ', rmb.format('Halg','10','5','50')
print' ', rmb.format('Oks','1','2','2')
print
print' ', rmbk.format('','Vahesumma', '73')
print' ', rmbks.format('','Käibemaks 20%', '14,6')
print' ', rmbk.format('','Kokku', '87.6')
for x in xrange(1,2):
    print
    pass
print' ', rmbc.format('Kontaktid','Arveldus')
print' ', rmbc.format('Madis@gmail.com','Sprm Pank')
print' ', rmbc.format('tel: 56666666','IBN 52151515125122')
