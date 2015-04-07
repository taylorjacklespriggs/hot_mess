from random import shuffle

def bogo(lst):
    while not all(l[i] <= l[i+1] for i in range(len(l) - 1)):
        shuffle(lst)

if __name__ == '__main__':
    lst = shuffle(range(100))
    print 'Shuffled:', lst
    bogo(lst)
    print 'Ordered by bogo:', lst

