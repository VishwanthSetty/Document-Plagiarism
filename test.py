# from nltk.corpus import wordnet
names=["dig","ripped","feed","food"]
syn_names = []
# # for syns in names:
# #     syn_names.append(wordnet.synsets(syns))
# #     print(syn_names)
# # for name in syn_names:
# #     for name1 in name:
# #         print(name1.lemma_names())
# syn = wordnet.synsets(names)
# print(syn)
# for i in syn:
#     print(i.lemma_names())
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

from nltk.corpus import wordnet
for name in names:
    for syn in wordnet.synsets(name):
        for name in syn.lemma_names():
            syn_names.append(name)

    syn_names = Remove(syn_names)
    print(syn_names)
    print("\n\n")