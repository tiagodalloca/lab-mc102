# Gabriel Teston

# Definido as funcoes necessarias


def punctuation():
    """ Retorna uma lista com todas as pontuacoes possiveis. """
    return ['', ',', '.', '?', '!', ':', ' ']


def erase(text):
    """ Retorna o text recebido removendo a palavra recebida como input abaixo. """
    text_list = text.split()
    aux = text.upper().split()
    word = input()
    word_punct = [word + p for p in punctuation()]
    for w in word_punct:
        while w.upper() in aux:
            i = aux.index(w.upper())
            text_list.pop(i)
            aux.pop(i)
    return ' '.join(text_list)


def invert(text):
    """ Retorna o texto recebido invertendo a palavra recebida como input abaixo. """
    text_list = text.split()
    aux = text.upper().split()
    word = input()
    word_punct = [word + p for p in punctuation()]
    for w in word_punct:
        while w.upper() in aux:
            i = aux.index(w.upper())
            if text_list[i][-1] in punctuation():
                p = text_list[i][-1]
                text_list[i] = text_list[i][-2::-1] + p
                aux[i] = aux[i][-2::-1] + p
            else:
                text_list[i] = text_list[i][::-1]
                aux[i] = aux[i][::-1]
    return ' '.join(text_list)


def replace(text):
    """ Retorna o texto recebido subistituindo a palavra recebida como input imediatamente abaixo pela palavra recebida como input susequente. """
    text_list = text.split()
    aux = text.upper().split()
    word = input()
    new_word = input()
    word_punct = [word + p for p in punctuation()]
    for w in word_punct:
        while w.upper() in aux:
            i = aux.index(w.upper())
            if text_list[i][-1] in punctuation():
                p = text_list[i][-1]
                text_list[i] = new_word + p
                aux[i] = new_word + p
            else:
                text_list[i] = new_word
                aux[i] = new_word
    return ' '.join(text_list)
    return new_text


# Dicionario das operacoes possiveis(switch case)
ops = {
    "D": erase,
    "I": invert,
    "R": replace
}

# Recebendo texto inicial
text = input()
print(text)

# Loop de operacoes
op = input()

while op != "Q":
    new_text = ops[op](text)
    print(new_text)
    text = new_text
    op = input()
