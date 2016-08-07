# bbcc_MatchingGloves
programming exercise

Introduction
Winter is coming and Manny needs to sort through his winter wear to make sure that all his gloves are in
pairs. Luckily he has labeled each of his gloves with a string, and has a system in place where each glove
is labeled with the reverse of the string that its matching pair is labeled with. Manny never
labels his gloves with a palindrome (a string that is the reverse of itself) because that is how he
labels his hats. Can you help Manny work out whether all his gloves have a matching pair?

Input Specifications
Your program will take
An input N (1 ≤ N ≤ 100,000) which denotes the number of gloves and hats Manny has in his
shopping bags.

This will be followed by N strings S[1], S[2], ..., S[N] where S[i] denotes the string that each
winter wear item is labeled with. Each string will only be comprised of lowercase letters a-z, and
there can be duplicates of a string.

Output Specifications
If all Manny's gloves have a pair, print the number of matching pairs of gloves that he has. Otherwise,
print -1.

Note that:
Palindromes do not denote a glove and should be ignored.
Multiple sets of the same pair are still valid and each pair should be counted.

Sample Input/Output
Input
5
bcd
erty
ytre
opipo
dcb

Output
2

Explanation
There are two matching pairs of words in this list, ("bcd", "dcb") and ("erty", "ytre"), and one palindrome
"opipo" which is ignored. Hence, all the gloves have a matching pair and the number of matching pairs is
2.

Input
3
abcde
edcba
abcde

Output
-1
Explanation
Although "abcde" has its reversed pair "edcba" in the list, there are two "abcde"s and only one "edcba",
so each string in the list does not have a reversed pair. Therefore the output is -1.

Input
3
ioi
ertre
ghhg

Output
0

Explanation
All three of the strings in the list are palindromes, so there are no matching pairs. Therefore the output is
0.
