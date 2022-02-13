class Data:
    ''' iterable container (reverse order) '''
    def __init__(self, data):
        self.data=data
        self.index=len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]

def Reverse(data):
    ''' function to iterate data in reverse order '''
    for i in data[::-1]:
        yield i

#Expression
even = (x for x in range(10) if x%2==0)
inc = ( i+1 for i in even)

odd = [o for o in inc]

for d in Data(odd):
    print(d)

    
