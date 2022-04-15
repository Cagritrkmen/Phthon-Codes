
A = set([1, 2, 3, 4])
Set1 = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 4), (4, 1), (4, 4),(4,2),(3,1),(3,2)]
Set2 = [(1, 1),(2,2),(3,3),(1,3),(4,4)]

def is_reflexive(MySet, A):
    for a in A:
        if (a, a) not in MySet:
            return False
    return True


def is_antisymmetric(MySet,A):
    for (a, b) in MySet:
        if (a,b) in MySet and (b,a) in MySet and a != b:
            return False
    return True


def is_transitive(MySet, A):
    for a in A:
        for b in A:
            if (a, b) in MySet:
                for c in A:
                    if (b, c) in MySet and (a, c) not in MySet:
                        return False
    return True

    
for MySet in [Set1,Set2]:
    print("Checking for: ")
    print(MySet)
    print ("  reflexive: ", is_reflexive(MySet, A))
    print ("  antisymmetric: ", is_antisymmetric(MySet, A))
    print ("  transitive:", is_transitive(MySet, A))
    if is_antisymmetric(MySet,A) == True and is_reflexive(MySet,A) == True and is_transitive(MySet,A) == True:
        print("This set is poset so hasse diagram of this set can be drawn.")
    else: 
        print("This set is not poset so hasse diagram of this set can not be drawn.")
    print("\n")    


