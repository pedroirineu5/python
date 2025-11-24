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

print(pessoa['mae'])