"""Импорт библиотек"""
from random import shuffle


def get_words():
    """
    Функция получения списка слов
    :return: возвращает список слов
    """
    with open('words.txt', 'r', encoding='utf-8') as file:
        return file.read().split()


def shuffle_word(word):
    """
    Функция перемешивания слова
    :param word:
    :return: возвращает перемешанное слово
    """
    word = list(word)
    shuffle(word)
    return ''.join(word)


def save_result(name, score):
    """
    Функция сохранения результата
    :param name: имя пользователя
    :param score: баллы пользователя
    """
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {score}\n")


def get_statistics():
    """
    Функция получения статистики
    :return: результаты в виде списка целых чисел пользователя
    """
    with open("history.txt", "r", encoding="utf-8") as file:
        text = file.read()
    results = [int(result.split()[1])
               for result in text.split("\n")[:-1]]
    return results


def text_statistics(results):
    """
    Функция вывода статистики
    :param results: список целых чисел
    :return: количество игр и максимальный рекорд
    """
    return f"Всего игр: {len(results)}\n" \
           f"Максимальный рекорд: {max(results)}"


def main():
    """
    Основная функция
    """
    name = input("Введите ваше имя: ")
    counter = 0
    for word in get_words():
        print(f"Угадай слово: {shuffle_word(word)}")
        user_input = input()
        if user_input == word:
            print("Верно! Вы получаете 10 очков.")
            counter += 10
        else:
            print(f"Неверно! Верный ответ - {word}.")
    save_result(name, counter)
    print(text_statistics(get_statistics()))


""" Запуск программы """
if __name__ == '__main__':
    main()
