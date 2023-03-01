def what(letter):
  for i in wym.keys():
    if i == letter:
      return wym[letter]
  return -1

def boyer(text, klucz):
  dł = len(klucz)
  a = dł-1
  b = dł-1
  while a < len(text):
      while text[a] == klucz[b]:
          a-=1
          b-=1
      if b == -1:
          return a+1
      else:
          a += dł - min(b, 1+what(text[a]))
          b = dł-1
  return -1

text = "skacze sobie po podwórku"
klucz = "po"
wym = {letter:index for index, letter in enumerate(klucz)}
print(boyer(text, klucz))