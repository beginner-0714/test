print('--369 게임--')
num = int(input('1부터 어디까지 진행할까요?: '))
for num in range(1,num+1):
    if(num%3==0):
        print('짝',end = ' ')
    print(num,end = ' ')
