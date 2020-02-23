#!/usr/bin/env python3

"""
    Reads a file, breaks the line into words, strips whitespace and punctuation from words, and converts them
    to lowercase.
    The function stats() further counts the frequency of each word as well as the percentage and inserts the
    results into two dictionaries.
"""

import string

word_list = []

def read_file(my_file):
    
    f = open(my_file, 'rb')
    
    for line in f:
        word_list = line.split()
    
    for idx in range(len(word_list)):
        word_list[idx] = str((word_list[idx]), 'utf-8') #Converts byte to str.
        word_list[idx] = word_list[idx].strip().strip(string.punctuation).lower() #Strips whitespace, punctuation and converts to lowercase.
        
    return word_list
    
def stats():
    
    word_list = read_file('file.txt')
    total_words = len(word_list) #Total number of words.
    print('Total # of words: {}\n'.format((total_words)))
    
    d = dict()
    for c in word_list:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
            
    print('Word frequency:\n {}\n'.format(d)) #Word frequency.
    
    f = dict()
    for k, v in d.items():
        percentage = round(v/total_words*100)
        f[k] = percentage
        
    print('Word frequency (%):\n {}'.format(f)) #Word frequency in percentage.

if __name__ == '__main__':
    
    print(read_file('file.txt'))
    stats()