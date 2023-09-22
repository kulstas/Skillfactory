import datetime
import re

# def get_last_name(full_name):
#     last_name = full_name.split(' ')[0]
#     return last_name
#
# print(get_last_name('Иванов Иван Иванович'))

# time_in = datetime.datetime.now()
# time_out = time_in + datetime.timedelta(days=3)
# seconds = int((time_out - time_in).total_seconds() / 60)
#
#
# print(time_in)
# print(time_out)
# print(seconds)

# t = "Нехороший человек — редиска или полный чудак!"
t = 1

# @register.filter()
def censor(text):
    if isinstance(text, str):
        # список нежелательных слов
        cens_list = ['редиска', 'чудак']

        filter_text = re.split(r"\W", text)
        for word in filter_text:
            if word in cens_list:
                cens_word = word[0] + '*' * (len(word) - 1)
                text = text.replace(word, cens_word)
        return text
    else:
        print(f'Переменная {text} не может быть обработана, так как не является строкой :(')



print(censor(t))
