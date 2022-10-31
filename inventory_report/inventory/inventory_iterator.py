from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            valor = self.data[self.index]
            self.index += 1
            return valor
        except IndexError:
            raise StopIteration
