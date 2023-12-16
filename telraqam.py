telekomlar = {
  "90":"Beeline",
  "91":"Beeline",
  "33":"Humans", 
  "99":"Uzmobile",
  "95":"Uzmobile",
  "93":"Ucell",
  "94":"Ucell",
  "50":"Ucell"
}

while True:
  raqam = input("Tel raqami: ")
  kod = raqam[:2]

  if kod in telekomlar:
    print(f"{telekomlar[kod]}: +998 ({kod}) {raqam[2:]}")
  else:
    print("Kod noto'g'ri")