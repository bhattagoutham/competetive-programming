def LongestWord(sen):

  # code goes here
  max_len = 0; max_word = None
  words = sen.split()
  
  for word in words:
    word_len = 0
    if word.isalpha() and len(word) > max_len:
      max_len = len(word)
      max_word = word
    else:
      i = 0; n = len(word); wlen = 0
      while i < n:
        s_i = i
        while  i < n and word[i].isalpha():
          wlen += 1; i += 1
        if wlen > max_len:
            max_len = wlen; max_word = word[s_i:i]
        if i >= n:
          break
        while  i < n and not word[i].isalpha():
          i+=1
  return max_word

# keep this function call here 
print(LongestWord("fun&!!asdf time"))