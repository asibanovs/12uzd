sk = int(input("Ievadiet, lūdzu, tik lielo nozīmi, cik skaitļu vēlaties salīdzināt: "))
a = 1
pāra = 0
nepāra = 0
pozitīvs = 0
negatīvs = 0
divcipara = 0
triscipara = 0
b = int (input("Ierakstiet 1, ja vēlaties salīdzināt nepāra un pāra, ierakstiet 2, ja vēlaties salīdzināt pozitīvo un negatīvo, ierakstiet 3, ja vēlaties salīdzināt divcipara un trīscipara: "))
if b ==1:
  while a<=sk:
    sk1 = int(input("Ievadiet, lūdzu, skaitli: "))
    if sk1%2==0:
      pāra=pāra+1
    else:
      nepāra=nepāra+1
    a=a+1
  if pāra>nepāra:
    print("Pāra skaitļu ir vairāk")
  elif pāra==nepāra:
    print("Draw!")
  else:
    print("Nepāra skaitļu ir vairāk")
elif b ==2:
  while a<=sk:
    sk1 = int(input("Ievadiet, lūdzu, skaitli: "))
    if sk1>0:
      pozitīvs=pozitīvs+1
    else:
      negatīvs=negatīvs+1
    a=a+1
  if pozitīvs>negatīvs:
    print("Pozitīvo skaitļu ir vairāk")
  elif pozitīvs==negatīvs:
    print("Draw!")
  else:
    print("Negatīvo skaitļu ir vairāk")
else:
  while a<=sk:
    sk1 = int(input("Ievadiet, lūdzu, skaitli: "))
    if sk1>=10 and sk1<=99:
      divcipara=divcipara+1
    elif sk1>=100 and sk1<=999:
      triscipara=triscipara+1
    a=a+1
  if divcipara>triscipara:
    print("Divcipara skaitļu ir vairāk")
  elif divcipara==triscipara:
    print("Draw!")
  else:
    print("Triscipara skaitļu ir vairāk")