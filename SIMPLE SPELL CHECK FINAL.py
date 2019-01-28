f=set(open("C:\\Users\\Lenovo\\Desktop\\Random.txt","r"))
for word in f:
    paragraph=set(word.replace("."," ").split())

di=set(open("C:\\Users\\Lenovo\\Desktop\\en-US.dic","r"))
dictionary=set(map(lambda s: s.strip(),di))

misspelt_words=set(paragraph)-set(dictionary)
print("The misspelt words in the paragraph are:")
print(misspelt_words)





