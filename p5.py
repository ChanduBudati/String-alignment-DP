#!/usr/bin/env python3

import sys
import math


def main():
	str1 = input().strip().strip('\n')
	str2 = input().strip().strip('\n')
	match_value = 5#int(sys.argv[1])
	mismatch_penality = -4#int(sys.argv[2])
	gap_penality = -8#int(sys.argv[3])
	up = 0
	left = 1
	diag = 2

	M = len(str1)+1
	N = len(str2)+1
	
	#initialization
	Brd = [[(0,2) for i in range(M)] for j in range(N)]
	for i in range(N):
		Brd[i][0] = (0, 0)
	for i in range(N):
		Brd[0][i] = (0, 1)

	#matrix fill
	for i in range(1,N):
		for j in range(1,M):
			if(str1[j-1] == str2[i-1]):
				score = match_value
			else:
				score = mismatch_penality
			tval = max((Brd[i-1][j-1][0] + score),(Brd[i][j-1][0] + gap_penality), (Brd[i-1][j][0] + gap_penality))
			if tval == (Brd[i-1][j-1][0] + score):
				tbk = 2
			elif tval == (Brd[i][j-1][0] + gap_penality):
				tbk = 1
			else:
				tbk = 0

			Brd[i][j] = (tval,tbk)
					

	#traceback
	j = M-1

	i = N-1
	astr1 = ''
	astr2 = ''
	while(True):
		if (i == 0 and j == 0):
			break

		if (Brd[i][j][1] == 2):
			astr1 = str1[j-1]+astr1
			astr2 = str2[i-1]+astr2
			i = i-1
			j = j-1
		elif(Brd[i][j][1] == 1):
			astr1 = str1[j-1]+astr1
			astr2 = "_" +astr2
			j = j-1
		else:
			astr1 = "_" +astr1
			astr2 = str2[i-1]+astr2
			i = i-1
			
	
	print(astr1)
	print(astr2)
main()
