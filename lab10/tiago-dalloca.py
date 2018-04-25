# RA 206341

# Os políticos da Aliança Rebelde realizam muitos discursos pela galáxia, e o processo de criação dos discursos demanda muito tempo, principalmente a parte de escrevê-los. Os redatores dos discursos notaram que as operações mais utilizadas por eles durante a escrita eram: apagar, substituir e inverter uma palavra. Para agilizar o processo de criação dos seus discursos, os políticos da Aliança Rebelde precisam de um editor de texto com estas três funções.

def foo(word):
    if word[-1:] in [",", "?", ".", ":", "!"]:
        return word[:-1]
    return word

def yeah(word):
    if word[0] in [",", "?", ".", ":", "!"]:
        return word[::-1][:-1][::-1] + word[0]
    return word


def ou_yeah(word, arg2):
    if word[-1:] in [",", "?", ".", ":", "!"]:
        return arg2 + word[len(word) - 1]
    return arg2


text = input().split()

cases = {
    "d": lambda _, arg: filter((lambda word: foo(word).lower() != arg), text),
    "i": lambda _, arg: map((lambda word: yeah(word[::-1]) if foo(word).lower() == arg else word), text),
    "r": lambda _, arg1, arg2: map((lambda word: ou_yeah(word, arg2) if foo(word).lower() == arg1 else word), text)
}


def inputs():
    x = input().lower()
    while x != "q":
        if x == "d":
            yield (x, input().lower())
        if x == "i":
            yield (x, input().lower())
        if x == "r":
            yield (x, input().lower(), input())
        x = input().lower()


print(" ".join(text))
for e in inputs():
    text = list(cases[e[0]](*e))
    print(" ".join(text))
