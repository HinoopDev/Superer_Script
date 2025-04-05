import constants

def parse(text:str)->list:
    str_counter = False
    lined_text  = []
    word = []
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


        elif char in constants.OPPERATORS:
            if word != []:
                lined_text.append("".join(word))
                word.clear()
            word.append(char)
            lined_text.append("".join(word))
            word.clear()

        elif char in constants.SINGLEKEYS:
            if word != []:
                lined_text.append("".join(word))
                word.clear()
            word.append(char)
            lined_text.append("".join(word))
            word.clear()

        else: word.append(char)
    if word != []: lined_text.append("".join(word))
    return lined_text
