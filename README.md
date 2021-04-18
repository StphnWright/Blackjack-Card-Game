**ENGI E1006 - Intro to Computing for Engineers & Applied Scientists**

Group Exercise Set 4

Upload the following four files to Courseworks:

problem1.py
problem2.py

**Important:** If you re-submit your assignment you need to re-upload all files, even if you changed just one of them. Otherwise, any files you uploaded previously will be lost if you submit a second time. 

**Problem 1 (60 pts) - Counting n-grams**
An n-gram is a contiguous sequence of n words in a given sequence of text. An n-gram of size 1 is referred to as a unigram, of size 2 is a bigram, and size 3 is a trigram. For example, for the sentence "Columbia University is great" the unigrams would be

    [('columbia',), ('university',), ('is',), ('great',)], 

the bigrams would be 

    [('columbia','university'), ('university','is'), ('is','great')], 

and the trigrams would be 

    [('columbia','university','is'), ('university','is','great')]

N-grams are frequently used in Natural Language Processing, in applications such as language modeling to identify a text's genre or author, or in machine translation to judge the quality of the translation output. 

Download the file problem1.py and complete the functions as described below. 

(a) Fill in the function count_ngrams(file_name, n), which should read an input file (file name provided as a string) and returns a dictionary of n-gram counts. This result dictionary should map each n-grams to the number of times that n-gram appears in the input text. Each n-gram key is a tuple (as in the example above) and the count is an int. Preprocess the file by converting everything to lower-case and removing punctuation. 

**Important:** n-grams can cross lines in the input file. Your program should remove line breaks and treat the text as one long list of words. 

(b) Fill in the function single_occurences(ngram_count_dict), which takes a dictionary as its only parameter (in the format produced by count_ngrams) and returns a list of all n-grams that occur only once.  This function should return a list of all n-grams with a count of 1. 

(c) Fill in the function most_frequent(ngram_count_dict, num) that takes in two parameters:
ngram_count_dict is a dictionary of ngram counts in the format returned by count_ngrams. num denotes the number of n-grams to return. This function returns a list of the num n-grams that appear most frequently in the input file.  For example if num=10, the method should return the 10 most frequent n-grams in a list. 

**Hint:** To get the num most frequent n-grams,  you will need to sort the information in the dictionary. Python does not support any way of sorting dictionaries directly, because they are unordered. The easiest way to do this is to convert the dictionary into a list of (frequency, n-gram) tuples and then sort that list.

A main function has been provided to test the functionality of your code. You can test your code on the file alice.txt. You are encouraged to change up the main method to make sure your functions work with different arguments. 

**Problem 2 (40 pts) - Black Jack**

Black Jack is a popular casino game played with a standard 52 card deck. A single player plays against the "dealer". (The rules below vary slightly from the game as it is commonly played in casinos).

**Basic rules:** In the first part of the game, the player is dealt cards repeatedly until one of the following events happens: 

 1. The player's score (i.e. the sum of the values of the player's cards, explained below) reaches 21. In this case, the player wins immediately.
 2. The player's score exceed 21. In this case, the player loses immediately. 
 3. The player decides to "stay", i.e. not take any more cards. 

If the player has neither won or lost at this point, it is the dealer's turn to draw cards. The dealer keeps drawing cards until the sum of her card values is 17 or higher. Then she stops and the winner is determined as follows: 

 1. If the dealer's score reaches 21, she wins.
 2. If the dealer's score exceeds 21, the player wins.
 3. If the sum of the card values of the player and the dealer are equal, the game is a "push" and nobody wins. 
 4. Otherwise, the person with the highest score wins. 

**Card values:** The card deck consists of 52 cards. There are four "suits": spades (♠), hearts (♥), diamonds (♦) and clubs (♣). For each suit, there are 13 cards with different ranks: 9 number cards with the values 2-10, three "face" cards Jack ("J"), Queen("K"), and King ("K"), and an Ace card ("A"). In black jack, all face cards have the value 10. 

The value of an Ace card depends on the context in which the card is dealt. If the player is dealt an Ace, the card's value is 11 unless this would result in a total score of more than 21. In that case, the value of the Ace is 1. The same rule applies if it is the dealer's turn. 

(a) Write the class Card, which represents a single playing card. The class should define two attributes, suit and rank. Both should be strings and they should be initialized with the parameters passed to the __init__(self, suit, value) method, so you can use the following line to create a new card: 

    some_card = Card('♠','A')
    another_card = Card('♥','10')

Write a suitable __str__(self) method for your class that returns a single string representing the card's suit and rank.

(b) Write the value(self,total) method of the Card class, that returns the game value of the card as an int, given the current score. If the card is a number card, that number should be the value. If it is a face card, the value should be 10. If it is an Ace, the value depends on the current score of either the player or the dealer, which is passed to the method as a parameter (1 or 11, see above).

(c) Outside of your Card class, write the function make_deck(), that returns a list of all possible 52 cards. Instead of listing each card in your code explicitly, use nested for loops to create the cards. Before returning the list, use the random.shuffle(some_list) method, which shuffles the element of some_list in place (i.e. it modifies some_list, rather than returning a new list).

(d) Write a main() function that plays a single game of Black Jack according to the rules specified above. First, get a new list of cards by calling the make_deck() method. To deal a card, remove the first element from the list. Keep track of the player's score. Call the card's value method to determine the value of the card. After each card, evaluate if the player has won or lost and otherwise ask her if she wants another card. If the player decides to "stay", perform the dealer's turn as described above (continue to use the same deck). 

Here is example output for a game of Black Jack. Your program does not have to mimic this output precisely. 

    You drew ♥9.
    sum: 9
    Do you want another card? (y/n)y
    You drew ♠Q.
    sum: 19
    Do you want another card? (y/n)n
    My turn.
    I drew ♦4
    My sum: 4
    I drew ♦6
    My sum: 10
    I drew ♦3
    My sum: 13
    I drew ♠3
    My sum: 16
    I drew ♦8
    My sum: 24
    You win.
