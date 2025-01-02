# استدعي الحروف الابجديه 
import string
alphabet = string.ascii_lowercase

#الكلمه الاصليه
alphabet = string.ascii_lowercase
word=input("Type a letter :    ").lower()
#الكلمه المشفره 
guess =""
#امسك حرف في الكلمه الاصليه
for letter in word:
  #استخرج الاندكس بتاعه في الابجديه
      original_position = alphabet.index(letter)
      #اجعل الاندكس الجديد اعلى اعلى بدرجتين
      new_position = (original_position +2) % 26
      #الاندكس الجديد سيشير الى الحرف الجديد،
      #اضف الحرف الجديد الى متغير الشفره
      guess += alphabet[new_position]
      
print(guess)

