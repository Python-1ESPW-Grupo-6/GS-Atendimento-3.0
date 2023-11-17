import sys
from datetime import datetime
import os

timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
nova_entrada = f'Nova entrada em {timestamp}:\n\n'
nome_arquivo = 'relatório.txt'

def traco():
    print('-'*30)

def erro():
    traco()
    print('Opção não encontrada, tente novamente!')
    traco()

def relatorio(tipo_entrada):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(nova_entrada)

            arquivo.write(f'Nome do paciente: {nome_paciente}\n')
            arquivo.write(f'Número do RG: {rg}\n')
            arquivo.write(f'Número do CPF: {cpf}\n')
            
            if plano_saude != 'nenhum':
                arquivo.write(f'Plano de saúde: {plano_saude}\n')
                arquivo.write(f'Número CNS: {cns}\n')
            
            arquivo.write(f'Tipo de entrada: {tipo_entrada}\n\n')
    
    else:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(nova_entrada)

            arquivo.write(f'Nome do paciente: {nome_paciente}\n')
            arquivo.write(f'Número do RG: {rg}\n')
            arquivo.write(f'Número do CPF: {cpf}\n')
            
            if plano_saude != 'nenhum':
                arquivo.write(f'Plano de saúde: {plano_saude}\n')
                arquivo.write(f'Número CNS: {cns}\n')
            
            arquivo.write(f'Tipo de entrada: {tipo_entrada}\n\n')

traco()
print('Sejá bem vindo ao nosso sistema de agendamento 3.0!')
traco()

while True:
    try:
        escolha = int(input('''\n Menu de entradas:
        [1] Entrada para urgências e emergências
        [2] Entrada para cirurgia\n\nEscolha a opção mais apropriada: '''))

        match escolha:
            
            case 1:
                print('Será necessario a apresentação de alguns documentos, \ninsira as informações nos locais abaixo.')

                print('')
                nome_paciente = input('Qual o nome do paciente? ')
                rg = int(input('Qual o RG? '))
                cpf = int(input('Qual o CPF? '))
                plano_saude = input('Qual o plano de saúde? (se não tiver, preencha com "nenhum") ')
                if plano_saude == 'nenhum':
                    pass
                else:
                    cns = int(input('Qual o número do CNS (Cartão Nacional de Saúde)?'))
                
                print('')
                print('Muito obrigado pela colaboração, seu agendamento já está no registro!')

                relatorio('urgência e emergência')

                sys.exit()

            case 2:
                print('Será necessario a apresentação de alguns documentos, \ninsira as informações nos locais abaixo.')

                print('')
                nome_paciente = input('Qual o nome do paciente? ')
                rg = int(input('Qual o RG? '))
                cpf = int(input('Qual o CPF? '))
                plano_saude = input('Qual o plano de saúde? (se não tiver, preencha com "nenhum") ')
                if plano_saude == 'nenhum':
                    pass
                else:
                    cns = int(input('Qual o número do CNS (Cartão Nacional de Saúde)?'))
                
                print('')
                print('Será necessário que o paciente leve os exames solicitados \npelo médico e objetos para uso pessoal!')
                print('Muito obrigado pela colaboração, seu agendamento já está no registro!')

                relatorio('cirurgia')

                sys.exit()

            case _:
                erro()
                print('')

    except ValueError:
        erro()
        print('')