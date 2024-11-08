print("="*20)
print("Rumus limas segitiga")
print("="*20)

a = int(input("alas\t: "))
ts = int(input("tinggi segitiga\t: "))
tl = int(input("tinggi limas\t: "))
s1 = int(input("sisi1\t: "))
s2 = int(input("sisi2\t: "))
s3 = int(input("sisi3\t: "))

t = int(input("tinggi\t: "))
l = 1/2 * a * (s1 + s2 + s3) + 1/2 * a
v = 1/3 * a * t

la = 1/2 * a * ts
ls1 = 1/2 * a * s1
ls2 = 1/2 * a * s2
ls3 = 1/2 * a * s3

print(f"luas permukaan\t: ",round(l))
print(f"volume\t: ",round(v))
lp = la + ls1 + ls2 + ls3
v = 1/3 * la * tl

print(f"luas permukaan\t: ",round(lp))
print(f"volume\t: ",round(v,2))