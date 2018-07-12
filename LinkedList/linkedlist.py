def create_list(first, second=None):
    global index
    index = 0
    linkedlist = [first, second, index]
    return linkedlist


def clear(linkedlist):
    linkedlist[0] = linkedlist[1] = None
    linkedlist[2] = 0


def find(linkedlist, element):
    p = linkedlist
    while p[0] != element:
        p = p[1]
    return p


def insert_first(linkedlist, x):
    index = linkedlist[2]
    linkedlist = linkedlist[:2]
    linkedlist = [x, linkedlist, index]
    linkedlist[2] += 1
    return linkedlist


def insert_before(linkedlist, x, element):
    linkedlist[2] += 1
    p = linkedlist
    while p[1][0] != element:
        p = p[1]
    n = p[1]
    ar = [x, n]
    p[1] = ar


def insert_after(linkedlist, x, element):
    linkedlist[2] += 1
    p = linkedlist
    while p[0] != element:
        p = p[1]
    n = p[1]
    ar = [x, n]
    p[1] = ar


def append(linkedlist, x):
    p = linkedlist
    ind = linkedlist[2]
    while ind != 0:
        p = p[1]
        ind -= 1
    ar = [x, None]
    p[1] = ar
    linkedlist[2] += 1


def is_empty(linkedlist):
    try:
        return True if linkedlist[2] == 0 else False
    except IndexError:
        print('Received the wrong LinkedList')



def delete_by_id(linkedlist, element_id):
    assert is_empty(linkedlist) is False
    linkedlist[2] -= 1
    p = linkedlist
    while id(p[1]) != element_id:
        p = p[1]
    try:
        p[1] = p[1][1]
    except TypeError:
        print('This element does not exist!')
        return False
    return True


def delete_first(linkedlist):
    assert is_empty(linkedlist) is False
    linkedlist[2] -= 1
    index = linkedlist[2]
    linkedlist = linkedlist[:2]
    linkedlist = linkedlist[1]
    linkedlist.append(index)
    return linkedlist


def delete_after(linkedlist, element):
    assert is_empty(linkedlist) is False
    linkedlist[2] -= 1
    p = linkedlist
    while p[0] != element:
        p = p[1]
    try:
        p[1] = p[1][1]
    except TypeError:
        print('This element does not exist!')
        return False
    return True


def delete_before(linkedlist, element):
    assert is_empty(linkedlist) is False
    linkedlist[2] -= 1
    p = linkedlist
    while p[1][1][0] != element:
        p = p[1]
    try:
        p[1] = p[1][1]
    except TypeError:
        print('This element does not exist!')
        return False
    return True


def delete_last(linkedlist):
    assert is_empty(linkedlist) is False
    p = linkedlist
    ind = linkedlist[2]
    linkedlist[2] -= 1
    while ind != 0:
        p = p[1]
        ind -= 1
    p[1] = None


def print_list(linkedlist):
    p = linkedlist
    while p is not None:
        print(p[0])
        p = p[1]


def linkedlist_to_as(linkedlist, format=True):
    list = [] if format else ""
    p = linkedlist
    while p is not None:
        if format:
            list.append(p[0])
        else:
            list += str(p[0])
        p = p[1]
    return list


def list_len(linkedlist):
    return linkedlist[2]


linkedlist = create_list(2)
append(linkedlist, 5)
append(linkedlist, 5)
append(linkedlist, 5)
append(linkedlist, 5)
append(linkedlist, 9)
linkedlist = insert_first(linkedlist, 11)
linkedlist = delete_first(linkedlist)
print(linkedlist)
delete_last(linkedlist)
insert_after(linkedlist, 8, 2)
insert_after(linkedlist, 15, 5)
insert_before(linkedlist, 20, 15)
delete_before(linkedlist, 15)
delete_after(linkedlist, 8)
element_id = find(linkedlist, 15)
delete_by_id(linkedlist, id(element_id))
print(linkedlist_to_as(linkedlist))
print_list(linkedlist)
clear(linkedlist)
