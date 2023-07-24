class Counter:
    def __init__(self, *args):
        if len(args) == 1:
            self._current = 0
            self._stop = args[0]
            self._interval = 1
        elif len(args) == 2:
            self._current = args[0]
            self._stop = args[1]
            self._interval = 1
        elif len(args) == 3:
            self._current = args[0]
            self._stop = args[1]
            self._interval = args[2]
        else:
            raise NotImplementedError

    def __iter__(self):
        return self
    
    def __next__(self):
        ##3의 배수일땐 "짝"이 나오게
        if self._current < self._stop:
            r = self._current
            self._current += self._interval
            if r > 0 and r % 3 == 0:
                r = "짝"
            return r
        else:
            raise StopIteration
        

for i in Counter(20):
    print(i , end =' ')
