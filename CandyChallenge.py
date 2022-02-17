
    
    
    
def step(test):
    M=list(map(int,input().split()))
    candy =list(map(int,input().split()))
    tot_candy=0
    count=0
    remain=0
    for i in range(len(candy)):
        count = candy[i]
        tot_candy +=count
        
    remain = tot_candy%M[1]
    
    
    



total_case = input()
for j in range(int(total_case)):
    step(j)
