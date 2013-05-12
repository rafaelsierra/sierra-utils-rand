# sierra-utils-rand

*New functions wanted!*

Use this to add more random functions to your code without having to code it over and over again (like generating random strings)

## Install

Just `pip install sierra-utils-rand` (or `python setup.py install`) 

## Available functions:

### `sierra.utils.rand.get_random_string()`:

This functions is useful to generate tokens and initial passwords.

#### Usage:

    >>> from sierra.utils.rand import get_random_string
    >>> get_random_string(20)
    'I^NPBYp]8U2#k+U,W/O~'
    >>> get_random_string(10, stringset='huae')
    'aheuhahauh'
    >>> get_random_string(15, only_letters=True)
    'DMbncnvPONHgfIA'
    >>> get_random_string(15, letters_and_numbers=True)
    '6bS8KmBtE1Rs5Eg'

#### Params:

* `length` - Length of return random string
* `stringset` - String or iterable of options to generate the random string
* `only_letters` - Returns a random string with only letters (case-sensitive) 
* `letters_and_numbers` - Same as `only_letters` but with numbers [0-9]
* `ignoreset` - Determines that some characters should be removed from stringset before generating the random string

#### Related

You can also use `sierra.utils.rand.stringsets` to use some predefined stringsets, options are:

* `stringsets.DEFAULT` - Default stringset when not setting one, includes letters, numbers and punctuations 
* `stringsets.HOMOGLYPH_SAFE` - Returns a [Homoglyph](https://en.wikipedia.org/wiki/Homoglyph) safe string. The actual string is: `abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789` 
* `stringsets.ONLY_LETTERS` - Returns only letters from a-z, upper case and lower case
* `stringsets.LETTERS_AND_NUMBERS` - Same as `ONLY_LETTERS` but with numbers 
    





