while True:
    n = int(input())
    if n == -1:
        break
    else:
        total = 0
        for i in range(1,n):
            if n % i == 0:
                total += i
            
        if total == n:
            print(f"{n} =",end =" ")
            for i in range(1,n):
                if n % i == 0:
                    print(i, end=" ")
                    if i == n//2 :
                        break
                    else:
                        print("+", end=" ")
        else:
            print(f"{n} is NOT perfect.")

    

     