#Dictionaries using setdefault

para=input("ENter the sentence in which you want to count the character")

count={}

for character in para:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)