# добавил комментарий 25.07
# декоратор, в котором встроенная функция умеет принимать аргументы
def do_it_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('декоратор отработал')
    return wrapper


@do_it_twice
def say_word(word):
    print('функция отработала', word)


say_word("Oo!!!")
# say_word = do_it_twice(say_word)
# say_word = do_it_twice(say_word("Aa!!!"))
print(say_word)
# say_word("Oo!!!")
# Oo!!!
# Oo!!!
