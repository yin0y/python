a = {}

a["이름"] = "김인영"
a["나이"] = "24살"
a["학번"] = "2018154029"
a["학과"] = "아동가족학과"
a["생일"] = "19991026"

print(a)
print(len(a))
print()

del a ["이름"]
del a ["나이"]
del a ["학번"]
del a ["학과"]
del a ["생일"]

print(a)
print(len(a))
print()

a = dict(이름 = "김인영", 나이 = "24살", 학번 ="2018154029", 학과 = "아동가족학과", 생일 ="19991026")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))
