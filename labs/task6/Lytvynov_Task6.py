from import_modules.validator import set_value
import textwrap

print('IKM-221D Task_6')
print('Lytvynov Danyil')


#Цикл в комрехеншен [], открытие в 1 файл
def read_and_write(inp_filename: str, out_filename: str):
    summ = int()
    with open(inp_filename, 'r') as inp_param:
        for line in inp_param:
            summ += int(line)

    with open(out_filename, 'w') as out_summ:
        out_summ.write(str(summ))


def even_or_odd(out_filename: str):
    x = set_value(int)
    with open(out_filename, 'w') as out:
        out.write('Odd' if x % 2 else 'Even')


#Добавить построковое считывание и вывести в цикле каждое предложение
def read_sentence_about_py(filename: str):
    with open(filename, 'r') as inpSentence:
        sentence_list = inpSentence.read()
    print(sentence_list)
    return sentence_list


def greeting_to_file(filename: str):
    name = None
    with open(filename, 'a') as hello:
        while not name:
            name = input('Enter name for greeting in file: ')
            hello.write('Hi,' + name + '\n')
            print('Hi,', name)


def the_in_text(filename: str):
    with open(filename, 'r') as book:
        return book.read().lower().count('the')


def book(filename: str, outpfilename: str):
    with open(filename, 'r') as book_for_read:
        reading_result = book_for_read.read()

    with open(outpfilename, 'w', encoding='utf8') as book_for_write:
        book_for_write.write(textwrap.fill((reading_result.replace('\n', '')), width=120))


if __name__ == '__main__':
    '''
    print(read_and_write('input/numbers.txt', 'output/sum_numbers.txt'))

    print(even_or_odd('output/typeOfNumber.txt'))

    sentence_list = read_sentence_about_py('../../input/learning_python.txt')

    print(sentence_list.replace('Python', 'C'))

    print(greeting_to_file('../../output/guest_book.txt'))

    print(the_in_text('../../input/book.txt'))

    print(book('../../input/book.txt', '../../output/book_out.txt'))
    '''
    print(book('../../input/book.txt', '../../output/book_out.txt'))