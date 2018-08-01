import json
import re


pattern = re.compile(r'\w{2,}')
words = {}
contents = None

with open('output.txt') as f:
    contents = f.read()


data = [json.loads(str(item)) for item in contents.strip().split('\n')]


for d in data:
    for w in d['text'].lower().split():
        match = pattern.match(w)
        if match:
            regex_word = match.group()
            if regex_word not in words:
                words[regex_word] = 1
            else:
                words[regex_word] += 1


print(words)
