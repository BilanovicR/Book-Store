# -*- coding: utf-8 -*-
from datetime import datetime
from fkorisnici import *
from meni_tekst import *

def ucitaj_knjige():  # funkcija za ucitavanje svih knjiga
	lista_knjiga = []
	knjige = open("knjige.txt")
	for line in knjige:
		knjiga_str = line.strip("\n")
		knjiga = eval(knjiga_str)
		lista_knjiga.append(knjiga)
	knjige.close()
	return lista_knjiga

global lista_knjiga
lista_knjiga = ucitaj_knjige()  # dobijam listu svih knjiga koju cu da koristim bez stalnog otvaranja fajla sa knjigama

def meni2():
	radim2 = True
	while radim2:
		print(glavni_meni2)
		izbor = input("Unesite broj funkcije:")
		if izbor == "1":
			print("Izabrali ste pretragu knjiga")
			pretraga_knjiga()
		elif izbor == "2":
			print("Izabrali ste prodaju knjiga")
			prodaja_knjiga()
		elif izbor == "3":
			print("Izabrali ste izlazak iz menija")
			print("******************************")
			break
		else:
			print("Uneli ste pogrešan broj, molimo ponovite unos.")


def meni1():  # sve funkcije u meniju menadžera su objašnjene ispod u ovom fajlu
	radim1 = True
	while radim1:
		print(glavni_meni1)
		izbor = input("Unesite broj funkcije:")
		if izbor == "1":
			print("Izabrali ste pretragu knjiga")
			print("****************************")
			pretraga_knjiga()
		elif izbor == "2":
			print("Izabrali ste unos nove knjige")
			print("*****************************")
			unos_knjige()
		elif izbor == "3":
			print("Izabrali ste brisanje knjige")
			print("****************************")
			brisanje_knjige()
		elif izbor == "4":
			print("Izabrali ste izmenu knjige")
			print("**************************")
			izmena_knjige()
		elif izbor == "5":
			print("Izabrali ste izlazak iz menija.")
			print("*******************************")
			break
		else:
			print("Uneli ste pogrešan broj, molimo ponovite unos.")
			print("**********************************************")

# funkcija za pretragu knjiga zajedno sa onom ispod
def un_pretraga(param):
	pronadjena = False
	upit = input("Pronađi ovo:")
	for knjiga in lista_knjiga:
		if knjiga["obrisano"] == False:
			if upit.lower() in knjiga[param].lower():
				pronadjena = True 
				print("Naziv: ", "{:<25}".format(knjiga["naziv"]), " Autor: ", "{:<20}".format(knjiga["autor"]),
				 " ISBN: ", "{:<10}".format(knjiga["isbn"]), " Žanr: ", "{:<10}".format(knjiga["zanr"]), 
				 " Količina: ", "{:<10}".format(knjiga["kolicina"]), " Cena: ", knjiga["cena"], " RSD")
	if not pronadjena:
		print("Ne postoji takva knjiga u bazi.")


def pretraga_knjiga():  # kraća ali neprecizna
	r = True
	global lista_knjiga	#ovako ce opet da mi ucita listu knjigu ako
	lista_knjiga = ucitaj_knjige() 	#je prethodno uneta neka promena
	print(pretraga_meni)
	while r:
		unos = input("Unesite parametar po kom želite da tražite knjigu: ")
		pronadjena = False
		if unos == "1":
			param = "naziv"
			un_pretraga(param) #funkcija objasnjena ispod
		elif unos == "2":
			param = "autor"
			un_pretraga(param)
		elif unos == "3":
			param = "isbn"
			un_pretraga(param)
		elif unos == "4":
			param = "zanr"
			un_pretraga(param)
		elif unos == "5":
			print("Izabrali ste izlaz iz menija.")
			r = False
		else:
			print("Pogrešan unos, ponovite")

def unos_knjige():  # funkcija za unos nove knjige, upisuje u formatu recnika( a cuva u obliku stringa) u fajlu
	global lista_knjiga	#ovako ce opet da mi ucita listu knjigu ako
	lista_knjiga = ucitaj_knjige() 	#je prethodno uneta neka promena
	naziv = unos_naziva()
	autor = unos_autora()
	zanr = unos_zanra()
	isbn = unos_isbn()
	cena = unos_cene()
	kolicina = unos_kolicine()
	f = open("knjige.txt", "a")
	knjiga = {"naziv": naziv, "autor": autor, "zanr": zanr, "isbn": isbn, "cena": cena, "kolicina": kolicina,
			  "obrisano": False}
	f.write(str(knjiga) + "\n")
	f.close()
	print("Uspešno ste uneli novu knjigu!")

def unos_naziva():  # unos naziva knjige
	x = True
	while x:
		unos = input("Unesite naziv knjige: ")
		if proveraTeksta(unos):  # objašnjeno ispod
			x = False
		else:
			print("Neprihvatljiv unos, pokušajte ponovo")
	return unos

def unos_autora():  # unos autora knjige
	y = True
	while y:
		unos = input("Unesite autora knjige: ")
		if proveraTeksta(unos):  # objašnjeno ispod
			y = False
		else:
			print("Neprihvatljiv unos, pokušajte ponovo")
	return unos

def proveraTeksta(unos):  # provera unosa teksta da nije prazan string i otklanjanje razmaka sa krajeva, za autora i naziv knjige
	if unos.strip(" ") == "":
		return False
	else:
		return True

def unos_zanra():  # unos zanra na osnovu ponuđene liste i provera da li je dobar unos
	print("1. klasik  2. krimi  3. autobiografija  4. sci-fi")
	while True:
		Zanr = input("Unesite index zanra: ")
		if Zanr == "1":
			zanr = "klasik"
			return zanr
		elif Zanr == "2":
			zanr = "krimi"
			return zanr
		elif Zanr == "3":
			zanr = "autobiografija"
			return zanr
		elif Zanr == "4":
			zanr = "sci-fi"
			return zanr
		else:
			print("Pogrešan unos, ponovite")

def provera_isbn(isbn):  # provera da li isbn postoji u bazi
	global lista_knjiga
	for knjiga in lista_knjiga:
		if isbn == knjiga["isbn"]:
			return False
	return True

def unos_isbn():  # unos isbn, provera formata i jedinstvenosti
	isbn = None
	while isbn is None:
		unos_isbn = input("Unesite ISBN: ")
		if unos_isbn.isdigit():
			if provera_isbn(unos_isbn):  # objašnjeno iznad
				isbn = unos_isbn
			else:
				print("Uneti ISBN već postoji. Pokušajte ponovo.")
		else:
			print("Pogrešan format ISBN-a, pokušajte ponovo")
	return isbn

def unos_cene():  # unos cene i provera vrednosti
	while True:
		cena = input("Unesite cenu: ")
		if cena.isdigit():
			if float(cena) >= 0:
				return float(cena)
		else:
			print("Pogrešna vrednost, unesite ponovo")

def unos_kolicine():  # unos količine i provera vrednosti
	k = True
	while k:
		kolicina = input("Unesite količinu: ")
		if kolicina.isdigit():
			if int(kolicina) >= 0:
				return int(kolicina)
		else:
			print("Pogrešna vrednost za unos količine, molimo ponovite")

# prilikom svake izmene atributa knjiga poziva se ova funkcija koja sačuva sve promene u postojećem fajlu
# i vraća listu knjiga koja je opet funkcija, i isparsira knjige i daje listu
def sacuvaj_knjige():
	f = open("knjige.txt", "w")
	for knjiga in lista_knjiga:
		f.write(str(knjiga) + "\n")
	f.close()
	print("Izmene knjiga su sačuvane!")
	return lista_knjiga

# funkcija za brisanje knjiga, trazi se unos ISBN-a i menja vrednost brisanja na True
def brisanje_knjige():
	global lista_knjiga	#ovako ce opet da mi ucita listu knjigu ako
	lista_knjiga = ucitaj_knjige() 	#je prethodno uneta neka promena
	pronadjena = False
	unos = input("Unesite ISBN knjige koju želite da izbrišete: ")
	for knjiga in lista_knjiga:
		if unos == knjiga["isbn"]:
			if knjiga["obrisano"] == False:
				knjiga["obrisano"] = True
				pronadjena = True
				print("Obrisali ste knjigu:")
				print("Naziv: ", knjiga["naziv"], " Autor: ", knjiga["autor"], " ISBN: ", knjiga["isbn"], " Žanr: ",
					  knjiga["zanr"], " Količina: ", knjiga["kolicina"], " Cena: ", knjiga["cena"], " RSD")
				sacuvaj_knjige()  # funkcija je objašnjena iznad
	if not pronadjena:
		print("Ne postoji knjiga sa tim ISBN-om ili je već obrisana")

def izmena_knjige():
	global lista_knjiga	#ovako ce opet da mi ucita listu knjigu ako
	lista_knjiga = ucitaj_knjige() 	#je prethodno uneta neka promena
	ova_knjiga = input("Unesite ISBN knjige koju želite da izmenite: ")
	pronasao = False
	for knjiga in lista_knjiga:
		if ova_knjiga == knjiga["isbn"]:
			pronasao = True
			print (knjiga)
			print (izmena_meni)
			par = input ("Unesite vrednost parametra koji želite da promenite ili izlazak iz menija: ")
			if par == "1":
				knjiga["naziv"] = unos_naziva() #na osnovu parametra menja se atribut knjige uz dodatnu proveru validnosti nove vrednosti, isto kao pri unosu nove knjige, ista funkcija
				sacuvaj_knjige() #po zavrsetku svake izmene se poziva funkcija za cuvanje podataka
			elif par == "2":
				knjiga["autor"] = unos_autora()
				sacuvaj_knjige()
			elif par == "3":
				knjiga["zanr"] = unos_zanra()
				sacuvaj_knjige()
			elif par == "4":
				knjiga["cena"] = unos_cene()
				sacuvaj_knjige()
			elif par == "5":
				knjiga["kolicina"] = unos_kolicine()
				sacuvaj_knjige()
			elif par == "6":
				print ("Izabrali ste izlazak iz menija")
				break
			else:
				print ("Pogrešan unos.")
				break  
	if not pronasao:
		print ("Ne postoji knjiga sa traženim ISBN-om.")


global racun
racun = ""
global suma
suma = float(0)
global konacanRacun
konacanRacun = ""

def dod_racun():
	global racun
	global suma
	print("Pregled knjiga:")
	print("{:<25}".format("Naziv"), "{:<20}".format("Autor"), "{:<10}".format("ISBN"), "Kolicina")
	for knjiga in lista_knjiga:
		print("{:<25}".format(knjiga["naziv"]), "{:<20}".format(knjiga["autor"]), "{:<10}".format(knjiga["isbn"])," ", knjiga["kolicina"])
	while True:
		nadjena = False
		unosIsbn = input("Unesite ISBN knjige koju želite da dodate na račun: ")
		unosKol = int(input("Unesite količinu:"))
		for knjiga in lista_knjiga:
			if knjiga["isbn"] == unosIsbn:
				nadjena = True
				kol = int(knjiga["kolicina"])
				c = float(knjiga["cena"])
				if unosKol <= kol:
					cena1 = c * unosKol
					suma += cena1
					racun1 = (" Kupljeno: " + knjiga["naziv"] + " Kolicina " + str(unosKol) + " Cena " + str(cena1) + "\n")
					racun += racun1 
					knjiga["kolicina"] = kol - unosKol
					sacuvaj_knjige()
					return racun, suma
				else:
					print("Uneli ste količinu veću od postojećeg stanja u magacinu. Pokušajte ponovo.")
		if not nadjena:
			print ("Pogresan unos ISBN-a, pokušajte ponovo")

def izd_racun():
	global racun
	global konacanRacun
	global suma
	if racun == "":
		print ("Ne možete izdati prazan račun, morate prvo dodati knjige na racun")
	else:
		print("Izdavanje sledećeg računa: ")
		konacanRacun = ( " *** Broj racuna:" + str(datetime.now()) + " Datum kupovine:" + str(datetime.now().strftime("%d-%m-%Y %H:%M")) + "\n" 
			+ racun + "\n" 
			+ "Ukupna cena: " + str(suma) + "\n"
			+ "Prodavac: " + korisnik["ime"] + " " + korisnik["prezime"] + " ***" + "\n")  
		print(konacanRacun)
		potvrda = input("Unesite 1 za izdavanje računa a 2 za izlazak iz menija: ")
		if potvrda == "1":
			rac = open("racuni.txt", "a")
			rac.write(str(konacanRacun))
			rac.close()
			print("Uspešno ste izdali račun")
			ponistiRacun()
		elif potvrda == "2":
			print("Izabrali ste izlazak iz menija.")
		else:
			print ("Pogresan unos, pokusajte ponovo.")

def ponistiRacun():
	global racun
	global suma
	global konacanRacun
	konacanRacun = ""
	suma = float(0)
	racun = ""
	return racun, suma, konacanRacun

def prodaja_knjiga():
	global lista_knjiga	#ovako ce opet da mi ucita listu knjigu ako
	lista_knjiga = ucitaj_knjige() 	#je prethodno uneta neka promena
	while True:
		print("Izaberite stavku")
		print("1. Dodaj na račun")
		print("2. Izdaj račun")
		print("3. Povratak na glavni meni i poništenje računa")
		print("***************************************")
		izbor = input("Unesite broj funkcije: ")
		if izbor == "1":
			print("Dodavanje na račun")
			dod_racun()
		elif izbor == "2":
			print("Izdavanje računa")
			izd_racun()
		elif izbor == "3":
			print("Poništavanje računa. Glavni meni")
			ponistiRacun()
			break
		else:
			print("Uneli ste pogrešan broj, ponovite unos.")

#pocetak aplikacije:
print("""---Knjizara---
Logovanje za zaposlene
""")
print("Unesite podatke da biste se ulogovali u sistem")

radim = True
# funkcija za pocetno logovanje u sistem,
# ponavlja se dok god se ne unesu ispravni podaci za kor.ime i sifru
while radim:
	pronadjena = False
	print ("***Za izlazak iz aplikacije unesite 'exit'***")
	x = input("Unesite korisničko ime: ")
	if x == "exit":
		print ("Izabrali ste izlazak iz aplikacije")
		radim = False
	else:
		y = input("Unesite sifru: ")
		for korisnik in lista_korisnika:
			if x == korisnik["korisnicko"] and y == korisnik["sifra"]:
				pronadjena = True
				print("Uspešno ste se prijavili kao " + korisnik["ime"] + " " + korisnik["prezime"])
				if korisnik["funkcija"] == "menadzer":
					meni1()
				elif korisnik["funkcija"] == "prodavac":
					meni2()
		if not pronadjena:
			print("Uneli ste pogrešne podatke, pokušajte ponovo")
