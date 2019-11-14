import re
from collections import defaultdict

string = re.sub(r'[^a-zA-Z0-9 ]+', '', input().lower()) # cleanse the string
k = int(input())

hashtable = defaultdict(int)
for word in string.split():
    hashtable[word] += 1

frequencyHashtable = defaultdict(list)
frequencies = set()
for key in hashtable:
    frequencyHashtable[hashtable[key]].append(key)
    frequencies.add(hashtable[key])

for frequency in sorted(frequencies, reverse=True):
    for word in sorted(frequencyHashtable[frequency]):
        if(hashtable[word] >= k):
            print(word + " " + str(hashtable[word]))
    