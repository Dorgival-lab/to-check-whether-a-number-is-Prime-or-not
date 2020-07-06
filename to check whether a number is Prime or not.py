# Programa Python para verificar se
# o número fornecido é primo ou não 
  
num = 11
  
# Se um número determinado for maior que 1 
if num > 1: 
      
   # Iterar de 2 para n / 2  
   for i in range(2, num): 
         
       # Se num é divisível por qualquer número entre  
       # 2 en / 2, não é primo  
       if (num % i) == 0: 
           print(num, "não é um número primo") 
           break
   else: 
       print(num, "é um número primo") 
  
else: 
   print(num, "não é um número primo")