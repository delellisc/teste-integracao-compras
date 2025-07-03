
from usuarios import cadastrar_usuario, usuarios_db
from produtos import cadastrar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db

def test_fluxo_integra_compras():
    print("\nIniciando teste de integração do sistema de compras...\n")

    """
    def setUp(self):
        self.usuarios_db = usuarios_db
        self.produtos_db = produtos_db
        self.compras_db = compras_db
    """

    # Limpa os "bancos" em memória
    def tearDown(self):
        usuarios_db = {}
        produtos_db = {}
        compras_db = {}

    # 1. Cadastrar usuários e testar
    def test_cadastrar_usuario():
        cadastrar_usuario(1, "Prancha em Miniatura")
        assert usuarios_db == {1: "Prancha em Miniatura"}, "Produto não encontrado"

        cadastrar_usuario(1, "Urso de Pelúca")

    test_cadastrar_usuario()

    # 2. Cadastrar produtos e testar


    # 3. Realizar compra válida


    # 4. Tentar compra com produto inválido


    # 5. Verificar compras do usuário 1


    # 6. Verificar um usuário que não tem compras

# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
