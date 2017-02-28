
def display(word, guessed_letters):
    
   
    word = word.upper()

    new_word = ""
    for char in word:                     
        new_word += char 
        new_word += " "

    word_list = list(new_word)  

    start_word_list = [' '] * len(word_list)
    for i in range(len(word_list)):
        if word_list[i].isalpha():
            start_word_list[i] = "_"
        else:
            start_word_list[i] = word_list[i]

    word_so_far = "".join(start_word_list)


    
    for i in range(len(guessed_letters)):
        for j in range(len(word_list)):

            if guessed_letters[i] == word_list[j]:
                word_list[j] = " "
                start_word_list[j] = guessed_letters[i]

    return "".join(start_word_list)
    
print display("ELEPHANT",["E","N"])



