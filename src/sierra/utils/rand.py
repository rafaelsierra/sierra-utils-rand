# -*- coding: utf-8 -*-
import random
import string
import collections

class stringsets(object):
    DEFAULT = string.ascii_letters+string.digits+string.punctuation
    HOMOGLYPH_SAFE = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    ONLY_LETTERS = string.ascii_letters
    LETTERS_AND_NUMBERS = string.ascii_letters+string.digits
    
    
def get_random_string(length, 
                      stringset=stringsets.DEFAULT,
                      only_letters=False, 
                      letters_and_numbers=False,
                      ignoreset=None
                      ):
    '''
    Uses random.SystemRandom to return a string with `length` characters chosen 
    from `stringset`.
    >>> len(get_random_string(20) == 20 
    
    Set only_letters=True and it will return only /[a-zA-Z]/
    
    Set letters_and_numbers=True and it will return /[a-zA-Z0-9]/
    
    Set ignoreset to some string or list/tuple of characters that should not be 
    included in the return string
    
    Setting both will result in only letters.
    
    Characters from stringset may repeat (or else you could just use 
    random.SystemRandom().sample())
    
    `length` must be non-zero positive, if not, will return None
    '''
    
    if length <= 0:
        return None

    # 'set' object does not support indexing
    if isinstance(stringset, set):
        stringset = ''.join(stringset)
    
    if only_letters:
        stringset = stringsets.ONLY_LETTERS
    elif letters_and_numbers:
        stringset = stringsets.LETTERS_AND_NUMBERS
        
    if ignoreset:
        stringset = ''.join((c for c in stringset if c not in ignoreset))
    
    rand = random.SystemRandom()
    char_list = [rand.choice(stringset) for foo in xrange(length)]
    return ''.join(char_list)