calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


calls -= 1

calls = count_calls()


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


print(string_info('Cheetos'))
print(string_info('ChesTER'))


def is_contains(string, list_to_search):
    count_calls()
    return string.casefold() in list_to_search


print(is_contains('Coco', ['My'.casefold(), 'Dear'.casefold(), 1, 55, 'CocO'.casefold()]))
print(is_contains('Coconut', ['My'.casefold(), 'Dear'.casefold(), 1, 55, 'CocO'.casefold()]))

print(calls)
