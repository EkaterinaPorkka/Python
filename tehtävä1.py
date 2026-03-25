from datetime import datetime
print("SYÖTÄ HENKILÖTIEDOT")
print("--------------------")
etunimi = input("Anna etunimet: ")
sukunimi = input("Anna sukunimi: ")
puhelin = input("Anna puhelinnumero: ")
email = input("Anna sähköpostiosoite: ")
syntymavuosi = input("Anna syntymävuosi: ")
print("\nKIITOS!\n")
nykyinen_vuosi = datetime.now().year
ika = nykyinen_vuosi - int(syntymavuosi)
print("HENKILÖN TIEDOT")
print("--------------------")

print("NIMI:")
print(f"  {sukunimi}, {etunimi}")

print("PUH:")
print(f"  {puhelin}")

print("E-MAIL:")
print(f"  {email}")

print(f"Ikä: {ika}")