# 1. Write a Python program to count the number of occurrences of each word or
# character in the string entered by the user. (Count the Number of Occurrences
# of each character only if the single word is entered by the user).

user_string=input("Enter the string :")
lst1=[]
for i in user_string:
    lst1.append(i)
unique_ch=set((lst1))
if len(user_string.split()) == 1:
    for ele in unique_ch:
        print(f"Occurance of character {ele} is {user_string.count(ele)}")
else:
    search_for=input("Enter word/character to to count:")
    count=0
    if len(search_for)==1:
        character_search=search_for
        for i in user_string:
            if i == character_search:
                count += 1
        print(f"the count of {character_search} is {count}")
    elif len(search_for)>1:
        word_search=search_for
        lst=user_string.split()
        for j in lst:
            if j == word_search:
                count += 1
        print(f"the count of word {word_search} is {count}")

