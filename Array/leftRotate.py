
"""
	Rotate the array element 
	arr =  [1,2,3,4,5,6,7] 
	d = 2 
	left rotate [3,4,5,6,7,1,2]
	right rotatte [6,7,1,2,3,4,5]

"""

"""
	using temp array 
	Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]
   Time complexity O(n)
Auxiliary Space: O(d)
	
"""
def usingTempArray(arr , d , n ):

	temp = arr[0:d];

	for i in range(0 , n -d ):
		arr[i] = arr[d+i];

	for i in range(0,d):
		
		arr[n-d +i] = temp[i]

# rotate one by one T - O(n*d)  S - O(1))
"""
To rotate by one, store arr[0] in a temporary variable temp, move arr[1] to arr[0], arr[2] to arr[1] …and finally temp to arr[n-1]

Let us take the same example arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
Rotate arr[] by one 2 times
We get [2, 3, 4, 5, 6, 7, 1] after first rotation and [ 3, 4, 5, 6, 7, 1, 2] after second rotation.

Implementation:

"""
def leftRotate(arr , d , n ):

	for i in range(d):
		#leftRotateByOne(arr , n);
		rightRotateByOne(arr , n )


def leftRotateByOne(arr , n):
	temp = arr[0];
	for i in range(n-1):
		arr[i]= arr[i+1];
	arr[n-1] = temp ;

def rightRotateByOne(arr , n):
	temp = arr[n-1];
	for i in range(n-1 ,0 ,-1 ):
		arr[i] =  arr[i-1];
	arr[0] = temp;

def printArray(array , size):
	for i in range(0 , size):
		print("%d"% array[i],end =" ");


"""
juggling algorith 

"""

def gcd(a , b ):
	if b == 0 :
		return a;
	else:
		return  gcd(b , a%b);

def leftRotateJug(arr, d , n):
	for i in range(0 , gcd(n,d)):
		temp = arr[i];
		j=1 
		while 1:
			k= j+n ;
			if k >= n :
				k = k-n;
			if k == i :
				break;
			arr[j] =arr[k];
			j=k;
		arr[j] = temp;

    
array = [1,2,3,4,5,6,7];
#array2 =[10,20,30,40,50,60,70,80,90,100];
# leftRotate(array , 2 , 7);
# printArray(array , 7);
# d =  3 % 10
#leftRotate(array2 , 3 , 10);
# print('\n');
leftRotateJug(array , 2 , 7);
printArray(array , 7);




# using temp array 




