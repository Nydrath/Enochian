import json

with open("text", "r", encoding='utf-8-sig') as f:
  original_text = f.read()
with open("pronounciation", "r", encoding='utf-8-sig') as f:
  pronounciation = f.read()

original_text = original_text.translate({ord(i):None for i in '.,:;!?()'}).lower().split()
pronounciation = pronounciation.translate({ord(i):None for i in '.,:;!?()'}).lower().split()
dict = {}
for word, pronounciation in zip(original_text, pronounciation):
  if word not in dict:
    dict[word] = pronounciation
  else:
    if dict[word] != pronounciation:
      print("Error! {0} has been written to pronounce {1} and {2}, which are different!".format(word, dict[word], pronounciation))

with open("pronounciation_key.json", "w") as f:
  json.dump(dict, f, sort_keys=True, indent=4)