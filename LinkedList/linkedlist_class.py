class LinkedList:
    def __init__(self):
        self._begin = None
        self._index = 0

    def clear(self):
        self._begin[0] = self._begin[1] = None
        self._index = 0

    def find(self, element):
        p = self._begin
        while p[0] != element:
            p = p[1]
        return p

    def insert_first(self, x):
        self._begin = [x, self._begin]
        self._index += 1
        return self._begin

    def insert_before(self, x, element):
        p = self._begin
        self._index += 1
        while p[1][0] != element:
            p = p[1]
        n = p[1]
        ar = [x, n]
        p[1] = ar

    def insert_after(self, x, element):
        p = self._begin
        self._index += 1
        while p[0] != element:
            p = p[1]
        n = p[1]
        ar = [x, n]
        p[1] = ar

    def append(self, x):
        p = self._begin
        self._index += 1
        ind = self._index
        while ind != 0:
            p = p[1]
            ind -= 1
        ar = [x, None]
        p[1] = ar
        self._index += 1

    def is_empty(self):
        return True if self._index in [-1, 0] else False

    def delete_by_id(self, element_id):
        assert self.is_empty() is False
        self._index -= 1
        p = self._begin
        while id(p[1]) != element_id:
            p = p[1]
        try:
            p[1] = p[1][1]
        except TypeError:
            print('This element does not exist!')
            return False
        return True

    def delete_first(self):
        assert self.is_empty() is False
        self._index -= 1
        self._begin = self._begin[1]
        return self._begin

    def delete_after(self, element):
        assert self.is_empty() is False
        self._index -= 1
        p = self._begin
        while p[0] != element:
            p = p[1]
        try:
            p[1] = p[1][1]
        except TypeError:
            print('This element does not exist!')
            return False
        return True

    def delete_before(self, element):
        assert self.is_empty() is False
        self._index -= 1
        p = self._begin
        while p[1][1][0] != element:
            p = p[1]
        try:
            p[1] = p[1][1]
        except TypeError:
            print('This element does not exist!')
            return False
        return True

    def delete_last(self):
        assert self.is_empty() is False
        p = self._begin
        ind = self._index - 1
        self._index -= 1
        while ind != 0:
            p = p[1]
            ind -= 1
        p[1] = None

    def print_list(self):
        p = self._begin
        while p is not None:
            print(p[0])
            p = p[1]

    def linkedlist_to_as(self, format=True):
        list = [] if format else ""
        p = self._begin
        while p is not None:
            if format:
                list.append(p[0])
            else:
                list += str(p[0])
            p = p[1]
        return list

    def list_len(self):
        return self._index


linkedlist = LinkedList()
linkedlist.insert_first(5)
linkedlist.append(8)
linkedlist.delete_after(8)
linkedlist.print_list()
linkedlist.clear()
