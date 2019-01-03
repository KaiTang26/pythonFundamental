from math import factorial as fac

n = 5

k = 3

result = fac(n)//(fac(k)*fac(n-k))

print(result)

print(int("10000", 2))

a = None

print( a is None)

if True:
    print("this True")

h = 42

if h > 50:
    print("h is greater than 50")
else:
    print("h is less than 50")

c = 5

while c >0:
    print(c)
    c -= 1

 # while True:
 #    response = input()
 #    if int(response) % 7 == 0:
 #        print("good guess")
 #        break

# colection in python: str, bytes, list dict

aString = """ hadjfdkfs
dfkdfdfkdfjjf"""

bString = "kdfkdfjdkfdkfjdf \n dkfdfjdklfjd"

print(aString)

print(bString.capitalize())

print(aString.encode("utf-8"))

f = [1,2,3,]

print(f[1])


phoneList = {"kai": "6138764252", "lala": "84379385"}
print(phoneList["kai"])

