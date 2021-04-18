"""
A program for counting n-grams, a continuous sequence of n words in a given text sequence. 

The function count_ngrams reads an input file and returns a dictionary of n-gram counts, the
result dictionary maps n-grams to their frequency. The single_occurence function takes in a
dictionary and returns a list of n-grams with only one occurrence, while the most_frequent
function takes in two parameters and returns a list of num n-grams with the highest occurrence
in the file. The main function tests the functionality of the code under various arguments.
"""

from collections import defaultdict
import string


def count_ngrams(file_name, n=2): 

    result = defaultdict(int)
    
    with open(file_name) as fp:
        text = " ".join(fp.readlines())
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.lower().strip().split()
        for i in range(len(words) - n):
            ngram = tuple(words[i:i + n])
            result[ngram] += 1
                
    return result


def single_occurences(ngram_count_dict): 
    
    single_ngrams = []
    for ngram, count in ngram_count_dict.items():
        if count == 1:
            single_ngrams.append(ngram)
    
    return single_ngrams


def most_frequent(ngram_count_dict, num=5): 
    
    freq_list = []
    most_freq = []
    
    for ngram, count in ngram_count_dict.items():
        freq_list.append((count, ngram))
        
    freq_list.sort(reverse=True)
    
    for ngram in freq_list[:num]:
        most_freq.append(ngram)
        
    return most_freq


def main():
    
    filename = "alice.txt"
    n = 2
    m = 3
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)
    
    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))
    print()
    
    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))
    print()
    
    ngram_counts = count_ngrams(filename, m)
    
    print('{}-grams that occur only once:'.format(m))
    print(single_occurences(ngram_counts))
    print()
    
    print('{} most frequent {}-grams:'.format(most_frequent_k, m))
    print(most_frequent(ngram_counts, most_frequent_k))
    print()


if __name__ == "__main__":
    main()
    
