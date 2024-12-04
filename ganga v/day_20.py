'''
name:ganga
date:04-12-2024
version1.1
Build a program to simulate a coin flip (output: Heads or Tails).
'''
import random
def coin_flip():
    choice=random.choices(['Head','Tails'])
    return choice
print("Head or Tails:",coin_flip())