'''
Suppose you are in a number system, where if 
the number doesn't contain 2 in the unit digit then 
the number is not valid. So the first number of the
system is 2, the second number is 12, and the third
is 22. For a given integer, n, you have to print the 
nth element of the number system

Input format: 
- First line, containing n denoting the number of
test cases. 
- n number of lines for the query

Output Format:
- Print the consecutive number in the number system
for each query

Sample Input:
- 3

Sample Output
- 22

Explanation: 
the first number will be 2, 2nd number will be 12
and the third number will be 22.
'''

def print_value(test_case:int):
    multiplier = test_case - 1
    print(10*multiplier + 2)

def handle_input():
    '''
    Grabs input test cases and returns it to main
    
    Arguments:
    - None
    
    Returns
    - `List` of test cases
    '''
    num_test_cases = int(input())
    test_cases = []

    for i in range(num_test_cases):
        cur_tc = int(input())
        test_cases.append(cur_tc)

    return test_cases

def main():
    test_cases = handle_input()

    for test_case in test_cases:
        print_value(test_case)

if __name__ == "__main__":
    main()