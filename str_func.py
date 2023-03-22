def str_func(source_string):
    return source_string.upper()


def first_letter():
    '''возвращает принятую строку с первой буквой в верхнем регистре'''
    numb = len(source_string)
    return f"{source_string[0].upper()}{source_string[1:numb]}"
