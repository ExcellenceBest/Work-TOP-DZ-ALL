import re
def find_occurences(list1: list, list2: list) -> int:
    str1 = ','.join([str(i) for i in list1])
    str2 = ','.join([str(i) for i in list2])
    count = []
    for i in re.finditer(str2, str1):
        count.append(i.end())
    occurences = len(count)
    return occurences

list1 = [1, 1, 2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 1, 3, 1, 2, 3, 1, 2, 3, 9, 1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 1, 3, 4, 1, 1, 3, 1, 1, 4]
list4 = [1, 1]
def main():
    ...
if __name__ == '__main__':
    main()