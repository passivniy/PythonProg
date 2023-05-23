from import_modules.validator import set_value
import textwrap

print('IKM-221D Task_6')
print('Lytvynov Danyil')


def read_and_write(inp_filename: str, out_filename: str):
    summ = int()
    with open(inp_filename, 'r') as inp_param:
        for line in inp_param:
            summ += int(line)
    with open(out_filename, 'w') as out_summ:
        out_summ.write(str(summ))
    return 'Completed.'


def even_or_odd(out_filename: str):
    x = set_value(int)
    with open(out_filename, 'w') as out:
        out.write('Even' if x % 2 == 0 else 'Odd')
    return 'Completed'


def read_sentence_about_py(filename: str):
    with open(filename, 'r') as inpSentence:
        sentence_list = inpSentence.read()
    print(sentence_list)
    return sentence_list

def greeting_to_file(filename: str):
    name = 'Name'
    while name:
        name = str(input('Enter name for greeting in file: '))
        if not name:
            break
        with open(filename, 'a') as hello:
            hello.write('Hi,' + name + '\n')
        print('Hi,', name)
    return 'Completed'


def the_in_text(filename: str):
    with open(filename, 'r') as book:
        string_book = book.read()
    return sum(string_book.count(item) for item in ['The', 'the'])


def book(filename: str, outpfilename: str):
    with open(filename, 'r', encoding='utf8') as book_for_read:
        reading_result = book_for_read.read()

    with open(outpfilename, 'w', encoding='utf8') as book_for_write:
       book_for_write.write(textwrap.fill((reading_result.replace('\n', '')), width=120))
    return 'Complete'


if __name__ == '__main__':
    '''
    print(read_and_write('input/numbers.txt', 'output/sum_numbers.txt'))
    
    print(even_or_odd('output/typeOfNumber.txt'))
    
    sentence_list = read_sentence_about_py('../../input/learning_python.txt')
    
    print(sentenceList.replace('Python', 'C'))

    print(greeting_to_file('../../output/guest_book.txt'))

    print(the_in_text('../../input/book.txt'))
    '''
    print(book('../../input/book.txt', '../../output/book_out.txt'))
