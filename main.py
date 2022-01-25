# This code is from Autocorrect starter code for Code2College Elite Qualifier,https://replit.com/@jmslocum16/AutocorrectStarter#main.py
#Used stack overflow, stackabuse, geeksforgeeks, https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/ , https://stackoverflow.com/questions/22800401/how-to-capitalize-the-first-letter-of-every-sentence 

#The correction will also be placed in the console, where it will allow you to copy the corrected version and post it into your document, it will also tell you the time it took to correct the word(s). The correction in the console is also a little different from the correction in the GUI window, as the correction in the console adds periods and capitalization, whilst the correction in the GUI window does not.

#This is where I imported a bunch of libraries that are used later on in the code-
import time


import nltk
from nltk.corpus import words
from tkinter import *
from textblob import TextBlob
nltk.download('words')
import pandas

correct_spellings = words.words()
spelling_series = pandas.Series(correct_spellings)
spelling_series


#This clears both the begining text and the fixed text boxes-
def clearAll() :
     
    #text entry and correction is deleted-
    word1_field.delete(0, END)
    word2_field.delete(0, END)
 


#Function to get a corrected word-
def correction() :
 
    # get the word(s) from entry box-
    input_word = word1_field.get().lower()   #I added .lower() because the autocorrect did not correct it properly if it was upper case.

    #Stats the timer-
    start_time = time.time()
  
    # create a TextBlob object-
    blob_obj = TextBlob(input_word)
 
    # get a corrected word-
    corrected_word = str(blob_obj.correct()).capitalize() #Added .capitalize() so that it adds back the capital letter that I took out, and if there never was one, I added one to make it gramaticaly correct.
  
    #Added this below to make each letter after a period capitalized to make it gramticaly correct-
    sentence = corrected_word.split('.')
    for i in sentence:
      print (i.strip().capitalize()+". ",end='')
    print()
  
    # insert method inserting the value in the text entry box-
    word2_field.insert(10, corrected_word)

    #This ends the timer-
    end_time = time.time()

    #To make the format look better-
    print()

    #To show how long it took to correct the input-
    elapsed_time = end_time - start_time
  
    print('Corrected ' + input_word + ' in ' + f'{elapsed_time:.2f}' + ' seconds.')
    print()

  
# Driver code

#This is what runs and starts the code-
if __name__ == "__main__" :
    

    # Create a GUI window-
    root = Tk()
 
    # Set the background colour of GUI window-
    root.configure(background = 'black')
     
    # Set the configuration of GUI window (WidthxHeight)-
    root.geometry("400x150")
 
    # set the name of tkinter GUI window-
    root.title("Mazz Enterprise Autocorrect")
     
    # Create Welcome to Spell Corrector Application: label-
    headlabel = Label(root, text = 'Welcome to Mazz Enterprise Autocorrect Application',
                    fg = 'black', bg = "red")
     
    # Create a "Input Word": label-
    label1 = Label(root, text = "Input Word",
                fg = 'black', bg = 'blue')
         
    # Create a "Corrected Word": label-
    label2 = Label(root, text = "Corrected Word",
                fg = 'black', bg = 'blue')
     
     
    #This is what creates the grid like structure for placing all the widgets into the grid like structure-
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 4, column = 0)
    label2.grid(row = 10, column = 0, padx = 10)    # padx keyword argument used to set padding along x-axis
 
         
    # Create a text entry box-
    word1_field = Entry()
    word2_field = Entry()

    word1_field.grid(row = 4, column = 1, padx = 10, pady = 10) # padx keyword used to set padding along x-axis
    word2_field.grid(row = 10, column = 1, padx = 10, pady = 10) # pady keyword used to set padding along y-axis
 
         
    # Create a Correction Button that uses the above correction function-
    button1 = Button(root, text = "Correction", bg = "red", fg = "black",
                                command = correction)
         
    button1.grid(row = 6, column = 1)
     
    # Create a Clear Button that uses the above clearAll function-
    button2 = Button(root, text = "Clear", bg = "red",
                    fg = "black", command = clearAll)
     
    button2.grid(row = 12, column = 1)
     
    # This is what starts the GUI-
    root.mainloop()





#Hope you enjoyed!








