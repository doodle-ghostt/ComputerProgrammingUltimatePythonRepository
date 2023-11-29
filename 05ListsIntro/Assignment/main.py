def make_abc():
    return ["a", "b", "c"]

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
    if mid > first and last > mid:
        return True
    else:
        return False
print("INCREASING")
print(increasing([1, 2, 3]))
print(increasing([5, 5, 5]))
print(increasing([-1, 0, 1]))
print(increasing([3, 3, 3]))
print(increasing([4, 5, 6]))

def all_true(list):
    if list[0] == True and list[1] == True and list[2] == True:
        return True
    else:
        return False
print("ALL TRUE")
print(all_true([True, False, True]))
print(all_true([False, False, False]))
print(all_true([True, True, True]))
print(all_true([False, True, False]))
print(all_true([True, False, False]))

def mostly_true(list):
    if list[0] == True and list[1] == True:
        return True
    elif list[1] == True and list[2] == True:
        return True
    elif list[0] == True and list[2] == True:
        return True
    else:
        return False
print("MOSTLY TRUE")
print(mostly_true([True, False, True]))
print(mostly_true([False, False, False]))
print(mostly_true([True, True, True]))
print(mostly_true([False, False, True]))
print(mostly_true([True, False, False]))

def make_copy(items):
    copy = items
    return copy
print("MAKE COPY")
original_list = [3, 4, 5]
new_list = make_copy(original_list)
print("og: ", original_list, "new: ", new_list)

def repeat_thrice(number):
    list1 = [number, number, number]
    return list1
print("REPEAT THRICE")
print(repeat_thrice(-1))
print(repeat_thrice(5))

def make_reversed_copy(numbers):
    list1 = [numbers[2], numbers[1], numbers[0]]
    return list1
print("MAKE REVERSED COPY")
original_list = [1, 2, 3]
new_list = make_reversed_copy(original_list)
print("og: ", original_list, "new: ", new_list)

def reverse_in_place(numbers):
    one = numbers[2]
    two = numbers[1]
    three = numbers[0]
    numbers[0] = one
    numbers[1] = two
    numbers[2] = three
    return numbers
print("REVERSE IN PLACE")
original_list = [1, 2, 3]
new_list = reverse_in_place(original_list)
print("og: ", original_list, "new: ", new_list)