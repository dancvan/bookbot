import string


def main():
    book_loc = 'books/frankenstein.txt'
    with open(book_loc) as f:
        file_contents = f.read()
        words = file_contents.split()
        alphdict, alphlist = create_alphabet_dict()
        for word in words:
            alphdict = count_letters(word, alphdict, alphlist)
    sorted_dict = sorted_by_count(alphdict)
    print_report(words,sorted_dict)
    

def sorted_by_count(alph_dict):
    return {k: v for k, v in sorted(alph_dict.items(), reverse=True, key=lambda item: item[1])}

def create_alphabet_dict():
    alphabet = list(string.ascii_lowercase)
    alphabet_dict = {}
    for letter in alphabet:
        alphabet_dict[letter] = 0
    return alphabet_dict, alphabet

def count_letters(str_input, alph_dict, alph_list):
    lowercase_string = str_input.lower()
    for letter in lowercase_string:
        if letter in alph_list:
            alph_dict[letter] += 1
    return alph_dict

def print_report(words,sorted_dictionary):
    print('-- Begin report of books/frankenstein.txt --')
    print('{} words found in the document'.format(len(words)))
    for letter in sorted_dictionary:
        print("The '{}' character was found {} times".format(letter, sorted_dictionary[letter])) 
    print('-- End report --')
main()
