
'''
Median of two sorted array if size of both arays is equal
'''
def median(A, B):

	fs = 0
	fe = len(A) - 1
	ss = 0
	se = len(B) - 1

	while fe - fs != 1 and  se - ss != 1:
		m1 = (fs + fe)/2

		m2 = (ss + se)/2 

		if B[m2] > A[m1]:
			fs = m1
			se = m2
		else:
			fe = m1 
			ss = m2 

	return float(max(A[fs], B[ss]) + min(A[fe], B[se]))/2

A = [1,2]
B = [4,5]

print median(A, B)