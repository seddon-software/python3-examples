"""
Create two subroutines that convert a decimal number in the 
range 1 to 4000 to Roman numerals, and back. Warning: This 
question is rather more difficult than it looks. Don't spend 
too much time on it."""

lookUp1 = { 
          'I' :    1,
          'V' :    5,
          'X' :   10,
          'L' :   50,
          'C' :  100,
          'D' :  500,
          'M' : 1000
         }
lookUp2 = { 
             0: '', 
             1: 'I', 
             2: 'II', 
             3: 'III', 
             4: 'IV', 
             5: 'V',
             6: 'VI', 
             7: 'VII', 
             8: 'VIII', 
             9: 'IX', 
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX',
            90: 'XC',
           100: 'C',
           200: 'CC',
           300: 'CCC',
           400: 'CD',
           500: 'D',
           600: 'DC',
           700: 'DCC',
           800: 'DCCC',
           900: 'CM',
          1000: 'M',
          2000: 'MM',
          3000: 'MMM',
          4000: 'MMMM'
         }

def toRoman(decimal):
    """
    analyse each of the 4 digits in turn
    """
    digits = list(str(decimal + 10000)) # make sure leading zeros are included
    # build list of digits (ignoring first digit)
    symbols = list()
    symbols.append(lookUp2[int(digits[1])*1000])
    symbols.append(lookUp2[int(digits[2])* 100])
    symbols.append(lookUp2[int(digits[3])*  10])
    symbols.append(lookUp2[int(digits[4])*   1])
    return "".join(symbols)
    

def toDecimal(romanNumeral):
    """
    build a list of roman symbols
    """
    theList = []
    for symbol in list(romanNumeral):
        theList.append(lookUp1[symbol])
    
    """
    if symbol is less than its successor it is negative
    so flip its sign
    """
    for i in range(theList.__len__() - 1):
        if theList[i] < theList[i + 1]:
            theList[i] = -theList[i]
    
    """
    all that remains is to sum all the items in the list
    """
    result = 0
    for n in theList:
        result += n     
    
    return result
       
print toRoman(2671) # MMDCLXXI
print toDecimal("XLIV")   # 44
print toDecimal("XLVI")   # 46
print toDecimal("XCIII")  # 93
print toDecimal("XCIV")   # 94
print toDecimal("CLXXXIV")   # 184
print toDecimal("MCMXXXIV")   # 1934

"""
convert in both directions and print out any discrepancies
"""
for i in range(4000):
    r = toRoman(i)
    print r
    n = toDecimal(r)
    if i - int(n) != 0:
        print "Error: ", i


