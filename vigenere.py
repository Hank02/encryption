# ask user if he/she wishes to encrypt or decrypt a message
pmode = 0
while True:
    try:
        pmode = int(input("Enter 1 to encrypt or 2 to decrypt a message: "))
        while pmode not in {1, 2}:
            int(input("Oops! Please enter 1 or 2: "))
            break
        break
    except (ValueError, NameError):
        print("Oops! That entry is not supported, try again...")

# ask user for a cypher keyword
key = input("Enter codeword: ")

# create list to store converted key
keylength = len(key)
realkey = [] * keylength

# convert "key" from string of chars to string of ints
for i in key:
    if i.isalpha():
        if i.isupper():
            realkey.append(ord(i) % ord('A') + 1)
        elif i.islower():
            realkey.append(ord(i) % ord('a') + 1)
    elif ord(i) >= 48 and ord(i) <=57:
        realkey.append(int(i))
    else:
        realkey.append(0)



# prompt user for input file and open it
infile_name = input("Enter input file name: ")
infile = open(infile_name, 'r')

# prompt user for output file and open it
outfiler_name = input("Enter output file name: ")
outfile = open(outfiler_name, "w")


# if on encryption mode, encrypt
if pmode == 1:
    # iterate over inmessage and rotate (within ASCII chars 32 - 126) using realkey
    indx = -1
    # loop over infile, encrypt and write to outfile
    while True:
        # temp variable to store current char
        char = infile.read(1)
        indx += 1
        # stop when EOF is reached
        if not char:
            break
        else:
            if ord(char) + realkey[indx % keylength] > 126:
                outfile.write(chr((ord(char) - 126 + realkey[indx % keylength])))
            else:
                outfile.write(chr((ord(char) + realkey[indx % keylength])))
else:
    # iterate over inmessage and rotate (within ASCII chars 32 - 126) using realkey
    indx = -1
    # loop over infile, encrypt and write to outfile
    while True:
        # temp variable to store current char
        char = infile.read(1)
        indx += 1
        # stop when EOF is reached
        if not char:
            break
        else:
            if ord(char) + realkey[indx % keylength] < 32:
                outfile.write(chr((ord(char) + 126 - realkey[indx % keylength])))
            else:
                outfile.write(chr((ord(char) - realkey[indx % keylength])))



# close files
infile.close()
outfile.close()