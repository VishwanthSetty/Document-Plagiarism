import re
from nltk.corpus import wordnet


with open("listWords.txt", 'r', encoding='utf-8') as file:
    commanwords = file.read()
    commanwords = commanwords.split()

def synonyms(words):
    pass

def plagiarism(text1, text2):
    
    sentense1 = text1.split('.')
    sentense2 = text2.split('.')

    print(text1)
    print(text2)
    
    VP_percentage = verbatimPlagiarism(sentense1,sentense2)

    print(VP_percentage)

    return 
    pass

def verbatimPlagiarism(sentense1, sentense2):
    Ouccred = 0
    i,j=0,0
    
    while(i<len(sentense1)):
        counter = 0
        while(True):
            counter+=1
            if(counter > len(sentense2)):
                break
           
            if(sentense1[i] == sentense2[j%(len(sentense2))-1]):
                Ouccred+=1
                # i+=1
                j+=1
                break
            else:
                j+=1
                continue
        i+=1
        
        
    return Ouccred/len(sentense2)
    pass

def paraphrasingPlagiarism(sentenses1, sentenses2):

    Ouccred = 0
    i,j=0,0
    
    while(i<len(sentenses1)):
        counter = 0
        while(True):
            counter+=1
            if(counter > len(sentenses2)):
                break
           
            if(compare(sentenses1[i],sentenses2[j%(len(sentenses2))-1])):
                Ouccred+=1
                # i+=1
                j+=1
                break
            else:
                j+=1
                continue
        i+=1
        
        
    return Ouccred/len(sentenses2)
    pass

def compare(sentense1,sentense2):
    sentense1 = sentense1.split()
    sentense2 = sentense2.split()
    for i in range(len(sentense1)):
        if sentense1[i] in commanwords:
            sentense1[i].pop(i)
        else:
            continue
    for i in range(len(sentense2)):
        if sentense2[i] in commanwords:
            sentense2[i].pop(i)
        else:
            continue
    
    sentense2[1]
    


    pass



if __name__ == "__main__":


    
    
    text1 = "a.b.c.d.e"
    text2 = "b.c.d.a"
    plagiarism(text1,text2)
    pass