N, K = map(int,input().split())
divisor_list = []
for i in range(1,N//2+1):
    if N % i == 0:
        divisor_list.append(i)
divisor_list.append(N)
if K > (len(divisor_list)):
    print(0)
else:
    print(divisor_list[K-1])