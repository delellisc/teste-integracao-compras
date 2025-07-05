
from usuarios import cadastrar_usuario, consultar_usuario, usuarios_db
from produtos import cadastrar_produto, consultar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db

def test_fluxo_integra_compras():
    print("\nIniciando teste de integração do sistema de compras...\n")

    # Limpa os "bancos" em memória
    usuarios_db.clear()
    produtos_db.clear()
    compras_db.clear()

    # 1. Cadastrar usuários e testar
    cadastrar_usuario(1, "João de Deus")
    assert consultar_usuario(1) == "João de Deus", "Usuário não foi cadastrado corretamente."

    # 2. Cadastrar produtos e testar    
    cadastrar_produto(1, "Prancha em Miniatura", 100)
    assert consultar_produto(1) == {'nome': 'Prancha em Miniatura', 'preco': 100}, "Produto não condizente."
    
    # 3. Realizar compra válida
    assert realizar_compra(1, [1]) == 100, "Compra não foi realizada com sucesso."

    # 4. Tentar compra com produto inválido
    try:
        realizar_compra(1, [2])
        assert False, "Esperado erro ao comprar produto inexistente"
    except ValueError as error_msg:
        assert str(error_msg) == "Produto 2 não encontrado.", f"Mensagem de erro incorreta: {error_msg}"

    # 5. Verificar compras do usuário 1
    assert listar_compras(1) == [{'produtos': [1], 'total': 100}], "Compras retornadas não condizem com as compras efetuadas pelo usuário."

    # 6. Verificar um usuário que não tem compras
    cadastrar_usuario(2, "Maria José")
    assert listar_compras(2) == [], "Usuário verificado possui compras!"
    
    # Como não foi solicitado, considerei essa mensagem final como feedback suficiente para o testador
    # As mensagens de erro em caso de falha nos `asserts` informam o comportamento do teste de fluxo
    print("\nTodos os testes foram executados com êxito!\n")

# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
