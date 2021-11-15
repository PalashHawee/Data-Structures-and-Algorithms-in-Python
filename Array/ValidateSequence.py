#Validate Sequence
#Time O(N) N is the length of the array
#Space O(1)
def isValidSubsequence(array, sequence):
   
    arrIdx=0
	seqIdx=0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx]==sequence[seqIdx]:
			seqIdx+=1
		arrIdx+=1
	return seqIdx==len(sequence)	
#Time O(N) N is the length of the array
#Space O(1)
#Using for loop
def isValidSubsequence(array, sequence):
    
    seqIdx=0
	for value in array:
		if seqIdx==len(sequence):
			break
		if sequence[seqIdx]==value:
			seqIdx+=1
	return seqIdx==len(sequence)		
