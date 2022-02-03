class FlatIterator:

    def __init__(self, start_list, end_list):

        self.start_list = start_list
        self.end_list = end_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        for el in range(len(self.start_list)):
          if self.cursor == len(self.start_list):
              raise StopIteration
          self.cursor += 1
          for item in range(len(self.start_list[el])):
              self.end_list.append(self.start_list[el][item])
        return self.end_list


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    end_list = []
    flat_list = [item for item in FlatIterator(nested_list, end_list)]
    print(flat_list[0])