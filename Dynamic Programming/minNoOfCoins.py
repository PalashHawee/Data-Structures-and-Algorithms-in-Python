#Min no of coins to make change
#Time O(nd) n is the target amount & d is the no of denominations
#Space O(n+1) n+1 is the length of num of coins array

def minNumberOfCoinsForChange(n, denoms):
    
    numOfCoins=[float("inf") for amount in range(n+1)]
	numOfCoins[0]=0
	for denom in denoms:
		for amount in range(len(numOfCoins)):
			if denom<=amount:
				numOfCoins[amount]=min(numOfCoins[amount], numOfCoins[amount-denom]+1)
	return numOfCoins[n] if numOfCoins[n]!=float("inf") else -1