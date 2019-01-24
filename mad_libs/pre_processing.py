# Four types of American words
word_type = ['adj', 'adv', 'noun', 'verb']

for i in range(4):                          # Iterate through all four types
    ### Import raw data
    file_name = 'raw_data/data.' + word_type[i]
    fi = open(file_name, 'r')


    ### Remove junk
    # Skip introduction paragraph (29 lines)
    for j in range(29):
        fi.readline()

    # Extract words 
    data = fi.readlines()                    # Read the rest of the file
    for j in range(len(data)):
        data[j] = data[j].split()[4]        # Extract the needed word in a line (4th word)
    fi.close()

    ### Remove duplicated words
    data = list(set(data))   

    
    ### Refinement
    # Because some words still have (a) or (p) etc. attach to it, remove them
    for j in range(len(data)):
        if data[j][len(data[j]) - 1] == ')':
            data[j] = data[j][:len(data[j]) - 3]


    ### Export clean data
    file_name = 'clean.' + word_type[i]
    fo = open(file_name, 'w')
    for j in range(len(data)):
        fo.write(data[j] + '\n')
    fo.close()
