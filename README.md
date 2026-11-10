# Estudo de POO – Herança e **kwargs em Python

## Sobre o projeto

Neste código, desenvolvi um pequeno exemplo utilizando Programação Orientada a Objetos (POO) em Python para entender melhor como funciona a herança entre classes e como podemos trabalhar com argumentos dinâmicos utilizando `**kwargs`.

A ideia foi criar uma classe principal chamada `Pessoa` e, a partir dela, uma classe `Programador`, que herda suas características e adiciona informações próprias.

## O que pratiquei

- **Herança:** utilizei a classe `Pessoa` como base para criar a classe `Programador`.
- **Construtores (`__init__`):** trabalhei com a inicialização dos objetos e seus atributos.
- **Super():** utilizei para chamar o construtor da classe pai e reaproveitar sua estrutura.
- **\*\*kwargs:** pratiquei o recebimento de argumentos nomeados adicionais, agrupados em um dicionário.
- **Atributos:** trabalhei com o armazenamento e acesso às informações dos objetos.

## Como funciona

A classe `Pessoa` recebe nome e idade, além de permitir receber outras informações através de `**kwargs`.

A classe `Programador` herda de `Pessoa`, recebe uma linguagem de programação e utiliza `super()` para encaminhar os argumentos à classe principal.

Dessa forma, consigo adicionar novas informações ao objeto sem precisar declarar todos os parâmetros individualmente em cada classe.

## Exemplo de utilização

```python
programador = Programador(
    "Silvo",
    30,
    linguagem="Python",
    salario=5000,
    experiencia="5 anos"
)
```

Nesse exemplo, nome, idade e linguagem são recebidos diretamente, enquanto salário e experiência são encaminhados através de `**kwargs`.

## Objetivo

Meu objetivo com esse exercício foi aprofundar meus conhecimentos em POO, principalmente na reutilização de código, herança e flexibilidade na passagem de argumentos entre classes.

Projeto desenvolvido para fins de estudo e prática em Python.
