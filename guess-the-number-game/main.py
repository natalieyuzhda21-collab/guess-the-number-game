import random

def guess_the_number():
    print("Привет! Я загадал число от 1 до 100. Попробуй угадать!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Введи свое число: "))
            attempts += 1

            if user_guess < secret_number:
                print("Слишком мало! Попробуй еще раз.")
            elif user_guess > secret_number:
                print("Слишком много! Попробуй еще раз.")
            else:
                print(f"🎉 Поздравляю! Ты угадал число за {attempts} попыток!")
                break
        except ValueError:
            print("Пожалуйста, введи корректное целое число.")

if __name__ == "__main__":
    guess_the_number()
