class UnrecognizedError(BaseException):
    pass


# словник для зберігання чисел, які можуть бути записані в текстовому форматі
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

big_numbers = {
    "hundred": 100,
    "hundreds": 100,
    "thousands": 1000,
    "thousand": 1000,
    "million": 1_000_000,
    "millions": 1_000_000
}


# функція для перетворення чисел в текстовому форматі на числовий формат
def text_to_number(text: str) -> int:
    """This function convert text to int
    if it can't be converted, raised UnrecognizedError
    """


    # розділяємо текст на окремі слова
    words = text.split()

    # змінні для зберігання числа та числівника
    number = 0
    previous = 0

    # перетворюємо слова на числа
    for word in words:

        if word in numbers:
            number += numbers[word]
            previous += numbers[word]

        elif word in big_numbers:
            big_number = big_numbers[word]
            remainder = number % big_number

            if remainder:
                if number < big_number:
                    number = big_number * remainder
                    previous = big_number * remainder

                else:
                    number += big_number * remainder - remainder
                    previous = big_number * remainder

        else:
            raise UnrecognizedError(f'unrecognized word "{word}"')

    return number


def main():
    i = 0
    while i < 10:
        i += 1
        num = input("Type your number: ")
        if num == "stop":
            break

        try:
            print(text_to_number(num))
        except UnrecognizedError as e:
            print(f"Unrecognized: {e}")
            continue


if __name__ == "__main__":
    main()
