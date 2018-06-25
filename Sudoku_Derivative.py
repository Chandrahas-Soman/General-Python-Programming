'''
Problem Statement: Write a program that checks whether an unsolved sudoku puzzle is in fact derived from an 
earlier puzzle by siimple operations.

The allowed operations are:

1. Rotating the entire puzzle clockwise or counter-clockwise.
2. Swapping two columns within a 3 * 9 column segment.
3. Swapping two rows within a 9 * 3 row segment.
4. Swapping entire 9 * 3 row or 3 * 9 column segment.

An operation is considered being performed on the sudoku solution (rather than on the unsolved puzzle) and 
always guarantees that if board if the board before transformation was a solution to a sudoku puzzle, it still
is afterwards.


Input:

The input starts with the number of test cases 0 <= N <= 50 on a single line.

Then for every test case follow nine lines describing last week's puzzle solution, from top to bottom. Each
line corresponds to a row in the puzzle and consists of nine digits(1,..,9), describing the contents of the cell
from left to right.

Last week's solution is followed by nine lines describing this week's unsolved puzzle. Here, also, every line
corresponds to a puzzle row and every digit (1,..,9) describes the contents of the cell. 0 indicates that the cell 
is empty. The rowa are presented ordered from top to bottom, and within each row, the cells are orederd from
left to right.

After every test case except the last one follows a blank line. Every unsolved puzzle is guarnteed to be uniquely 
solvable and last week's solution is always a proper sudoku solution.


Output:

For every test case, output "Yes" if the sudoku puzzle can be derived from the given solved puzzle using the
allowed operations, or "No" if this is not possible.

'''

import sys

def rotate_clk(mat):

	mat = list(list(x)[::-1] for x in zip(*mat))

	return mat


# possible row values = 1,2,3
# possible rs values = 1,2,3
def row_swap_within_row_segment(mat,r1,r2,row_seg):
	
	temp = (row_seg - 1)*3 - 1
	mat[r1 + temp], mat[r2 + temp] = mat[r2 + temp], mat[r1 + temp]
	
	return mat


# possible col values = 1,2,3
# possible cs values = 1,2,3
def col_swap_within_col_segment(mat,c1,c2,col_seg):
	
	temp = (col_seg - 1)*3 - 1
	
	for k in range(0,9):
		mat[k][c1 + temp], mat[k][c2 + temp] = mat[k][c2 + temp], mat[k][c1 + temp]
	
	return mat
	'''
	mat = row_swap_within_row_segment(zip(*mat),c1,c2,col_seg)

	return zip(*mat)
	'''

# possible rs values = 1,2,3
def swap_row_segment(mat,rs1,rs2):

	seg1 = (rs1 - 1)*3
	seg2 = (rs2 - 1)*3

	for k in range(0,3):
		mat[seg1 + k], mat[seg2 + k] = mat[seg2 + k], mat[seg1 + k]

	return mat


# possible cs values = 1,2,3
def swap_col_segment(mat,cs1,cs2):

	seg1 = (cs1 - 1)*3
	seg2 = (cs2 - 1)*3

	for l in range(0,9):
		for k in range(0,3):
			mat[l][seg1 + k], mat[l][seg2 + k] = mat[l][seg2 + k], mat[l][seg1 + k]

	return mat


 
def is_match(yest,today_NZ):

	match = True
	
	for p in today_NZ:
		i = p[0]
		j = p[1]
		val = p[2]
		
		if int(yest[i][j]) != val: 
			match = False 
			break

	return match


'''
def is_partial_row_match(yest,today_NZ,rs):

	partial_row_match = True

	for p in today_NZ:
		i = p[0]
		j = p[1]
		val = p[2]

		start = (rs-1)*3
		end = rs*3
			if i in range(start,end):		
				if int(yest[i][j]) != val: 
					partial_row_match = False 
					break

	return partial_row_match


def is_partial_col_match(yest,today_NZ,cs):

	partial_col_match = True

	for p in today_NZ:
		i = p[0]
		j = p[1]
		val = p[2]

		#start = (cs-1)*3
		#end = cs*3
		
		if j == (cs-1)*3:	
			if int(yest[i][j]) != val: 
				partial_col_match = False 
				break

	return partial_col_match
'''


def populate_sudoku(index):
	
	mat = []
	row = []

	for j in range(0,9):
		for k in range(0,9):
			row.append(argument_list[index+j][k])
		mat.append(row)
		row = []
	
	return mat



argument_list = []

#for x in sys.stdin:
#	argument_list.append(x[:-1])

argument_list = ['2',
'963174258','178325649','254689731',
'821437596','496852317','735961824',
'589713462','317246985','642598173',
'060104050','200000001','008305600',
'800407006','006000300','700901004',
'500000002','040508070','007206900',
'',
'534678912','672195348','198342567',
'859761423','426853791','713924856',
'961537284','287419635','345286179',
'010900605','025060070','870000902',
'702050043','000204000','490010508',
'107000056','040080210','208001090']



n = argument_list[0]
j = 1
yesterday = []
today = []
today_NZ = []
match_found = False

for i in range(0,int(n)):

	yesterday = populate_sudoku(j)
	j = j + 9 
	today = populate_sudoku(j)

	for p in range(0,9):
		for q in range(0,9):
			if int(today[p][q]) != 0:
				today_NZ.append([p,q,int(today[p][q])])

	original = yesterday[:]

	segments = [[0,0],[1,2],[1,3],[2,3]]

	for cses in range(0,4):
		yesterday = original[:]						
		D = swap_col_segment(yesterday,segments[cses][0],segments[cses][1])
		for col_seg_counter_outer in range(1,3):
			for cses_inner in range(0,4):
				yesterday = D[:]
				E = col_swap_within_col_segment(yesterday,segments[cses_inner][0],segments[cses_inner][1], col_seg_counter_outer)
				'''
				if is_partial_col_match(yesterday,today_NZ,col_seg_counter_outer):
					pass
				else:
					continue
				'''
				for col_seg_counter_inner in range(2,4):
				
					if col_seg_counter_inner <= col_seg_counter_outer:
						continue
					else:
						for cses_inner_in in range(0,4):
							yesterday = E[:]
							F = col_swap_within_col_segment(yesterday,segments[cses_inner_in][0],segments[cses_inner_in][1],col_seg_counter_inner)

							for rses in range(0,4):
								yesterday = F[:]					
								A = swap_row_segment(yesterday,segments[rses][0],segments[rses][1])
								for row_seg_counter_outer in range(1,3):
									for rses_inner in range(0,4):
										yesterday = A[:]
										B = row_swap_within_row_segment(yesterday,segments[rses_inner][0],segments[rses_inner][1], row_seg_counter_outer)
										'''
										if is_partial_row_match(yesterday,today_NZ,row_seg_counter_outer):
											pass
										else:
											continue
										'''
										for row_seg_counter_inner in range(2,4):
											if row_seg_counter_inner <= row_seg_counter_outer:
												continue
											else:
												for rses_inner_in in range(0,4):
													yesterday = B[:]
													C = row_swap_within_row_segment(yesterday,segments[rses_inner_in][0],segments[rses_inner_in][1],row_seg_counter_inner)

													for rotation in range(0,4):
														match_found = is_match(yesterday,today_NZ)

														if match_found:
															break
														else:
															G = rotate_clk(yesterday)
															yesterday = G[:]
													if match_found:
														break

											if match_found:
												break

										if match_found:
											break

									if match_found:
										break

								if match_found:
									break								

							if match_found:
								break

					if match_found:
						break

				if match_found:
					break

			if match_found:
				break

		if match_found:
			break				


	if match_found:
		sys.stdout.write('Yes')
	else:
		sys.stdout.write('No')
	sys.stdout.write('\n')
	j = j + 10
	yesterday = []
	today = []
	today_NZ = []
	match_found = False

