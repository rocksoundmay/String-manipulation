#!/usr/bin/env python
# coding: utf-8

# In[1]:


# problem 1
Name = input("Enter your name: ")
print(f"Hello, {Name}. Nice to meet you. ")
print("Hello, " + Name + ". Nice to meet you. ")


# In[2]:


# problem 2
Word = input("Enter a word: ")
reversed_word = Word[::-1]
print(f"reversed word: {reversed_word}. ")


# In[6]:


# problem 3
sentence = input("Enter a sentence: ")
char_count = len(sentence)
print(f"This sentence has {char_count} characters. ")


# In[9]:


# problem 4
string = input("Enter a word or a sentence: ")

string_lower = string.lower()

a_count = string_lower.count('a')
e_count = string_lower.count('e')
i_count = string_lower.count('i')
o_count = string_lower.count('o')
u_count = string_lower.count('u')

vowel_count = a_count + e_count + i_count + o_count + u_count
print(f"There are {vowel_count} vowels. ")


# In[10]:


# problem 5
word_to_check = input("Enter a word: ")
word_palindrome = word_to_check.upper()

if word_palindrome == word_palindrome[::-1]:
    print(f"This word is a palindrome.")
else:
    print(f"This word is not a palindrome.")


# In[11]:


# problem 6
secret_message = input("Enter your secret message: ")
encrypted = secret_message.upper().replace(" ","_")
print(f"Encrypted secret message: {encrypted}. ")


# In[ ]:




