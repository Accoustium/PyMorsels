class CyclicList:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __iter__(self):
        return self

    def __next__(self):
        self.my_list = [*self.my_list[1:], self.my_list[0]]
        return self.my_list[-1]

    def __getitem__(self, item):
        pass
