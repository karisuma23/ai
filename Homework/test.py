n = int(input('3 or 5 이상 1000 이하의 정수를 입력하시오'))
list3 = []
list5 = []
for i in range(1,n+1):
   if i%3 == 0: 
       list3 = i 
   for j in range(1,n+1):    
    if j%5 ==0:
       list5 = j

       print(list3)
       print(list5)
       
       