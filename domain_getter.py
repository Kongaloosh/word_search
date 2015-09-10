import pickle
import random
import whois

__author__ = 'kongaloosh'

results = open('results','r')
domains = []

try:
    while True:
        domains.append(pickle.load(results))

except EOFError:
    print(len(domains))
    while True:
        pick = domains[random.randint(0, (len(domains))-1)]
        for (word,tld) in pick:
            try:
                domain = word[:len(word)-len(tld)] + '.' + tld
                if whois.whois(domain)["expiration_date"] == None:
                    print(domain)
                    exit(1)
            except UnboundLocalError:
                pass