plainText=raw_input("Enter the Text to be Encoded : ")
def railcipher(plainText):
   plainText = plainText.lower()
   cipherText = ""
   rail1 = ""
   rail2 = ""
   rail3 = ""

   for i in range(len(plainText)):
      if i%3 == 0:
         rail1 += plainText[i]
      elif i%3 == 1:
         rail2 += plainText[i]
      else:
         rail3 += plainText[i]

   cipherText = rail1 + rail2 + rail3

   return cipherText
print "The Encoded Cipher is --> ",railcipher(plainText)
