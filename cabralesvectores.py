a = []

b = ['Instagram','X','Telegram','Epson','InDrive']

length = len(a)
print(length)

length = len(b)
print(length)

IN = True,False
print(b[0] + ',' + b[2]+ ','+b[4])

datos_personales = ['Jose Angel', '18', '1.78', 'Comprometido', 'La central']
datos_personales.append('Trigueño')
print(datos_personales)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
it_companies.insert(0,'Asus')
print(it_companies)

does_exist = 'kawai' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

it_companies.pop (2)
print(it_companies)

del it_companies[4]
print(it_companies)

it_companies.clear()
print (it_companies)
