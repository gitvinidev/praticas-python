if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    listAll = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i<=x and j<=y and k<=z and i+j+k!=n]
    
    
    print(listAll)

