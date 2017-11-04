import pygame
import sys
from Rhythm import Rhythm

class Rank:
    Rank_file = open('C:\Rank.txt', 'w')

    def __init__(self,):
        self.option = sys.argv[1]
        self.rank = []


    def writing(self, score):
        self.option == '-a'
        score = sys.argv[2]
        f = open('C:\Rank.txt', 'a')
        f.write(score)
        f.write('\n')
        f.close()

    def reading(self):
        f = open('C:\Rank.txt', 'v')
        self.rank = f.read()
        f.close()
        return self.rank
