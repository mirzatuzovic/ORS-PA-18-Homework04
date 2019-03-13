"""
===================   TASK 2   ====================
* Name: Even and Odd Numbers
*
* Write a script that will populate list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that user
* will always provide integer numbers. At the end,
* script should print how many even and odd numbers
* were present in list.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

broj_elemenata_niza = int(input("Unesite broj elemenata niza:"))

niz =[]
parni = 0
neparni = 0
for i in range(broj_elemenata_niza):

   element_niza = int(input("Unesite novi element:"))
   niz.append(element_niza)


for element_niza in niz:
    if(element_niza % 2) == 0:
        parni +=1
    else:
        neparni += 1

print(niz)
print("Parnih je:", parni)
print("Neparnih je:" , neparni)