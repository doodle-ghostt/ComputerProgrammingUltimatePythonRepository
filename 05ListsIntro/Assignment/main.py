def make_abc():
    return ["a, b, c"]

print("MAKE ABC")
print(make_abc())

def equal_edges(list1):
    first = list1[0]
    last = list1[-1]
    if first == last:
        return True
    else:
        return False
    
print("EQUAL EDGES")
print(equal_edges([1, 2, 3, 4, 1]))
print(equal_edges([5, 6, 7, 8, 9]))
print(equal_edges([-1, 0, 1, 2, -1]))
print(equal_edges([4, 4]))

def common_edge(lista, listb):
    firsta = lista[0]
    lasta = lista[-1]
    firstb = listb[0]
    lastb = listb[-1]
    if firsta == firstb or firsta == lastb:
        return True
    elif lasta == firstb or lasta == lastb:
        return True
    else:
        return False
    
print("COMMON EDGE")
print(common_edge([1, 2, 3, 4], [5, 6, 7, 8]))
print(common_edge([1, 2, 3], [3, 4, 5]))
print(common_edge([4, 5, 6], [7, 8, 9]))
print(common_edge([-1, 0, 1, 2, -1], [2, 3, 4, 5]))
print(common_edge([3, 3, 3], [3, 3, 3]))

def all_the_same(listI):
    total = int(listI[0]) + int(listI[1]) + int(listI[2])
    if int(total)/3 == int(listI[0]):
        return True
    else:
        return False
    
print("ALL THE SAME")
print(all_the_same([1, 2, 3]))
print(all_the_same([5, 5, 5]))
print(all_the_same([-1, 0, 1]))
print(all_the_same([3, 3, 3]))
print(all_the_same([4, 5, 6]))

def all_unique(integers):
    first = integers[0]
    mid = integers[1]
    last = integers[2]
    if first != mid and first != last and mid != last:
        return True
    else:
        return False
print("ALL UNIQUE")
print(all_unique([1, 2, 3]))
print(all_unique([5, 5, 5]))
print(all_unique([-1, 0, 1]))
print(all_unique([3, 3, 3]))
print(all_unique([4, 5, 6]))

def increasing(list):
    first = list[0]
    mid = list[1]
    last = list[2]
    if mid < first and last < mid:
        return True
    else:
        return False
print("INCREASING")
print(increasing([1, 2, 3]))