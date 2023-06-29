def leiaint(msg):
    While True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, dogote um número inteiro válido.')
            continue
        except (KeyboardInterrupt):