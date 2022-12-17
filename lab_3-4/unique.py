import field
from gen_random import gen_random


class Unique(object):


    def __init__(self,items, ignore_case = False, **kwargs):
        self.items = items
        self.a=kwargs
        self.ignore_case = ignore_case
        self.uniq=set()
        
        self.index=0

    def __iter__(self):
        return self
    def __next__(self):
        if self.ignore_case == False :
            for i in self.items:
                if(i not in self.uniq):
                    self.uniq.add(i)
                    return i
            raise StopIteration
        else:
            for i in self.items:
                try:
                    
                    if(i.upper() not in self.uniq):
                        self.uniq.add(i.upper())
                        return i
                except AttributeError:
                    if (i not in self.uniq) :
                        self.uniq.add(i)
                        return i
            raise StopIteration
                        
                
 
if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    data = gen_random(10, 1, 3)
    print(list(Unique(data)))

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    print(list(Unique(data)))

    print(list(Unique(data, ignore_case=True)))
