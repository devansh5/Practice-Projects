#Dictionaries using setdefault
import pprint

para=input("ENter the sentence in which you want to count the character")

count={}

for character in para:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)
print(pprint.pformat(count))
# importing the pprint module