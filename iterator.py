class FlatIterator:
    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = 0  # курсор списка вложенного в основной список
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor == len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.nested_list_cursor]


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)