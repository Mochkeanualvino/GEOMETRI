r = int(input("Masukan jari-jari alas tabung: "))
t = int(input("Masukan tinggi tabunng: "))
PHI = 3.14

volume = PHI * r**2 * t
keliling = 2 * PHI * r * (r + t)

print(f'volume: {volume}')
print(f'keliling: {keliling}')