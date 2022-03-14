#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# avem cele 3 liste letters numbers si symbols cu toate elementele pe care le vom folosi in parola
print("Welcome to My Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) # scriem numarul de litere
nr_symbols = int(input(f"How many symbols would you like?\n"))# scriem numarul de simboluri
nr_numbers = int(input(f"How many numbers would you like?\n"))# scriem numarul de numere


eList = [] #avem o lista goala in
for i in range(0, nr_letters): #parcurgem forul pana la numarul de litere dat mai sus
    eList.append(random.choice(letters)) #adaugam elementele in lista si nu intr-un sir de caractere deoarece vrem ca la final sa le asezam random in sir
for i in range(0, nr_numbers):
    eList.append(random.choice(numbers))
for i in range(0, nr_symbols):
    eList.append(random.choice(symbols))

#in urma celor 3 for-uri avem o lista cu elemente random pe pozitii deja stabilite, ramanandu-ne sa facem schimbari de pozitii in lista
random.shuffle(eList)
#in lista se afla parola generata si ne ramane sa punem elementele intr-un string
finalPassword = ""
for i in range(0, len(eList)):
    finalPassword += eList[i]

print(finalPassword) # afisam parola





