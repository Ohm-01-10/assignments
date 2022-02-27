from itertools import permutations
oper=set ()
user_inp= "ludo"
letter = [x.lower() for x in user_inp]
for n in range (3, len (user_inp) + 1) :
    for y in list (permutations (letter, n)):
        z="".join(y)
        oper.add(z)
print (oper)