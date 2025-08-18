# Lidando com números
numero1 = 10 # tipo inteiro
numero2 = 5.6 # tipo float
numero3 = 5 + 2j
'''
There are three distinct numeric types: 
integers, floating-point numbers, 
and complex numbers.
'''
numero4 = int(numero2)
isinstance(numero1,object) # True
isinstance(numero1,int) # True
isinstance(numero1,float) # False

isinstance(numero2,object) # True
isinstance(numero2,int) # False
isinstance(numero2,float) # True

isinstance(numero3,object) # True
isinstance(numero3,int) # False
isinstance(numero3,float) # False
#######################################
# Faça um programa que receba dois números inteiros 
# e realize a soma dos dois números
valor1 = input('Digite o primeiro número')
valor1 = int(valor1)

valor2 = int(input('Digite o segundo número'))

valor3 = valor1 + valor2
print(valor3)
#######################################
'''
Textual data in Python is handled with 
str objects, or strings. 
Strings are immutable sequences 
of Unicode code points. 
'''
s = 'Fatec Araras'
print(s.upper())

# Strings são iteráveis.

###########################################
# Dada uma string s, mostrar True caso a string tenha
# pelo menos uma vogal (a,e,i,o,u)
s1 = 'swtr' # False
s2 = 'oi mundo' # True

resultado_s1 = False
for letra in s1:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        resultado_s1 = True
print(resultado_s1)

resultado_s2 = False
for letra in s2:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        resultado_s2 = True
print(resultado_s2)