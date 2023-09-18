'''
All values were encrypted as 
a->1, b->2, c->3, d->4, ..., z->26
Then we can determine how many different
people would be killed by interpreting this 
in as many ways as possible. 
'''
letter_conversions = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7,
                      "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, 
                      "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
                      "t":20, "u":21, "v":22, "w":23, "x":24, "y":25,
                      "z":26}

def calculate_combs(input:str):
    # default combination
    invalid = {"7", "8", "9"}
    num_combs = int(1)
    for i in range(len(input)):
        if (input[i] == "1" or input[i] == "2") and (len(input) > i+1) and (input[i+1] not in invalid):
            # add a combination for every 1 or 2 in the sequence
            num_combs += 1
    print(num_combs)

def main():
    string = input()
    calculate_combs(input=string)

if __name__ == "__main__":
    main()