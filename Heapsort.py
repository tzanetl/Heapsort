# Taneli Leppanen
# ALgorithms for Engineering Informatics
# Task 1 - Heapsort

# For sorting a list of integers

# Sources
# 1) http://www.geekviewpoint.com/python/sorting/heapsort
# 2) https://en.wikipedia.org/wiki/Heapsort


import random


def test():
    # Length of the test list
    length = 10
    # Range of random integers a <= N <= b
    a = 1
    b = 20

    lst = generateList(length, a, b)

    print(lst)
    heapsort(lst)
    print(lst)


def heapsort(lst):

    if len(lst) == 0:
        print("List is empty")
        return
    elif len(lst) == 1:
        return

    heapify(lst)

    if len(lst) == 2:
        return

    toSortedList(lst)


# Swaps the first item with the last item and adds it to the res -list
# Afterwards the list made into a heap
# Loops for the length of the list
def toSortedList(lst):
    res = []
    l = len(lst)
    for i in range(l):
        swap(lst, 0, len(lst) - 1)
        res.append(lst.pop(len(lst) - 1))
        heapify(lst)

    lst += res


# Makes the list into a heap
def heapify(lst):

    for i in range(int(len(lst)/2) - 1, -1, -1):
        shiftdown(lst, i, len(lst) - 1)


# Moves the member of the heap into the correct positon
def shiftdown(lst, parent, last):
    # Position of largest biggest child
    # Initially set as the left child
    lpos = parent * 2 + 1

    while lpos <= last:
        # Checking if right child exitst and if it's bigger than left child
        if (lpos < last) and (lst[lpos] < lst[lpos + 1]):
            lpos += 1

        # Checking if the bigger child is bigger than the parent
        # and swapping their positions if True
        if lst[lpos] > lst[parent]:
            swap(lst, lpos, parent)
            # The swapped member is set as the new parent and the process is
            # repeated to check if it is in the right place
            parent = lpos
            lpos = parent * 2 + 1

        # If heap condition is satisfied return is called
        else:
            return


# Swaps positions of 2 items in list
def swap(lst, a, b):
    tempList = lst[a]
    lst[a] = lst[b]
    lst[b] = tempList


# Reads the file into a list
def reader(file_name):
    try:
        file = open(file_name, 'r')
        lst = []

        for line in file:
            line = line.strip()

            if line == "":
                continue

            lst.append(int(line))

        file.close()
        return lst

    except IOError:
        print("Error while trying to open the file")
        return None

    except FileNotFoundError:
        print("File \"" + file_name + "\" not found")
        return None

    except ValueError:
        print("Cannot convert \"" + line + "\" to integer")
        file.close()
        return None


def generateList(length, a, b):
    lst = []

    for i in range(length):
        lst.append(random.randint(a, b))

    return lst

test()
