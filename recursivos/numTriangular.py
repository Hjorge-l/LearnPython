def numTriangular(n):
    print("Número triangular de",n,"=", int(n*(n+1)/2))

def numTriangularRecursivo(n):
    suma = n
    if n == 0:
        return 0
    else:
        suma += numTriangularRecursivo(n-1)
        return suma        

def main():
    print("--Versión normal--")
    numTriangular(4)
    numTriangular(13)
    print("--Versión recursiva--")
    print("::",numTriangularRecursivo(4))
    print("::",numTriangularRecursivo(13))

main()