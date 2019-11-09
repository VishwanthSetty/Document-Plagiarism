import re
def plagiarism(text1, text2):
    
    sentense1 = text1.split('.')
    sentense2 = text2.split('.')

    print(sentense1)
    print(sentense2)
    
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



if __name__ == "__main__":

    text1 = "a.b.c.d.e"
    text2 = "b.c.d.a.e"
    plagiarism(text1,text2)
    pass