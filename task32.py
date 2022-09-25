  
def mult(a,b):
    for i in range(1, a+1):
     for j in range(i, i*b+1, i):
         print(j, end='\t')
     print()
   
def sum(a,b):
    for i in range(0, a+1):
     for j in range(0, b+1):
         print(j+i, end='\t')
     print()
def degree(a,b):
    for i in range(1, b+1,1):
        print(i, end='\t')
    print()    
    for i in range(2, a+1):
     for j in range(1, b+1):
         print(i**j, end='\t')
     print()
def print_operation_table(operation,num_rows,num_columns): 
    if operation==1:
        mult(num_rows,num_columns)
    elif operation==2:
        sum(num_rows,num_columns)
    elif operation==3:
        degree(num_rows,num_columns)
   
choise=int(input('Укажите какую таблицу вы хотите задать\n1-таблица умножения\n2-таблица сложения\n3-таблица возведения в степень\n'))
num_rows=int(input('Введите количество строк'))
num_columns=int(input('Введите количество столбцов'))
print_operation_table(choise,num_rows,num_columns)