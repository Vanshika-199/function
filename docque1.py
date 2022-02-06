def match_words(words):
  ctr = 0
  for word in words:
    if len(word)>1 and word[0]==word[-1]:
      ctr += 1
  return ctr
print(match_words(['abc', 'xyz', 'aba', '1221']))

#Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
# list=['abc', 'xyz', 'aba', '1221']
# result= 2.

