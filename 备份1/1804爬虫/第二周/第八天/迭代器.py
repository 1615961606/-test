from collections import Iterable
class Booklist(object):
    def __init__(self):
        self.data = []
        self.current = 0
    def add_books(self,item):
        self.data.append(item)

    def __iter__(self):
        return self
    def __next__(self):
        if len(self.data) > self.current:
            result = self.data[self.current]
            self.current +=1
            return result
        else:
            raise StopIteration

books = Booklist()
books.add_books('保护者')
books.add_books('小橘子')
for y in books:
    print(y)
print(isinstance(books,Iterable))