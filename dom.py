import numpy as np
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("try.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
print('the number of terms: ',len(terms))
dic = {}
list = []
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    dic.update({ids.childNodes[0].data: 0})

for term in terms:
    ids = term.getElementsByTagName('id')[0]
    category: object = term.getElementsByTagName('is_a')
    for everyis_a in category:
        dic[everyis_a.childNodes[0].data]+=1
print(dic)
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    category = term.getElementsByTagName('is_a')
    for everyis_a in category:
        dic[everyis_a.childNodes[0].data] = dic[ids.childNodes[0].data]+dic[everyis_a.childNodes[0].data]
    list.append(dic[ids.childNodes[0].data])
print(dic)