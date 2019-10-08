# This problem was taken from hackerrank


def reverseArray(a):
    # reverse the array
    rev = a[::-1]

    # Converting the list to a string then joinin the letters on a space
    print(' '.join(map(str, rev)))

    # returning it for the hackerrank solution
    return ' '.join(map(str, rev))

# testing my solution
arr = [1, 5, 6, 7, 8, 92]
reverseArray(arr)
