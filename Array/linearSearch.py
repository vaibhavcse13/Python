"""
#problem statement 
Problem Statement:
Linear Search: Given an integer array and an element x, find if element is present in array or not. If element is present, then print index of its first occurrence. Else print -1.

Input:
First line contains an integer, the number of test cases ‘T’. Each test case should be an integer. Size of the array ‘N’ in the second line. In the third line, input the integer elements of the array in a single line separated by space. Element X should be inputted in the fourth line, i.e., after entering the elements of array. Repeat the above steps second line onwards for multiple test cases.

Output:
Print the output in a separate line returning the index of the element X. If the element is not present, then print -1.




"""

def linearSearch(arr , x , n):
    for j in range(0,n):
        if(arr[j] == x):
            return j;
    return -1;

#testcase 
t =  int(raw_input());

for i in range(0,t):
    
    #number of array element 
    n = int(raw_input());
    
    #input array
    arr = map(int , raw_input().split());
    
    #element to search 
    x = int(raw_input());
    
    print(linearSearch(arr , x , n));