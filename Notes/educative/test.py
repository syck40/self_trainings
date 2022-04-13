def ms(li):
  if len(li) > 1:
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    ms(left)
    ms(right)
    print(li, left, right)
    i, j, k = 0, 0, 0
    
ms([54,26,93,17,77,31,44,55,20])
