import json
from difflib import get_close_matches

data = json.load(open("data.json"))

class Dictionary:

  def __init__(self, word):
    self.word = word

  def translate(self):
    word = self.word.lower()
    if word in data:
      return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
      yn = input("Did you mean %s? \nEnter Y if yes, else N for No " % get_close_matches(word, data.keys())[0]).lower()

      if yn == "yes" or yn == "y":
        return data[get_close_matches(word, data.keys())[0]]
      elif yn == "no" or yn == "n":
        return "Try again"

    else:
      return "Word does not exist, Try Another Word."


user_input = input("Enter the word: ")
dicts = Dictionary(user_input)

response = dicts.translate()

if type(response) is list:
  for i in response:
    print('"' + i + '"')

else:
  print(response)
