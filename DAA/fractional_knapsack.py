from timeit import default_timer as timer

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, arr):

    arr.sort(key = lambda x : (x.value/x.weight), reverse = True)

    finalvalue = 0.0

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value

        else:
            finalvalue += item.value * W / item.weight
            break

    return finalvalue


if __name__ == "__main__":

    W = int(input("Enter Maximum Wieght : "))
    n = int(input('Enter number of items: '))
    VAL = input('Enter the values of the {} item(s) in order: '.format(n)).split()
    VAL = [int(v) for v in VAL]
    WT = input('Enter the positive weights of the {} item(s) in order: '.format(n)).split()
    WT = [int(w) for w in WT]
    arr = []
    for x, y in zip(VAL, WT):
        arr.append(Item(x, y))

    max_val = fractionalKnapsack(W, arr)
    print(max_val)