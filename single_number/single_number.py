'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    no_dups = []
    # interate through nums
    for x in arr:
        # check to see if the number is already in the `no_dups` array
        if x not in no_dups:
            no_dups.append(x)
        # if it is, remove it from the `no_dups` array
        else:
            no_dups.remove(x)
    # when we're done iterating, the only number in our `no_dups` array is the 
    # odd number out
    # return it
    return no_dups[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")