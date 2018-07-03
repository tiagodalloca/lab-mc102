#!/usr/bin/env python3

import re

sair_re = re.compile("^\s*q\s*$")
impressao_re = re.compile("^\s*(A|B)\s*$")
atribuicao_re = re.compile("^\s*(A|B)\s*=\s*\{\s*([^\}]*)\s*\}\s*$")
pertence_re = re.compile("^\s*([0-9]+)\s*e\s*(A|B)\s*$")
contido_re = re.compile("^\s*(A|B)\s*c\s*(A|B)\s*$")
adiciona_re = re.compile("^\s*(A|B)\s*\+=\s*([0-9]+)\s*$")
remove_re = re.compile("^\s*(A|B)\s*\-=\s*([0-9]+)\s*$")
uniao_re = re.compile("^\s*(A|B)\s*u\s*(A|B)\s*$")
intersecao_re = re.compile("^\s*(A|B)\s*\^\s*(A|B)\s*$")
uniao_disjunta_re = re.compile(
    "^\s*(A|B)\s*\\\\\s*(A|B)\s*u\s*(A|B)\s*\\\\\s*(A|B)\s*$")
diferenca_re = re.compile("^\s*(A|B)\s*\\\\\s*(A|B)\s*$")

conj = dict()
conj["A"] = list()
conj["B"] = list()

import sys
import os
sys.path.insert(0, os.getcwd())
import lab15 as lab

while __name__ == '__main__':
    linha = input()

    m = sair_re.match(linha)
    if m:
        break

    m = impressao_re.match(linha)
    if m:
        print(m.group(1), "=", "{" + ', '.join(str(v)
                                               for v in sorted(conj[m.group(1)])) + "}")
        continue

    m = atribuicao_re.match(linha)
    if m:
        conj[m.group(1)] = list()
        for i in re.split("[\s,]+", m.group(2)):
            if i:
                lab.adicao(conj[m.group(1)], int(i))
        print(m.group(1), "=", "{" + ', '.join(str(v)
                                               for v in sorted(conj[m.group(1)])) + "}")
        continue

    m = pertence_re.match(linha)
    if m:
        if lab.pertence(conj[m.group(2)], int(m.group(1))):
            print("verdadeiro")
        else:
            print("falso")
        continue

    m = contido_re.match(linha)
    if m:
        if lab.contido(conj[m.group(1)], conj[m.group(2)]):
            print("verdadeiro")
        else:
            print("falso")
        continue

    m = adiciona_re.match(linha)
    if m:
        lab.adicao(conj[m.group(1)], int(m.group(2)))
        print(m.group(1), "=", "{" + ', '.join(str(v)
                                               for v in sorted(conj[m.group(1)])) + "}")
        continue

    m = remove_re.match(linha)
    if m:
        lab.subtracao(conj[m.group(1)], int(m.group(2)))
        print(m.group(1), "=", "{" + ', '.join(str(v)
                                               for v in sorted(conj[m.group(1)])) + "}")
        continue

    m = uniao_re.match(linha)
    if m:
        r = sorted(lab.uniao(conj[m.group(1)], conj[m.group(2)]))
        print(m.group(1), "u", m.group(2), "=",
              "{" + ', '.join(str(v) for v in r) + "}")
        continue

    m = intersecao_re.match(linha)
    if m:
        r = sorted(lab.intersecao(conj[m.group(1)], conj[m.group(2)]))
        print(m.group(1), "^", m.group(2), "=",
              "{" + ', '.join(str(v) for v in r) + "}")
        continue

    m = diferenca_re.match(linha)
    if m:
        r = sorted(lab.diferenca(conj[m.group(1)], conj[m.group(2)]))
        print(m.group(1), "\\", m.group(2), "=",
              "{" + ', '.join(str(v) for v in r) + "}")
        continue

    m = uniao_disjunta_re.match(linha)
    if m:
        r = sorted(lab.uniao_disjunta(conj[m.group(1)], conj[m.group(2)]))
        print(linha, "=", "{" + ', '.join(str(v) for v in r) + "}")
        continue
    print("Read error:", linha)
