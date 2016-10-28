#!/usr/bin/python
#Problem        : Matching Gloves
#Language       : Python
#by Joe Velardo

from __future__ import print_function
import sys

def is_palindrome(word):
    length = len(word)
    if length%2 == 0:
       split_len = length/2
       half1 = word[0:split_len]
       half2 = word[split_len:length]
    else:
       center = length/2
       half1 = word[0:center+1]
       half2 = word[center:length]
        
    half2 = half2[::-1]    

    if half1 == half2:
       return(1)
    else:
       return(0)

def get_num():
    num = raw_input()
    return(num)

num_clothes = int(get_num())
clothes_entries = []
i = 0
while i < num_clothes:
    clothes_entries.append(raw_input())
    i += 1

pairs = 0
non_pairs = 0
not_pals = []

for i in clothes_entries:
    if is_palindrome(i) == 0:
       not_pals.append(i)

if (len(not_pals) == 0) or ((len(not_pals)%2) != 0):
   pairs = -1
   print(pairs)
   sys.exit()
else:
   matches = []
   last = list(not_pals)
   while len(not_pals) > 0:
          first = last.pop(0)
          not_pals.remove(first)
          for i in not_pals:
              chk_cloth = str(i)
              if first == (chk_cloth[::-1]):
                 matches.append(str(first+chk_cloth))
                 break
pairs = len(matches)
print(str(pairs))
