import pickle
import random
import whois
import urllib2
import re
from bs4 import BeautifulSoup

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
        while True:
            pick = domains[random.randint(0, (len(domains))-1)]
            print(pick[0])
            definition =  find(pick[0][0])
            if definition:
                results = []
                for (word,tld) in pick:
                    try:
                        domain = word[:len(word)-len(tld)] + '.' + tld
                        if whois.whois(domain)["expiration_date"]:
                            results.append({'domain':domain, 'definition':definition})
                    except (UnboundLocalError, KeyError):
                        pass
                    # except whois.parser.PywhoisError:           # this isn't 100% accurate
                    #     results.append({'domain':domain, 'definition':definition})
                return results[random.randint(0, (len(results))-1)]
def find(word):
    print(word)
    try:
        x=urllib2.urlopen("http://dictionary.reference.com/browse/"+word+"?s=t")
    except:
        return None

    x=x.read()
    soup = BeautifulSoup(x, 'html.parser')
    defs = soup.find_all('div', class_="def-content")
    defs = [d.text for d in defs]
    if defs: return defs

    items=re.findall('<meta name="description" content="'+".*$",x,re.MULTILINE)
    for x in items:
        y=x.replace('<meta name="description" content="','')
        z=y.replace(' See more."/>','')
        m=re.findall('at Dictionary.com, a free online dictionary with pronunciation,              synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith("Get your reference question answered by Ask.com"):
                return None
            else:
                return z
    else:
        return None

if __name__ == "__main__":
    find('dream')