def create_list(first, second=None):
    global index
    index = 0
    linkedlist = [first, second]
    return linkedlist


def insert_first(linkedlist, x):
    linkedlist = [x, linkedlist]
    return linkedlist


def insert_before(linkedlist, x, element):
    p = linkedlist
    while p[1][0] != element:
        p = p[1]
    n = p[1]
    ar = [x, n]
    p[1] = ar


def insert_after(linkedlist, x, element):
    p = linkedlist
    while p[0] != element:
        p = p[1]
    n = p[1]
    ar = [x, n]
    p[1] = ar


def append(linkedlist, x):
    p = linkedlist
    global index
    ind = index
    while ind != 0:
        p = p[1]
        ind -= 1
    ar = [x, None]
    p[1] = ar
    index += 1


def delete_first(linkedlist):
    linkedlist = linkedlist[1]
    return linkedlist


def delete_after(linkedlist, element):
    p = linkedlist
    while p[0] != element:
        p = p[1]
    p[1] = p[1][1]


def delete_before(linkedlist, element):
    p = linkedlist
    while p[1][1][0] != element:
        p = p[1]
    p[1] = p[1][1]


def delete_last(linkedlist):
    p = linkedlist
    ind = index-1
    while ind != 0:
        p = p[1]
        ind -= 1
    p[1] = None


def print_list(linkedlist):
    p = linkedlist
    while p is not None:
        print(p[0])
        p = p[1]


def list_len():
    return index


linkedlist = create_list(2)
append(linkedlist, 5)
append(linkedlist, 5)
append(linkedlist, 5)
append(linkedlist, 5)
append(linkedlist, 9)
linkedlist = insert_first(linkedlist, 11)
linkedlist = delete_first(linkedlist)
delete_last(linkedlist)
insert_after(linkedlist, 8, 2)
insert_after(linkedlist, 15, 5)
insert_before(linkedlist, 20, 15)
delete_before(linkedlist, 15)
print_list(linkedlist)
delete_after(linkedlist, 8)
print_list(linkedlist)
