def Fibonacci(entrada):
    contador, numero_atual, proximo_numero = 0, 0, 1
    
    while contador < entrada:        
        print(f'{numero_atual}, ', end='')
        
        # Verifica se o número de entrada faz parte da sequência de fibonacci.
        if entrada == numero_atual:
            print(f'\nNúmero {numero_atual} pertence a sequência de fibonacci!')
            break
        elif numero_atual > entrada:
            print(f'\nO Numero {entrada} não pertence a sequência de fibonacci')
            break
        
        soma = numero_atual + proximo_numero
        numero_atual = proximo_numero
        proximo_numero = soma
        contador += 1      

      
entrada = int(input('Informe um número para verificar se o mesmo pertence a sequência de fibonacci.\n'))
Fibonacci(entrada)