# meu_dicionario = {'nome': 'Pedro', 'idade': 21, 'profissao': 'DevOps'}

# print(meu_dicionario.get('nome'))
# print(meu_dicionario.get('idade'))
# print(meu_dicionario.get('profissao'))


pessoa = {
    'nome': 'pedro',
    'idade': 21,
    'profissao': 'QA->Dev->DevOPS',
    'hobbies': ['Gaming', 'Drawing', 'Home Labbing'],
    'pet': {
        'nome': 'Maia',
        'idade': 1,
        'peso': '2kg',
        'Racoes': ['Dog Chow', 'Magnus']
    },
    'mae': {
        'nome': 'Lindona',
        'sobrenome': 'Da Silva',
        'hobbies': ['Beber', 'ser Foda']
    }
}
#     v                   v até o ultimo v, será retornado uma lista
print(pessoa.get('hobbies')[0])

#acessando a pessoa pedro, indo para a mãe, acessar o array de hobbies e pega o primeiro valor. :)
print(pessoa['mae']['hobbies'][0])
