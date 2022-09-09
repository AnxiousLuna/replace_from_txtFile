import sys
import numpy as np
from pathlib import Path

#file = Path('txt-kopi.txt')
#file.write_text(file.read_text().replace('-e', ''))

A=np.loadtxt("AAA.txt",dtype="str")
AA=list(A)
print(len(AA))

B=np.loadtxt("BBB.txt",dtype="str")
BB=list(B)
print(len(BB))


print("start")
value = len(AA)
counter=1

for i in BB:
    if i in AA:
        BB.remove(i)
        counter += 1
        procent = counter/value*100
        print("C : "+str(counter)+" --- "+str(procent)+"%" )
        
print(str(BB))

with open("Result.txt", "a") as file_object:
    file_object.write(str(BB))

print("End")
