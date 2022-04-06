from collections import Counter
def check(s1, s2):
  d1 = Counter(s1)
  w = len(s1)
  print(d1)
  for i in range(len(s2)):
    if s2[i] in d1:
      d1[s2[i]] -= 1
    if i >= w and s2[i-w] in d1:
      d1[s2[i-w]] += 1
  print(d1)
check('ab', 'cbafagerf')
