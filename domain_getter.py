import pickle
import random
import whois

__author__ = 'kongaloosh'

def random_domain():
    pass


def domainify():
    """Returns a random domain where the last characters form a TLD"""
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
                        return(domain)
                except UnboundLocalError:
                    pass