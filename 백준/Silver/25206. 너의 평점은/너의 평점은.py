grade = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
num = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
result = 0 
credit_total = 0
for _ in range(20):
    name, credit, rank = input().split()
    credit = float(credit)
    if rank != 'P':
        credit_total += credit
        result += credit*num[grade.index(rank)]
        
print(result/credit_total)
