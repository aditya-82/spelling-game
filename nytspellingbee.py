
def main():
    possible_words = []
    words = get_words()
    alphabets = []
    final_answers = []
    
    while True:
        primary_alphabet = input("Enter primary alphabet: ")
        if char_check_2(primary_alphabet):
            break
        else:
            continue
    
    for word in words:
        if prime_alpha_check(word, primary_alphabet):
            possible_words.append(word)
        else:
            continue
    
    alphabets.append(primary_alphabet)
    while True:
        try:
            letter = input("Enter secondary alphabets(Control z to end): ")
        except EOFError:
            break
        
        if char_check_2(letter):
            alphabets.append(letter)
        else:
            print("Not accepted. Please type a letter")
    
    for word in possible_words:
        if char_check_3(word, alphabets) == True:
            final_answers.append(word)
        else:
            continue

    print(final_answers)


def get_words():
    w = []
    with open("words.txt") as file:
        a = file.readlines()
        for word in a:
            word = word.lower().strip()
            correct = char_check_1(word)
            if correct == True:
                w.append(word)
            else:
                continue
        return w


def char_check_1(a):
    ans = True
    for char in a:
        if char.isalpha() == False:
            ans = False
            return ans
        else:
            continue
    return ans


def char_check_2(a):
    if len(a) == 1:
        if a.isalpha() == True:
            return True
        else:
            return False
    else:
        return False


def prime_alpha_check(a, b):
    for letter in a:
        if letter == b:
            return True
        else:
            continue

    return False


def char_check_3(a, b):
    if len(a) > 3:
        for letter in a:
            if letter in b:
                continue
            else:
                return False
    else:
        return False
    return True 


if __name__ == "__main__":
    main()