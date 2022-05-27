# Array of Products

#Time O(n) | Space O(n)


def arrayOfProducts(array):
    # Write your code here.
    products=[1 for _ in range(len(array))]
    leftProducts=[1 for _ in range(len(array))]
    rightProducts=[1 for _ in range(len(array))]

    leftRunningProduct=1
    for i in range(len(array)):
        leftProducts[i]=leftRunningProduct
        leftRunningProduct*=array[i]

    rightRunningProduct=1
    for i in reversed(range(len(array))):
        rightProducts[i]=rightRunningProduct
        rightRunningProduct*=array[i]

    for i in range(len(array)):
        products[i]=leftProducts[i]*rightProducts[i]
    return products    
