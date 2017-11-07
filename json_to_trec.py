# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:47:48 2015

@author: ruhansa
"""
import json
# if you are using python 3, you should 
# import urllib.request 
import urllib2


# change the url according to your own koding username and query
inurl = 'http://artigupta7.koding.io:8983/solr/project2/select?q=%D0%91%D0%B8%D0%BB%D1%8C%D0%B4.+%D0%92%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%B9+%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82+%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%B8%D1%82%2C+%D1%87%D1%82%D0%BE+%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F+%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%82+1%2C5+%D0%BC%D0%BB%D0%BD+%D0%B1%D0%B5%D0%B6%D0%B5%D0%BD%D1%86%D0%B5%D0%B2+%D0%B2+%D1%8D%D1%82%D0%BE%D0%BC+%D0%B3%D0%BE%D0%B4%D1%83&rows=1000&fl=id%2C+score&wt=json&indent=true&defType=dismax&bq=(%D0%91%D0%B8%D0%BB%D1%8C%D0%B4.)%5E2.5+OR+(%D0%92%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%B9)%5E3.5+OR+(%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82)%5E3.5+OR+(%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%B8%D1%82%2C)%5E2.5+OR+(%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F)%5E5.5+OR+(%D0%B1%D0%B5%D0%B6%D0%B5%D0%BD%D1%86%D0%B5%D0%B2)%5E3.5+OR+(%D0%BC%D0%BB%D0%BD)%5E2.0+OR+(%D0%B3%D0%BE%D0%B4%D1%83)%5E2.0'
outfn = 'file.txt'


# change query id and IRModel name accordingly
qid = '010'
IRModel='Default'
outf = open(outfn, 'a+')
data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
# data = urllib.request.urlopen(inurl)

docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()