import pygame
import sys
import locale
import functools


class Rank:


    def __init__(self,):
        self.rank = []

    def lensort(self, ):
        pass

    def writing(self, score):
        f = open('C:\Rank.txt', 'a')
        f.write(score)
        f.write('\n')
        f.close()

    def reading(self):
        f = open('C:\Rank.txt', 'r')
        self.rank = f.read()
        self.rank.split("\n")
        f.close()
        return self.rank
