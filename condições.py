#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-#
#   >>> Fundamentos de Python <<<     #
#   >> Condições (if, else, elif) <<  #
#   >>> len, listas, etc. <<<         #
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-# 

'''    >>>> Cauã Campos <<<<    '''

### Início do código ###

from time import sleep

' >>>> Exemplo utilizando o len e listas. <<<< '

testes = ['Matemática', 'Sociologia', 'Redação'] # Uma lista com os testes de hoje. (segunda-feira)
print(f'Ainda hoje, você terá que fazer {len(testes)} avaliações.') # Imprime a quantidade de testes que você terá que fazer hoje. (segunda-feira)
print('')

sleep(3)

' >>>> Exemplo utilizando as condições <<<< '

#  Calculando nota do bimestre:

# Suponhamos que a média de uma escola é 6.
# E o sistema funciona assim: ele pega a nota do seu teste, trabalho e prova, e divide tudo por 3, se no final der >= 6 sua nota é azul.

nota_1 = int(input('Digite sua nota no teste: '))  # Recebe a nota do teste.
nota_2 = int(input('Digite sua nota no trabalho: ')) # Recebe a nota do trabalho.
nota_3 = int(input('Digite sua nota na prova: ')) # Recebe a nota da prova.

total = nota_1 + nota_2 + nota_3 # Soma todas as notas.
resultado = total / 3 # Divide tudo por dois.

print('')

print(f'Sua nota no teste foi {(nota_1)}.')
sleep(1)
print(f'Sua nota no trabalho foi {(nota_2)}.')
sleep(1)
print(f'Sua nota na prova foi {(nota_3)}.')
print('')
sleep(1)
print(f'Calculando sua nota final...')
print('')
sleep(5)

if resultado > 6:
    print(f'Parabéns, seu resultado final foi {(resultado)}, nota azul!')
elif resultado == 6:
    print(f'Parabéns sua nota foi {(resultado)}, nota azul, mas podemos melhorar, FOCO!!!')
else:
    print(f'Opss, seu resultado final foi {(resultado)}, nota vermelha. você está de recuperação!')
