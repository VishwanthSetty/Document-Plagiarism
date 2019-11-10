with open("100 comman words.txt",'r',encoding = 'utf-8') as file:
    file2 = open("listWords.txt", 'w', encoding= 'utf-8')
    lists= file.read()
    # print(lists)
    lists = lists.split("\n")
    for i in lists:
        if('(' in i):
            index = str.find(i,'(')
            i = i[0:index-1]
            file2.write(i+'\n')
        else:
            file2.write(i+'\n')
            continue
    file2.close()
    pass