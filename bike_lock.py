#!/usr/bin/python

import itertools
import mmap

bike_lock_c1 = ['d', 'm', 'r', 'f', 'b', 'l', 'p', 'w', 's', 't']

bike_lock_c2 = ['a', 'i', 'o', 'l', 'e', 'h', 'w', 'r', 'y', 'u']
    
bike_lock_c3 = ['n', 's', 'k', 'o', 'a', 'l', 'e', 'r', 'm', 't']

bike_lock_c4 = ['g', 'k', 'm', 's', 't', 'e', 'p', 'y', 'l', 'd']

def main():
    # seen_words = set()
    scrab_file = open('four_words_scrabble.txt')
    out_file = open("words_for_bike.txt", 'w')
    search = mmap.mmap(scrab_file.fileno(), 0, access=mmap.ACCESS_READ)
    for word in itertools.product(bike_lock_c1, bike_lock_c2, bike_lock_c3, bike_lock_c4):
        word = ''.join(word).upper()
        if search.find(word) != -1:
            print (word.lower(),"True")
            out_file.write(word.lower() + "\n")
            # if word not in seen_words:
                # seen_words.add(word)

if __name__ == "__main__": main()
