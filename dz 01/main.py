"""Задача 1. На вход программе подаются два массива целых чисел. Необходимо
найти число вхождений второго массива в первый. То есть посчитать, сколько
раз последовательность чисел второго массива (без перестановок) встречается
в первом.
_________________________________Решение"""
def find_occurence(list1: list, list2: list) -> dict:
    occurrence = {}
    for i in list1:
        if i in list2:
            occurrence[i] = occurrence.get(i, 0) + 1
    return occurrence

def main():
    list1 = [1, 2, 3, 3, 3, 4, 4, 7, 8, 9, 1]
    list2 = [1, 3, 4, 8, 9]
    print(find_occurence(list1, list2))
if __name__ == "__main__":
    main()