from itertools import permutations
import enchant
d=enchant.Dict("en_US")
oper=set ()
user_inp= "friend"
letter = [x.lower() for x in user_inp]
for n in range(len(user_inp)):
    for y in list (permutations (letter, len(user_inp))):
        z="".join(y)
        if d.check(z):
            oper.add(z)
print (oper)