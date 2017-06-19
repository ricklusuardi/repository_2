lista_libri = ['Eclisse','Alba Tragica' , 'Spartacus', '2001', 'Promessi Sposi' , 'Moby Dick', 'Memorie di Adriano', 'Lolita', 'il Conte di Montecristo', 'il Gattopardo', '1984', 'Cime Tempestose', 'il Processo', 'i Fratelli Karamazov']


output = ""
for libro in lista_libri:
	output += libro
	if (libro != lista_libri[-1]):
		output += ', '

print(output)
lista_libri.sort()
lista_ordinata =lista_libri

for libro in lista_ordinata:
	numero= lista_ordinata.index(libro) + 1
	print (numero, libro)

libri_prestabili=int(input('quanti libri vuoi prendere in prestito? ' ))
n_prestati=range(libri_prestabili)
libri_prestati = []
for i in n_prestati:
	numero_libro = 0
	while not(numero_libro>0 and numero_libro<14):
		numero_libro=int(input('inserisci il numero di uno dei libri che vuoi prendere'))
	index = numero_libro - 1
	libri_prestati.append(lista_ordinata[index])
	lista_ordinata.pop(index)
	print('il libro è stato prestato con successo')
	libri_disponibili = len(lista_ordinata)
	len_prestati = len(libri_prestati)
	
	print('libri disponibili:', libri_disponibili)
	print('libri prestati:' , len_prestati)

print('i libri disponibili sono:' )
for libro in lista_ordinata:
	numero= lista_ordinata.index(libro) + 1
	print (numero, libro)
print('i libri prestati sono:')
for a in libri_prestati:
	numero= libri_prestati.index(a) + 1
	print (numero, a)