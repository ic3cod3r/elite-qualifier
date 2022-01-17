# This code is from Autocorrect starter code for Code2College Elite Qualifier,https://replit.com/@jmslocum16/AutocorrectStarter#main.py
#Used stack overflow, stackabuse, geeksforgeeks, https://www.geeksforgeeks.org/create-a-gui-to-get-domain-information-using-tkinter/?ref=rp  , https://stackoverflow.com/questions/22800401/how-to-capitalize-the-first-letter-of-every-sentence 

import time
#text

import nltk
from nltk.corpus import words
"""from nltk.metrics.distance import (
  #edit_distance,
  jaccard_distance,
  )"""
from tkinter import *
from textblob import TextBlob
#from nltk.util import ngrams
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

def clearAll() :
     
    # whole content of text entry area is deleted
    word1_field.delete(0, END)
    word2_field.delete(0, END)
 
# Function to get a corrected word
def correction() :
 
    # get a content from entry box
    input_word = word1_field.get().lower()   #I added .lower() because the autocorrect did not correct it properly if it was upper case.
  
  #print("One",input_word)
    # create a TextBlob object
    start_time = time.time()


    #print("Two", input_word)
    blob_obj = TextBlob(input_word)
 
    # get a corrected word
    corrected_word = str(blob_obj.correct()).capitalize() #Added .capitalize() so that it adds back the capital letter that I took out, and if there never was one, I added one to make it gramaticaly correct
  
    #Added this below to make each letter after a period capitalized to make it gramticaly correct.
    sentence = corrected_word.split('.')
    for i in sentence:
      print (i.strip().capitalize()+". ",end='')
    print()
  
    # insert method inserting the
    # value in the text entry box.
    word2_field.insert(10, corrected_word)
    #word2_field.insert(10, i.strip().capitalize()+". ",end='')
    end_time = time.time()

    
    print()
    elapsed_time = end_time - start_time
    print('Corrected ' + input_word + ' in ' + f'{elapsed_time:.2f}' + ' seconds.')
    print()

  
# Driver code
if __name__ == "__main__" :
    

    # Create a GUI window
    root = Tk()
 
    # Set the background colour of GUI window
    root.configure(background = 'black')
     
    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("400x150")
 
    # set the name of tkinter GUI window
    root.title("Mazz Enterprise Autocorrect")
     
    # Create Welcome to Spell Corrector Application: label
    headlabel = Label(root, text = 'Welcome to Mazz Enterprise Autocorrect Application',
                    fg = 'black', bg = "red")
     
    # Create a "Input Word": label
    label1 = Label(root, text = "Input Word",
                fg = 'black', bg = 'blue')
         
    # Create a "Corrected Word": label
    label2 = Label(root, text = "Corrected Word",
                fg = 'black', bg = 'blue')
     
     
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    # padx keyword argument used to set padding along x-axis .
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 4, column = 0)
    label2.grid(row = 10, column = 0, padx = 10)
 
         
    # Create a text entry box
    # for filling or typing the information.
    word1_field = Entry()
    word2_field = Entry()
         
    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    word1_field.grid(row = 4, column = 1, padx = 10, pady = 10)
    word2_field.grid(row = 10, column = 1, padx = 10, pady = 10)
 
         
    # Create a Correction Button and attached
    # with correction function
    button1 = Button(root, text = "Correction", bg = "red", fg = "black",
                                command = correction)
         
    button1.grid(row = 6, column = 1)
     
    # Create a Clear Button and attached
    # with clearAll function
    button2 = Button(root, text = "Clear", bg = "red",
                    fg = "black", command = clearAll)
     
    button2.grid(row = 12, column = 1)
     
    # Start the GUI
    root.mainloop()


"""
#This is my code before the GUI, need to figure out how to make it part of my own code!!!!

from textblob import TextBlob

with open("text.txt", "r") as f:        # Opening the test file with the intention to read
    text = f.read()                     # Reading the file
    textBlb = TextBlob(text)            # Making our first textblob
    textCorrected = textBlb.correct()   # Correcting the text
    print(textCorrected)


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





"""










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