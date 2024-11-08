#PROGRAM BALOK
#DIBUAT OLEH MOCH KEANU ALVINO

panjang = float(input('Input panjang balok: '))
lebar = float(input('Input lebar balok: '))
tinggi = float(input('Input tinggi balok: '))
 
luas = 2*(panjang*lebar) + 2*(panjang*tinggi) + 2*(lebar*tinggi)
 
print('Luas permukaan balok = ',round(luas,2))

