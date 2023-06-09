import re


def get_date_in_right_format(match):
    value1 = match.group(1).zfill(2)
    month = match.group(2).zfill(2)
    value3 = match.group(3).zfill(2)
    return f'{value1 if len(value1) != 4 else value3}.{month}.{value3 if len(value3) == 4 else value1}'


def search_year_in_text(filename: str):
    search_format = r'\b\d{3,4}\b'

    with open(filename, 'r', encoding='utf-8') as date_file:
        result = [(re.findall(search_format, text)[0], index_line) for index_line, text in enumerate(date_file, 1)]
    return sorted(result, key=lambda x: int(x[0]))


def text_to_sentences(filename: str):
    with open(filename, 'r', encoding='utf8') as text:
        result = text.read()
    result_list = re.findall(r'[^.!?]+[.!?]', result)
    return [i.replace('\n', '') for i in result_list]


if __name__ == '__main__':
    result = []
    with open('../../input/data_list.txt', 'r', encoding='utf-8') as file:
        for i in file.read().split('\n'):
            result.append(re.sub(r'(\d{1,2}|\d{4})[./](\d{1,2})[./](\d{4}|\d{1,2})', get_date_in_right_format, i))
    print(result)

    list_result = search_year_in_text('../../input/date.txt')
    print(list_result)

    sentences_list = text_to_sentences('../../input/text_about_programming.txt')
    print(sentences_list)
