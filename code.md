
quote_gen.py
============


no cli arguments. 


Just read the quotes.json file, randomise the quotes and store the random order as a pickle object. 
use that pickle object and pop one of the list and print that quote. and quit. 
When you run it again, the pickle file will be present then just pop one of the list, print the quote and quit. 

Generalised algorithm
=====

1. Start. 
2. Look for the pickle file containing the list of random quotes. 
2a) Unpickle the file and get the random list of quotes 
2b) File not present. Then create a random list of quotes from quotes.json and return the random list 
3. Pop a quote from the random list of quotes. 
4. Print the quote
5. Persist the new state of random quotes list and exit .


Algorithm to Create a random list of quotes
======

1. Read quotes.json and get the total number of quotes.
2. Create a list containing the indices representing the quotes. 
3. Randomise the list. 



Implementation
==============

Place to store the data: 
$QUOTE_GEN_PATH = "~/.quote_gen/"

quotes.json: $QUOTE_GEN_PATH/quotes.json 
pickle file: $QUOTE_GEN_PATH/qpersist
