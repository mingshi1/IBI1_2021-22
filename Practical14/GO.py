# find the parentNode of a term, once parentNode of the term occurs, times of the parentNode +1
# calculate the number of whole childnodes of the parent node
# draw boxplots and count the mean

####### Since using the dom to calculate, it will cost about 20 minutes to get results

from xml.dom.minidom import parse
import numpy as np
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
print('the number of terms: ',len(terms))
dic = {}
list1=[]
list=[]
dictionary={}
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    dic.update({ids.childNodes[0].data: 0}) # dic:{Go:0}
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    dictionary.update({ids.childNodes[0].data: []}) # dictionary:{Go:[]}
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    category = term.getElementsByTagName('is_a')
    for everyis_a in category:
        dic[everyis_a.childNodes[0].data]+=1 # find the first generation

for term in terms:
    ids = term.getElementsByTagName('id')[0]
    category = term.getElementsByTagName('is_a')
    if dic[ids.childNodes[0].data]==0:
        for everyis_a in category:
            dictionary[everyis_a.childNodes[0].data].append(ids.childNodes[0].data)

        for everyis_a in category:
            if not everyis_a.childNodes[0].data in list1:
                list1.append(everyis_a.childNodes[0].data)
def loop():
    global list1
    global dictionary
    list2=list1
    list1=[]
    for term in terms:
        ids = term.getElementsByTagName('id')[0]
        category = term.getElementsByTagName('is_a')
        if ids.childNodes[0].data in list2:
            for everyis_a in category:
                for element in dictionary[ids.childNodes[0].data]:
                    if not element in dictionary[everyis_a.childNodes[0].data]:
                        dictionary[everyis_a.childNodes[0].data].append(element)
                if not ids.childNodes[0].data in dictionary[everyis_a.childNodes[0].data]:
                        dictionary[everyis_a.childNodes[0].data].append(ids.childNodes[0].data)
            for everyis_a in category:
                if not everyis_a.childNodes[0].data in list1:
                    list1.append(everyis_a.childNodes[0].data)
    return list1
while list1 != []:
    loop()
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    dic[ids.childNodes[0].data]=len(dictionary[ids.childNodes[0].data])
    list.append(len(dictionary[ids.childNodes[0].data]))
list_translation=[]
for term in terms:
    ids = term.getElementsByTagName('id')[0]
    df=term.getElementsByTagName('def')[0]
    type=df.getElementsByTagName('defstr')[0]
    if 'translation' in type.childNodes[0].data:
        list_translation.append(dic[ids.childNodes[0].data])
    elif 'Translation' in type.childNodes[0].data:
        list_translation.append(dic[ids.childNodes[0].data])
print('translation: ',len(list_translation))

import matplotlib.pyplot as plt
plt.figure(figsize=(15,6))
plt.title('Distribution of the gene ontology',fontsize=20)
plt.ylabel('the number of childNodes')
plt.boxplot(list, vert=True, whis=1, patch_artist=True, meanline=True, showbox= True, showcaps=True, showfliers=True,notch=False)
plt.xticks([1],['overall gene ontology'],fontsize=10)
plt.show()
plt.figure(figsize=(15,6))
plt.title('Distribution of the translation related genes',fontsize=20)
plt.ylabel('the number of childNodes')
plt.boxplot(list_translation, vert=True, whis=1, patch_artist=True, meanline=False, showbox= True, showcaps=True, showfliers=True,notch=False)
plt.xticks([1],['translation related gene'],fontsize=10)
plt.show()
plt.xticks([1],['translation related genes'],fontsize=10)
print('whole genes mean: ',np.mean(list))
print('translation mean: ', np.mean(list_translation))
if np.mean(list_translation)>=np.mean(list):
    print('On average, translation related genes have more childNodes.')
else:
    print('On average, the overall genes ontology has more childNodes.')
