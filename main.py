# This code is from Autocorrect starter code for Code2College Elite Qualifier,https://replit.com/@jmslocum16/AutocorrectStarter#main.py

import time
#text
import nltk
from nltk.corpus import words
from nltk.metrics.distance import (
  #edit_distance,
  jaccard_distance,
  )
from nltk.util import ngrams
nltk.download('words')
import pandas

correct_spellings = words.words()
spelling_series = pandas.Series(correct_spellings)
spelling_series

"""
def jaccard(entries, gram_number):
  outcomes = []
  for entry in entries:
    spellings = spelling_series[spelling_series.str.startswith(entry[0])]
    distances = ((jaccard_distance(set(ngrams(entry, gram_number)), set(ngrams(word, gram_number))), word) for word in spellings)
    closest = min(distances)
    outcomes.append(closest[1])
  return outcomes

def JDreco(entries=['cormulent', 'incendenece', 'validrate']):
  return jaccard(entries, 3)
print(JDreco())

userinput = []
for i in range(0,3):
  word = input("Type the word(s): ")
  userinput.append(word)
userinput 
"""  
# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words


def suggest(entries, all_words):
  # YOUR CODE HERE. 
  if entries in all_words:
    
    print(entries + " is a word")
    
  else:
    
    for entry in entries:
      temp = [(jaccard_distance(set(ngrams(entry, 2)), set(ngrams(w, 2))),w) for w in correct_spellings if w[0]==entry[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])

def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        #entries = input(':> ')
        entries = []
        if ('quit' == entries):
          break
        
        for i in range(0, 1):
          word = input("Type the word(s): ")
          entries.append(word)
        entries
        suggest(entries, all_words)

if __name__ == "__main__":
    main()
















#This is a different type of autocorrect that doesn't work as well as the one above.













"""# This code is from Autocorrect starter code for Code2College Elite Qualifier,https://replit.com/@jmslocum16/AutocorrectStarter#main.py

import time

import nltk
from nltk.corpus import words
from nltk.metrics.distance import (
  #edit_distance,
  jaccard_distance,
  )
from nltk.util import ngrams
nltk.download('words')
import pandas

correct_spellings = words.words()
spelling_series = pandas.Series(correct_spellings)
spelling_series


def jaccard(entries, gram_number):
  outcomes = []
  for entry in entries:
    spellings = spelling_series[spelling_series.str.startswith(entry[0])]
    distances = ((jaccard_distance(set(ngrams(entry, gram_number)), set(ngrams(word, gram_number))), word) for word in spellings)
    closest = min(distances)
    outcomes.append(closest[1])
  return outcomes

def JDreco(entries=['cormulent', 'incendenece', 'validrate']):
  return jaccard(entries, 3)
print(JDreco())

userinput = []
for i in range(0,3):
  word = input("Type the word(s): ")
  userinput.append(word)
userinput 

# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words


def suggest(text, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that
  if text in all_words:
    print(text + " is a word")
  else:
    entries = []
    for i in range(0,3):
      word = input("Type the word(s): ")
      entries.append(word)
    entries

    for entry in entries:
      temp = [(jaccard_distance(set(ngrams(entry, 2)), set(ngrams(w, 2))),w) for w in correct_spellings if w[0]==entry[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])

def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()


"""