'''
this method is working for find an element in 2D matrix
Approch:

	first find the sutable row for particular taret value with the help for binary search then
	second implement sprate binaryserach for find element in partcular coloum

'''

def searchElementInMatrix(matrix:list[list[int]],target: int) -> bool:
	ROWS,COLS = len(matrix),len(matrix[0])

	topRow ,botRow = 0, ROWS-1

	while topRow<=botRow:
		row = (topRow+botRow)//2

		if target > matrix[row][-1]:
			topRow = row + 1

		elif target < matrix[row][0]:
			botRow = row - 1

		else:
			break

	if not(topRow<=botRow):
		return False

	row = (topRow+botRow) // 2

	leftPoint,rightPoint = 0,COLS-1

	if leftPoint<=rightPoint:
		mid = (leftPoint+rightPoint) // 2

		if target > matrix[row][mid]:
			leftPoint = mid+1

		elif target<matrix[row][mid]:
			rightPoint = mid-1

		else:
			return True

	return False


matrix = [[1 , 3 , 5 , 7],[ 10 ,11 , 16 , 20],[ 23 , 30 , 34 , 60]]
target = 5

print(searchElementInMatrix(matrix,target))


