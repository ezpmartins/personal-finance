class Despesa:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        try:
            self.valor = float(valor)
            if self.valor <= 0:
                raise ValueError('O valor da despesa deve ser positivo.')
        except ValueError:
            raise ValueError('O valor da despesa deve ser um número válido.')

class ControleDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self,despesa):
        self.despesas.append(despesa)

    def listar_depesas(self, criterio=None):
        if not self.despesas:
            print('Nenhuma despesa foi cadastrada')
            return

        despesas_ordenadas = list(self.despesas)

        if criterio == 'categoria':
            despesas_ordenadas.sort(key=lambda despesa: despesa.categoria)
        elif criterio =='valor':
            despesas_ordenadas.sort(key=lambda despesa: despesa.valor)
        elif criterio == 'descricao':
            despesas_ordenadas.sort(key=lambda despesa: despesa.descricao)
        print('-'*30)
        print('Lista de Despesas:')
        print('-'*30)
        total_despesas = 0.0  # Inicialize como float para garantir
        for index, despesa in enumerate(despesas_ordenadas, start=1):
            print(f'{index}. Descrição: {despesa.descricao}')
            print(f'Categoria: {despesa.categoria}')
            print(f'Valor: R$ {despesa.valor:.2f}')
            print('-'*20)
            total_despesas += despesa.valor
        print('-'*30)
        print(f'O total de despesas foi: R$ {total_despesas:.2f}') # Formatação correta
        print('-'*30)


if __name__ == '__main__':
    controle = ControleDespesas()

    while True:
        print('\n--- Menu ---')
        print('1 - Adicionar Despesas')
        print('2 - Listar Despesas')
        print('3 - Listar Despesas por categoria')
        print('4 - Listar Despesas por valor')
        print('5 - Listar Despesas por descrição')
        print('6 - Sair')

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
            controle.listar_depesas(None)

        elif opcao == '3':
            print('\n--- Listar Despesas por categoria ---')
            controle.listar_depesas(criterio='categoria')

        elif opcao == '4':
            print('\n--- Listar Despesas por valor ---')
            controle.listar_depesas(criterio='valor')

        elif opcao == '5':
            print('\n--- Listar Despesas por Descrição ---')
            controle.listar_depesas(criterio='descricao')

        elif opcao == '6':
            print('Finalizando...')
            break

        else:
            print('Opção inválida! Tente novamente.')