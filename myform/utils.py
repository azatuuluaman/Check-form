import re


def type(one):
    test = {'email': 'moiemail',
            'number': '606060606060',
            'date': 44,
            'text': 'moitext',
            }

    for two, three in test.items():
        if re.fullmatch(three, one):
            return two

    return 'text'


def type_form(four):
    res = {}
    four = four.dict()
    for five, six in four.items():
        res[five] = type()
