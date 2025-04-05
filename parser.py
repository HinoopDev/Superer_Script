import constants

def parse(text:str)->list:
    str_counter = False
    lined_text  = []
    word = []

    # get rid of \n
    text = text.replace("\n", ";")

    # seperate segments
    for char in text:
        if char == '"' and not str_counter: 
            str_counter = True
            if word != []: 
                lined_text.append("".join(word))
                word.clear()
            word.append('"')

        elif char == '"' and str_counter: 
            str_counter = False
            word.append('"')
            lined_text.append("".join(word))
            word.clear()

        elif char == " " and not str_counter:
            if word != []:
                lined_text.append("".join(word))
                word.clear()


        elif char in constants.OPPERATORS or char in constants.SINGLEKEYS or char in constants.BRAKETS:
            if word != []:
                lined_text.append("".join(word))
                word.clear()
            word.append(char)
            lined_text.append("".join(word))
            word.clear()

        else: word.append(char)
    if word != []: lined_text.append("".join(word))

    # gets types
    


    return lined_text