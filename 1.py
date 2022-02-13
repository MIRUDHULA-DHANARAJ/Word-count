count=0
word_search=input("enter the world to be searched")
with open("text.txt",'r') as f:
  for i in f:
    word=i.split()
    for word_find in word:
      if word_find == word_search:
        count+=1
print(word_search,'found',count,'times from the file')