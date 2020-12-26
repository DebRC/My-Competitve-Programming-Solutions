def decimalToBinary(n):  
    return bin(n).replace("0b", "")
def binaryToDecimal(n): 
    return int(n,2)
n=int(input())
bin_n=list(decimalToBinary(n))
bin_n.reverse()
bin_n="".join(bin_n)
print(binaryToDecimal(bin_n))