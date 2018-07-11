
def ucitaj_korisnike():
	lista_korisnika = []
	korisnici = open("korisnici.txt")
	for line in korisnici:
		korisnik = eval(line.strip("\n"))
		lista_korisnika.append(korisnik)
	korisnici.close()
	return lista_korisnika


lista_korisnika = ucitaj_korisnike()