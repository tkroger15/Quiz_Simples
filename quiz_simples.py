def cabecalho(txt=' '):
    print('-' * len(txt))
    print(f'\033[34m{txt}\033[m')
    print('-' * len(txt))


total_acertos = soma_acertos = cnt_questoes = 0

cabecalho('MEU JOGO DE PERGUNTAS')

perguntas = {  # dic1
    'pergunta1': {  # dic 2
        'pergunta': 'qual é o protagonista de the boys?',
        'resposta': {'a': 'leitinho', 'b': 'tempesta', 'c': 'bruto'},  # cic 3
        'resposta_certa': 'c',

    },
    'pergunta2': {
        'pergunta': 'quem mora no abacaxi e vive no mar?',
        'resposta': {'a': 'bob esponja', 'b': 'patrick', 'c': 'sirigueijo'},
        'resposta_certa': 'a'
    },
    'pergunta3': {
        'pergunta': 'Quem é o protagonista de 300?',
        'resposta': {'a': 'jack', 'b': 'Leonidas', 'c': 'Dean'},
        'resposta_certa': 'b'

    },
    'pergunta4': {
        'pergunta': 'Qual jogo do ano de 2018?',
        'resposta': {'a': 'red dead', 'b': 'God of war', 'c': 'zelda'},
        'resposta_certa': 'b'
    },
    'pergunta5': {
        'pergunta': 'assassin creed...',
        'resposta': {'a': 'morreu no Black flag', 'b': 'odyssey é bom', 'c': 'o II é ruim'},
        'resposta_certa': 'a'
    }
}

for pk, pv in perguntas.items():  # pergunta key
    cnt_questoes += 1
    print(f'{pk}: {pv["pergunta"]}')
    print()
    print('alternativas: ')
    
    for qk, qv in pv['resposta'].items():  # questao key
        print(f'({qk}) {qv}')
    resposta_usuario = input('Qual seu palpite? ').lower().strip()[0]
    
    if resposta_usuario != 'a' and resposta_usuario != 'b' and resposta_usuario != 'c':
        while True:
            resposta_usuario = input('Qual seu palpite? ').lower().strip()[0]
            if resposta_usuario == 'a' or resposta_usuario == 'b' or resposta_usuario == 'c':
                break

    if resposta_usuario == pv['resposta_certa']:
        print('\033[32mcorreto!\033[m')
        total_acertos += 1
        print()
    else:
        print('\033[31mIncorreto!\033[m')
        print()

soma_acertos = total_acertos / cnt_questoes * 100

if soma_acertos >= 60:
    print(f'\033[32mFim de jogo! você obteve {total_acertos} acertos de {cnt_questoes} perguntas!\033[m')
    print(f'\033[32mSua porcentagem de acertos é de: {soma_acertos :.0f}%\033[m')
else:
    print(f'\033[31mFim de jogo! você obteve {total_acertos} acertos de {cnt_questoes} perguntas!\033[m')
    print(f'\033[31mSua porcentagem de acertos é de: {soma_acertos :.0f}%\033[m')
