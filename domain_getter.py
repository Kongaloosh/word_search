import pickle
import random
import whois
import urllib2
import re

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
                        definition =  find(word)
                        return {'domain':domain, 'definition':definition}
                except UnboundLocalError:
                    pass
                except whois.parser.PywhoisError:           # this isn't 100% accurate
                        definition =  find(word)
                        return {'domain':domain, 'definition':definition}

def find(word):
    x=urllib2.urlopen("http://dictionary.reference.com/browse/"+word+"?s=t")
    x=x.read()
    items=re.findall('<meta name="description" content="'+".*$",x,re.MULTILINE)
    for x in items:
        y=x.replace('<meta name="description" content="','')
        z=y.replace(' See more."/>','')
        m=re.findall('at Dictionary.com, a free online dictionary with pronunciation,              synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith("Get your reference question answered by Ask.com"):
                print "Word not found! :("
            else:
                return z
    else:
            print "Word not found! :("
