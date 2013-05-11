# sierra-utils-rand

*New functions wanted!*

Use this to add more random functions to your code without having to code it over and over again (like generating random strings)

## Available functions:

`sierra.utils.rand.get_random_string()`:

    
    >>> from sierra.utils.rand import get_random_string
    >>> get_random_string(20)
    'I^NPBYp]8U2#k+U,W/O~'
    >>> get_random_string(10, stringset='huae')
    'aheuhahauh'
    >>> get_random_string(15, only_letters=True)
    'DMbncnvPONHgfIA'
    >>> get_random_string(15, letters_and_numbers=True)
    '6bS8KmBtE1Rs5Eg'
    
This functions is useful to generate tokens and initial passwords.




