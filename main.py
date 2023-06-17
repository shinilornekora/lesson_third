#  Дана строка n. Вывести количество каждого символа в ней.
#
# 'aabbbcccdd' -> a 2 b 3 c 3 d 2
#  O(N**2), O(N * M), O(N)
#  16 M - количество уникальных символов в строке 4M  4
#  O(4 * N**2) -> O(N**2), O(log(N + 4)) -> O(log(n))


# Данный алгоритм работает со сложностью O(N**2).
def strCounter__first(string: str):
    for symbol in string:
        counter = 0
        for sub_symbol in string:
            if sub_symbol == symbol:
                counter += 1
        print(symbol, counter)


# Данный алгоритм работает со сложностью O(N * M)
def strCounter__second(string: str):
    for symbol in set(string):
        counter = 0
        for sub_symbol in string:
            if sub_symbol == symbol:
                counter += 1
        print(symbol, counter)


# Данный алгорнитм работает за O(N) hashmaps
def strCounter__third(string: str):
    symbols = {}
    for symbol in string:
        symbols[symbol] = symbols.get(symbol, 0) + 1
    return symbols


#  Leetcode, Codewars
print(strCounter__third('aabbbcccdd'), end='\n\n')
