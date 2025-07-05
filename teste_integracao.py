
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
    # assert usuarios_db == {1: "João de Deus"}, "Usuário não foi cadastrado corretamente."

    # 2. Cadastrar produtos e testar    
    cadastrar_produto(1, "Prancha em Miniatura", 100)
    assert consultar_produto(1) == "Prancha em Miniatura", "Produto não condizente."

    # 3. Realizar compra válida
    

    # 4. Tentar compra com produto inválido


    # 5. Verificar compras do usuário 1


    # 6. Verificar um usuário que não tem compras

# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
