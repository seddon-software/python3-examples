def convertCardToOrdinal(card):
    pip = card[0]
    suit = card[1]
    if suit == 'Spades': offset = 39
    if suit == 'Hearts': offset = 26
    if suit == 'Diamonds': offset = 13
    if suit == 'Clubs': offset = 0
    if pip == 'A': value = 14
    elif pip == 'K': value = 13
    elif pip == 'Q': value = 12
    elif pip == 'J': value = 11
    elif pip == '10': value = 10
    else: value = ord(pip) - ord('0')
    return value + offset
    
def compare(a, b):
    return cmp(convertCardToOrdinal(a), convertCardToOrdinal(b))

def keyfunction(item):
    return convertCardToOrdinal(item)

cards = [
         ('7','Spades'),
         ('4','Hearts'),
         ('J','Hearts'),
         ('10','Hearts'),
         ('6','Diamonds'),
         ('A','Spades'),
         ('3','Clubs'),
         ('8','Hearts')
        ]
cards.sort(cmp=compare)
print cards

cards = [
         ('7','Spades'),
         ('4','Hearts'),
         ('J','Hearts'),
         ('10','Hearts'),
         ('6','Diamonds'),
         ('A','Spades'),
         ('3','Clubs'),
         ('8','Hearts')
        ]
cards.sort(key=keyfunction)
print cards
"""This is easier to use and faster to run. When using the cmp parameter, the sorting 
   compares pairs of values, so the compare-function is called multiple times for every
   item. The larger the set of data, the more times the compare-function is called per
   item. With the key function the sorting instead keeps the key value for each item
   and compares those, so the key function is only called once for every item. This 
   results in much faster sorts for large sets of data.
"""