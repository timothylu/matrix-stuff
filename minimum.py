import numpy as np

# returns the row with the lowset sum in "mat"
def min_row(idx, mat):
	min_row = mat[0]
	min_idx = idx[0]
	#print("first row sum: " + str(min_row.sum()))
	
	count = 0

	for row in mat:
		temp = row.sum()
		if temp < min_row.sum():
			#print("new min: " + str(temp))
			min_row = row
			min_idx = idx[count]
		count += 1
	return min_idx, min_row

if __name__ == "__main__":
	pass