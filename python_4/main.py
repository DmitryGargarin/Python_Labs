import math


class Tribonacc:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.nums = [0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 3:
            res = self.nums[self.count]
        elif self.count < self.size:
            res = self.nums[self.count - 3] + self.nums[self.count - 2] + self.nums[self.count - 1]
            self.nums.append(res)
        else:
            raise StopIteration
        self.count += 1
        return res


class Leibniz:
    def __init__(self, final):
        self.final = final
        self.sum = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if round(self.sum, 2) != self.final:
            current = pow(-1, self.num) / (2 * self.num + 1)
            self.sum += current
            self.num += 1
            if self.num == 700:
                print("Infinite row")
                raise StopIteration
            return round(self.sum, 2)
        else:
            print("Count:", self.num)
            raise StopIteration


trib = Tribonacc(35)
for i in trib:
    print(i, sep='\t', end='\n')

leib = Leibniz(0.72)
for i in leib:
    print(i, sep='\t')
