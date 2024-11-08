print("="*20)
print("Rumus kerucut")
print("="*20)

r = int(input("jari-jari\t: "))
s = int(input("garis pelukis\t: "))
t = int(input("tinggi\t: "))

lp = 3.14 * r * (r + s)
ls = 3.14 * r * s
v = 1/3 * 3.13 * r * r * t

print(f"luas permukaan\t: ",round(lp))
print(f"luas selimut\t: ",round(ls))
print(f"volume\t: ",round(v))