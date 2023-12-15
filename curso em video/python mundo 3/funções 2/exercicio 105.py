def notas(*n, sit = False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :para
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r