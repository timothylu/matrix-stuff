import numpy as np

# returns the row with the lowset sum in "mat"
def min_row(mat):
	min_row = mat[0]
	#print("first row sum: " + str(min_row.sum()))
	for row in mat:
		temp = row.sum()
		if temp < min_row.sum():
			#print("new min: " + str(temp))
			min_row = row
	return min_row

if __name__ == "__main__":
	pass