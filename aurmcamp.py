import numpy as np
matrix = np.array([[1, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 1]])

a = 0
b = 0
checkpoint_list = []

def lookup(a, b):
  global checkpoint_list
  if [a, b] == [4, 4]:
    print(4, 4)
    print("Finished")
  else:
    lookup_return = []
    checklist = []
    matrix[a, b] = 0
    if 0 <= a <= 4 and 0 <= b-1 <= 4:
      if matrix[a, b-1] == 1: #왼쪽으로
        lookup_return.append([a, b-1])
    if 0 <= a+1 <= 4 and 0 <= b <= 4:
      if matrix[a+1, b] == 1: #아래로
        lookup_return.append([a+1, b])
    if 0 <= a-1 <= 4 and 0 <= b <= 4:
      if matrix[a-1, b] == 1: #위로
        lookup_return.append([a-1, b])
    if 0 <= a <= 4 and 0 <= b+1 <= 4:
      if matrix[a, b+1] == 1: #오른쪽으로
        lookup_return.append([a, b+1])

    print(a, b)
    #print(lookup_return)
  
    if len(lookup_return) == 2: #갈림길
      checkpoint_list = lookup_return
      lookup(lookup_return[0][0], lookup_return[0][1])
    if len(lookup_return) == 1: #정상
      lookup(lookup_return[0][0], lookup_return[0][1])
    if len(lookup_return) == 0: #막다른 길
      if len(checkpoint_list) == 2:
        lookup(checkpoint_list[1][0], checkpoint_list[1][1])
        checkpoint_list = []
  
lookup(0, 0)

