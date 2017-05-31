#!/usr/bin/python
import re

regexp = [r'60-6\d{2,2}', r'\w+[@]\w+([._]?\w+)*[.][a-zA-Z]{2,3}']

re1 = r'60-6\d{2,2}'
re1strs = ['60-634' ,'03-60-667' ,'60-556' ,'60-6999']

re2 = r'\w+[@]\w+([._]?\w+)*[.][a-zA-Z]{2,3}'
re2strs = ['ab@cd.ef' ,'ab@cd.ef_gh.ij' ,'ab.cd.ef_gh.i' ,'12@34.56.gh_ij']

def regTest(reg, strs=[]):
    for s in strs:
        m = re.match(reg, s)
        if m :
            print("{0} match m.group()={1}, m.span()={2}".format(s, m.group(),m.span()))
        else :
            print("{0} doesn`t match".format(s))

def regsearchTest(reg, strs=[]):
    for s in strs:
        m = re.search(reg, s)
        if m :
            print("{0} search m.group()={1}, m.span()={2}".format(s, m.group(),m.span()))
        else :
            print("{0} doesn`t match".format(s))
        #use findall
        f = re.findall(reg, s)
        if f :
            print("{0} findall {1}".format(s, f))
        else :
            print("{0} doesn`t findall".format(s))

regTest(re1,re1strs)
regTest(re2,re2strs)
regsearchTest(re1,re1strs)
regsearchTest(re2,re2strs)
regTest(re2,re2strs)
