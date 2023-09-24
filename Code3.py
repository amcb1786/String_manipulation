#!/usr/bin/env python
# coding: utf-8

# In[14]:


# greeting message
greeting = input("Enter your full name: ") 
print("Hello"+ " " + greeting + "!" + " " + "Nice to meet you.")


# In[ ]:


#reversed string
s1 = input("Enter a word of your choice: ")
lengthofs1 = len(s1)
reverses1 = s1[lengthofs1::-1]
print(reverses1)


# In[ ]:


#string length 
sentence = input("Enter a sentence: ")
length = len(sentence)
print("The sentence has" , length , "characters.")


# In[ ]:


# vowel count 
sentence_word = input("Enter a sentence or a word: ")
count = 0
i = 0 
for i in range(len(sentence_word)):
    if( 
        (sentence_word[i] == "a")
            or (sentence_word[i] == "e")
            or (sentence_word[i] == "i")
            or (sentence_word[i] == "o")
            or (sentence_word[i] == "u")
    ): 
            count += 1
print("Number of vowels in the given sentence or word is:", count)


# In[15]:


# palindrome check 
word = input("Enter a word of your choice: ")
if word == word[::-1]:
        print("It is a palindrome")
else:
        print("It is not a palindrome")


# In[13]:


# secret message
secret_message = input("Enter a secret message as a sentence: ")
uppencrypted_message = secret_message.upper() 
repencrypted_message = uppencrypted_message.replace(" ","_")
print(repencrypted_message)


# In[ ]:




