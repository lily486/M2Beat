from operator import itemgetter
import locale
import functools


class Rank:
    locale.setlocale(locale.LC_ALL, '')

    def __init__(self,):
        self.rank = []

    def lensort(self, ):
        pass

    def writing(self, score):
        f = open('Rank.txt', 'a')
        f.write(score)
        f.write('\n')
        f.close()

    def reading(self):
        f = open('Rank.txt', 'r')
        self.rank = f.readlines()
        f.close()
        b = sorted(self.rank, key=lambda x: int(x.split(",")[0][1:]), reverse=True)
        a = "".join(b)
        f = open('Rank.txt', 'w')
        f.write(a)
        f.close()
