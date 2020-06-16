def break_words(stuff):
    """LPTHW: This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """LPTHW: Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """LPTHW: Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """LPTHW: Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """LPTHW: Takes a full sentence in and return the sorted words."""
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
    """LPTHW: Takes full sentence and prints first & last words."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """LPTHW: Takes full sentence, sorts, then prints first and last."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# Import will generate: ex25.pyc
# That appears to be the compiled python module.
"""
Python 2.7.12 (default, Apr 15 2020, 17:07:12)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> s = "All good things come to those who wait."
>>> words = ex25.break_words(s)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(s)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(s)
All
wait.
>>> ex25.print_first_and_last_sorted(s)
All
who
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
"""

# help(ex25)  to use the Python Doc
