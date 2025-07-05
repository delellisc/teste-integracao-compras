# Sistema de Compras - Teste de Integração
Este projeto simula um sistema básico de compras em Python com funcionalidades para cadastro de usuários, cadastro de produtos e realização de compras. O principal objetivo do exercício é praticar a integração entre módulos, o tratamento de exe
ceções e a validação de dados por meio de testes manuais.

## Objetivo da Avaliação

Implementar um fluxo de integração testando as principais funcionalidades do sistema de compras:

- Cadastro de usuários
- Cadastro de produtos
- Realização de compras
- Listagem de compras
- Tratamento de exceções

## Testes Requisitados e Implementação

Cada etapa foi transformada em um teste dentro da função `test_fluxo_integra_compras()`, encontrada no arquivo de [Teste de Integração](./teste_integracao.py).

### Limpeza dos "bancos" de dados

Os dicionários em memória são esvaziados no início do teste para garantir um ambiente limpo:
```py
usuarios_db.clear()
produtos_db.clear()
compras_db.clear()
```

### 1. Cadastrar usuários e testar
Cadastra um usuário e garante que as informações esperadas foram armazenadas:
```py
cadastrar_usuario(1, "João de Deus")
assert consultar_usuario(1) == "João de Deus", "Usuário não foi cadastrado corretamente."
```

### 2. Cadastrar produtos e testar
Cadastra um produto e garante que as informações esperadas foram armazenadas:
```py
cadastrar_produto(1, "Prancha em Miniatura", 100)
assert consultar_produto(1) == {'nome': 'Prancha em Miniatura', 'preco': 100}, "Produto não condizente."
```

### 3. Realizar compra válida
Realiza uma compra e verifica se a função retorna o valor esperado:
```py
assert realizar_compra(1, [1]) == 100, "Compra não foi realizada com sucesso."
```

### 4. Tentar compra com produto inválido
Simula uma compra de um produto inexistente e trata o erro:
```py
try:
    realizar_compra(1, [2])
    assert False, "Esperado erro ao comprar produto inexistente"
except ValueError as error_msg:
    assert str(error_msg) == "Produto 2 não encontrado.", f"Mensagem de erro incorreta: {error_msg}"
```

### 5. Verificar compras do usuário 1
Verifica se a função de listagem retorna as compras efetuadas pelo usuário previamente:
```py
assert listar_compras(1) == [{'produtos': [1], 'total': 100}], "Compras retornadas não condizem com as compras efetuadas pelo usuário."
```

### 6. Verificar um usuário que não tem compras
Verifica se a função de listagem retorna uma lista vazia para um usuário que não efetuou nenhuma compra:
```py
cadastrar_usuario(2, "Maria José")
assert listar_compras(2) == [], "Usuário verificado possui compras!"
```

## Como executar
Para fazer uso desse sistema e executar os testes apresentados, o passo inicial é clonar este repositório:
```sh
git clone https://github.com/delellisc/teste-integracao-compras
```

A estrutura esperada para o repositório local é a seguinte:
```sh
.
├── compras.py
├── produtos.py
├── README.md
├── teste_integracao.py
└── usuarios.py
```

Após isso, o arquivo de teste pode ser executado com o comando abaixo:
```sh
python3 teste_integracao.py
```

## Ambiente de Desenvolvimento
Esse código foi desenvolvido no sistema operacional abaixo:
```sh
$ cat /etc/os-release
NAME="Pop!_OS"
VERSION="22.04 LTS"
ID=pop
ID_LIKE="ubuntu debian"
PRETTY_NAME="Pop!_OS 22.04 LTS"
VERSION_ID="22.04"
[...]
```

A versão do Python utilizada foi a seguinte:
```sh
$ python3 --version
Python 3.10.12
```

O código foi editado utilizando o terminal:
```sh
$ gnome-terminal --version
# GNOME Terminal 3.44.0 using VTE 0.68.0 +BIDI +GNUTLS +ICU +SYSTEMD
```

E o Visual Studio Code:
```sh
$ code --version
1.101.2
2901c5ac6db8a986a5666c3af51ff804d05af0d4
x64
```

## Autor

**Camilo de Lellis**  
[GitHub](https://github.com/delellisc) | [LinkedIn](https://www.linkedin.com/in/camilo-de-lellis-de-medeiros/)