import pickle
import random

__author__ = 'kongaloosh'

results = open('results','r')
domains = []

try:
    while True:
        domains.append(pickle.load(results))
except EOFError:
    print(len(domains))
    pick = random.randint(0, (len(domains))-1)
    print(domains[pick])