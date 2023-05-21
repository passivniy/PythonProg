from labs.task11.Lytvynov_Task11 import search_date_group, date_in_right_format, search_year_in_text, text_to_sentences


def test_for_search_year_in_text():
    input_param = '../input/date2.txt'
    actual = search_year_in_text(input_param)
    expected = [('1492', 2), ('1789', 3), ('1969', 1)]
    assert actual == expected


def test_for_text_to_sentences():
    input_param = '../input/text_.txt'
    actual = text_to_sentences(input_param)
    expected = [
        'Программирование - это процесс создания программного кода для выполнения определенных задач компьютером.',
        'Языки программирования, такие как Python, Java и C++, позволяют разработчикам создавать сложные программы'
        ' понятнымобразом для компьютеров.']
    assert actual == expected