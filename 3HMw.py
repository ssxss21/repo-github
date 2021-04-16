#task 1
eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven': 'семь',
    'eight' : 'восемь',
    'nine': 'девять',
}

def num_translate(eng_word):
    return eng_rus_dict.get(eng_word)

print(num_translate('six'))

#task 2

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven': 'семь',
    'eight' : 'восемь',
    'nine': 'девять',
}
def num_translate(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return eng_rus_dict[eng_word].capitalize()
    else:
        return eng_rus_dict[eng_word]

    print(num_translate_adv('six'))
    print(num_translate_adv('Six'))


#task 3
    def thesaurus(name):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0],[])
        out_dict[name[0]].append(name)
    return out_dict

print(thesaurus("Иван","Мария","Петр","Илья"))


#task 5


import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    joke_list = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
        return joke_list

print(get_jokes(1))
print(get_jokes(2))