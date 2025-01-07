from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import AlternatingGroup


print("Program start:")

G=AlternatingGroup(5)


bit0=Permutation(0,1,2,3,4)
bit1=Permutation(0,4,2,1,3)


print("AND gate verification:")

g0=Permutation(0,1,3,4,2)

g3=Permutation(0,1,3)

print("0,0 -> ")
print(int(g3 * bit0 * bit0 * bit0 * g0 * ~bit0 * ~bit0 * ~bit0 * ~g3 == bit1))
print("0,1 -> ")
print(int(g3 * bit1 * bit0 * bit1 * g0 * ~bit1 * ~bit0 * ~bit1 * ~g3 == bit1))
print("1,0 -> ")
print(int(g3 * bit0 * bit1 * bit0 * g0 * ~bit0 * ~bit1 * ~bit0 * ~g3 == bit1))
print("1,1 -> ")
print(int(g3 * bit1 * bit1 * bit1 * g0 * ~bit1 * ~bit1 * ~bit1 * ~g3 == bit0))

print("NOT gate verification:")

g1=Permutation(0,4)(1,2)

print("0 ->")
print(int(g1 * bit0 * (~g1) == bit1))

print("0 ->")
print(int(g1 * bit1 * (~g1) == bit0))

"""for g1 in G.generate():

    p0 =  g1 * bit0 * (~g1)
    p1 = g1 * bit1 * (~g1)

    if p0 == bit1 and p1 == bit0:
        print("Found it!")
        print("g1:")
        print(g1)"""




"""

for bit0 in [Permutation(0,1,2,3,4), Permutation(2,3,4), Permutation(1,2)(3,4)]:
    print("bit0: ")
    print(bit0)
    for bit1 in G.conjugacy_class(bit0):
        print("bit1: ")
        print(bit1)
        if bit0!=bit1:
            for g0 in G.generate():
                    for g1 in G.generate():
                        if g1 == Permutation(4):
                            for g2 in G.generate():
                                if g2 == Permutation(4):
                                    q00 = (bit0) * g2 * bit0 * g1 * bit0 * g0 * (~((bit0) * g2 * bit0 * g1 * bit0))
                                    q10 = (bit0) * g2 * bit1 * g1 * bit0 * g0 * (~((bit0) * g2 * bit1 * g1 * bit0))
                                    q01 = (bit1) * g2 * bit0 * g1 * bit1 * g0 * (~((bit1) * g2 * bit0 * g1 * bit1))
                                    q11 = (bit1) * g2 * bit1 * g1 * bit1 * g0 * (~((bit1) * g2 * bit1 * g1 * bit1))

                                    found=False
                                    
                                    if ((q00 == q01) and (q00 == q10) and (q00 != q11)):
                                        found=True      
                                    

                                    if found:
                                        for g3 in G.generate():
                                            p00 = g3 * q00 * (~g3)
                                            p11 = g3 * q11 * (~g3)

                                            foundit=False

                                            if ((p00 == bit0) or (p00 == bit1)) and ((p11 == bit0) or (p11 == bit1)):
                                                print("Found it perfect!")
                                                foundit=True
                                            

                                            if foundit:
                                                print("g0: ")
                                                print(g0)
                                                print("g1: ")
                                                print(g1)
                                                print("g2: ")
                                                print(g2)
                                                print("g3: ")
                                                print(g3)
                                                print("bit0: ")
                                                print(bit0)
                                                print("bit1: ")
                                                print(bit1)
                                                print("values of q:")
                                                print(q00)
                                                print(q01)
                                                print(q10)
                                                print(q11)

"""