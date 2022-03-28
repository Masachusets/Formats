import json
from from xml.dom import minidom


def words_longer_than_6_json(file):
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    lst_news = data['rss']['channel']['items']
    lst = []
    for new in lst_news:
        lst += filter(lambda x: len(x) > 5, new['description'].split())
    return lst

def top_ten(lst: list) -> dict:
    word_count = {}
    for word in lst:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    top = {}
    for word, num in word_count.items():
        if num not in top:
            top[num] = [word]
        else:
            top[num] += [word]
    return top


def output(dic: dict):
    i = 1
    for num in sorted(dic, reverse=True)[:10]:
        word = ''.join(dic[num])
        print(f'{i} место: слово(слова) \'{" ".join(dic[num])}\' - {num} раз(а)')
        i += 1


#print(words_longer_than_6('newsafr.json'))
output(top_ten(words_longer_than_6_json('newsafr.json')))
