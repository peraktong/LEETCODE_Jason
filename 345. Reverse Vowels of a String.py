
"""
https://docs.python.org/2/howto/regex.html

There are two more repeating qualifiers. The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional. For example, home-?brew matches either homebrew or home-brew.

The most complicated repeated qualifier is {m,n}, where m and n are decimal integers. This qualifier means there must be at least m repetitions, and at most n. For example, a/{1,3}b will match a/b, a//b, and a///b. It won’t match ab, which has no slashes, or a////b, which has four.

You can omit either m or n; in that case, a reasonable value is assumed for the missing value. Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity — actually, the upper bound is the 2-billion limit mentioned earlier, but that might as well be infinity.

Readers of a reductionist bent may notice that the three other qualifiers can all be expressed using this notation. {0,} is the same as *, {1,} is equivalent to +, and {0,1} is the same as ?. It’s better to use *, +, or ? when you can, simply because they’re shorter and easier to read.


"""

import re
def reverseVowels(s):

    ### Here ? means "or" and aeiou can happens any time.

    vowels = re.findall('(?i)[aeiou]', s)

    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


reverseVowels(s="hello")
