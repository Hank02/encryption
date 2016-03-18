
# function to convert "key" from a string of chars to a list of ints
def convert(key):
    keylength = len(key)
    realkey = []
    
    # loop over key and convert non-numbers into ints
    for i in key:
        if i.is_integer() == False:                                 
            if i.isupper():
                realkey.append(ord(i) % ord('A') + 1)