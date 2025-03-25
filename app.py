class Despesa:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        try:
            self.valor = float(valor)
            if self.valor <= 0:
                raise ValueError("O valor da despesa deve ser positivo.")
        except ValueError:
            raise ValueError("O valor da despesa deve ser um número válido.")

class ControleDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self, despesa):
        self.despesas.append(despesa)

    def listar_depesas(self):
        if self.despesas:
            print('-'*30)
            print('Lista de Despesas:')
            print('-'*30)
            for index, despesa in enumerate(self.despesas, start=1):
                print(f'{index}. Descrição: {despesa.descricao}')
                print(f'Categoria: {despesa.categoria}')
                print(f'Valor: R$ {despesa.valor:.2f}')
                print('-'*20)
            print('-'*30)
        else:
            print('Nenhuma despesa foi cadastrada.')

if __name__ == '__main__':
    controle = ControleDespesas()

    while True:
        print('\n--- Menu ---')
        print('1 - Adicionar Despesas')
        print('2 - Listar Despesas')
        print('3 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            print('\n--- Adicionar Despesa ---')
            descricao = input('Qual a descrição do produto? ')
            categoria = input('Qual a categoria do produto? ')
            while True:
                valor_str = input('Qual o valor do produto? R$ ')
                try:
                    valor = float(valor_str)
                    if valor <= 0:
                        print('Erro: O valor da despesa deve ser positivo. Tente novamente.')
                    else:
                        despesa = Despesa(descricao, categoria, valor)
                        controle.adicionar_despesas(despesa)
                        print('-'*30)
                        print('Despesa adicionada com sucesso!')
                        print('-'*30)
                        break
                except ValueError:
                    print('Erro: O valor digitado não é um número válido. Tente novamente.')
            continue

        elif opcao == '2':
            print('\n--- Listar Despesas ---')
            controle.listar_depesas()

        elif opcao == '3':
            print('Finalizando...')
            break

        else:
            print('Opção inválida! Tente novamente.')