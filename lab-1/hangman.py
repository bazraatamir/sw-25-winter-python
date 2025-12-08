# hangman.py
import random

def choose_word(word_list):
    # word_list-ээс нэг үгийг random буюу санамсаргүйгээр сонгоно
    word = random.choice(word_list)
    # Сонгосон үгийг бүх том үсэг болгон буцаана
    return word.upper()
   
   
    pass

def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
         # Нууц үгийн бүх үсгийг нэг нэгээр шалгана
        if letter in guessed_letters:
             # Хэрэв тоглогч таасан бол тухайн үсгийг харуулна
            progress += letter + "*"
        else:
            # Хэрэв таагаагүй бол '*' гэж харуулна
            progress +="*"
    # Бүх үсгийг нэг мөр болгон хэвлэнэ 
    print("Одоогийн байдал: " + progress)
   
    
    pass

def get_guess(already_guessed):
    # Хэрэглэгчээс input авна
    gues = input("Та нэг үсэг таа: ").upper()

    # Оролт зөвхөн нэг үсэг эсэхийг шалгана
    if len(gues) !=1 or not gues.isalpha():
        print("Зөвхөн нэг үсэг оруулна уу.")
        return get_guess(already_guessed)
        
    # Аль хэдийн таасан үсэг бол дахин нэвтрүүлэх боломж олгоно
    if gues in already_guessed:
        print("Та энэ үсгийг аль хэдийн таасан байна. Өөр үсэг оруулна уу.")
        return get_guess(already_guessed)
    # Зөв үсгийг буцаана
    return gues

def update_state(word, guess, guessed_letters):
    # Жинхэнэ state-ийг шинэчилнэ
    pass


def main():
    word_list = ["PYTHON","MONGOL","COMPUTER","HANGMAN"]
    word = choose_word(word_list)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong and not  (set(word) <= guessed_letters):
        display_progress(word, guessed_letters)
        guess = get_guess(guessed_letters)
        # update_state ...

if __name__ == "__main__":
    main()