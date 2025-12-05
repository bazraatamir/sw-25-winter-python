# hangman.py
import random

def choose_word(word_list):
    
    # word_list-ээс нэг үгийг random буюу санамсаргүйгээр сонгоно
    # Сонгосон үгийг бүх том үсэг болгон буцаана
    pass

def display_progress(word, guessed_letters):
    # Нууц үгийн бүх үсгийг нэг нэгээр шалгана
    # Хэрэв тоглогч таасан бол тухайн үсгийг харуулна
    # Хэрэв таагаагүй бол '_' гэж харуулна
    # Бүх үсгийг нэг мөр болгон хэвлэнэ 
    pass

def get_guess(already_guessed):
    # Хэрэглэгчээс input авна
    # Оролт зөвхөн нэг үсэг эсэхийг шалгана
    # Аль хэдийн таасан үсэг бол дахин нэвтрүүлэх боломж олгоно
    # Зөв үсгийг буцаана
    pass

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