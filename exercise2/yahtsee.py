from enum import Enum
import collections

class Category(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    PAIR = 7
    TWOPAIRS = 8
    THREEOFAKIND = 9

class Numbers(object):
    def __init__(self,num):
        self.num = num
    
    def score(self,values):
        sum = 0
        for v in values:
            if v==self.num:
                sum += self.num

        return sum


class Yahtsee(object):
    def score(self,category,values):
        def pair(values):
            values.sort(reverse=True)
            for v in zip(values[:-1],values[1:]):
                if v[0]==v[1]:
                    return 2*v[0]

            return 0

        def twopairs(values):
            frequencies = collections.Counter(values)
            result = 0
            pairs = 0
            for key in frequencies:
                if frequencies[key]>=2:
                    result += 2*key
                    pairs += 1
            return result if pairs==2 else 0

        def threeofakind(values):
            frequencies = collections.Counter(values)
            result = 0
            for key in frequencies:                
                if frequencies[key]>=3:
                    result += 3*key
            return result

        switcher={
            Category.ONES:Numbers(1).score,
            Category.TWOS:Numbers(2).score,
            Category.THREES:Numbers(3).score,
            Category.FOURS:Numbers(4).score,
            Category.FIVES:Numbers(5).score,
            Category.SIXES:Numbers(6).score,
            Category.PAIR:pair,
            Category.TWOPAIRS:twopairs,
            Category.THREEOFAKIND:threeofakind
        }
        func = switcher.get(category,lambda values:None)
        return func(values)