def reversestring(comp_string):  
  words = comp_string.split(' ')  
  reversestring = ' '.join(reversed(words))  
  return reversestring  
  
if __name__ == "__main__":  
    string_1 = str(input())
    print (reversestring(string_1))
