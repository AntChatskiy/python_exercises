"""
*https://acmp.ru/index.asp?main=solution&id_task=2
In INPUT.TXT I've a number, that mean how many progression members do I 've. 
In OUTPUT.TXT I should write number, which's the sum of all members of the progression.
As example:
INPUT.TXT
26
---
-5
OUTPUT.TXT
352
---
-15
P.S. go hell with it acmp.ru, i do not understand that's happening:
"Presentation error"
"""
f = open("INPUT.TXT", "r")
N = f.readline()
f.close()
if N.isdigit():
    N = int(N)
    if N < 10**4:

        a = 0
        if N < 0:
            N = N*-1
            a = 1

        S = 0
        for i in range(1, N+1):
            S = S+i
        if a == 1:
            S = S*-1

        f = open("OUTPUT.TXT", "w")
        f.write(str(S))
        print(S)
        f.close()
