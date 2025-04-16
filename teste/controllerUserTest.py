import unittest
from unittest.mock import patch
from controller.user import listarUsuarios, criarUsuario, deletar, listarApenasUmUsuario

class TestServiceUser(unittest.TestCase):
    
    def setUp(self):
        self.mock_users = [{"nome":"pedro", "email":"cpf", "senha":"1232141", "CPF":"12292813432"},
               {"nome": "Chico", "email": "teste@teste.com", "senha": "1234567", "CPF":"471987563"}]
        
    @patch('controller.user.usariosLista', new_callable=list)
    def test_criarUsuario(self, mock_usariosLista):
        mock_usariosLista.extend(self.mock_users)
        result = criarUsuario(mock_usariosLista)
        self.assertTrue(result)
        
    @patch('controller.user.usariosLista', new_callable=list)
    def test_listar_um_usuario(self,mock_usariosLista):
        mock_usariosLista.extend(self.mock_users)
        result = listarApenasUmUsuario("471987563")
        self.assertEqual(result, mock_usariosLista[1])

    @patch('controller.user.usariosLista', new_callable=list)
    def test_listar_todos_os_usuarios_service(self,mock_usariosLista):
        mock_usariosLista.extend(self.mock_users)
        result = listarUsuarios()
        self.assertEqual(result, mock_usariosLista)

    @patch('controller.user.usariosLista', new_callable=list)
    def test_deletar_usuario_success(self, mock_usariosLista):
        mock_usariosLista.extend(self.mock_users)

        result = deletar("471987563")
        self.assertTrue(result)
        self.assertEqual(len(mock_usariosLista), 1)  
        self.assertNotIn({"nome": "Chico", "email": "teste@teste.com", "senha": "1234567", "CPF": "471987563"}, mock_usariosLista)


if __name__ == "__main__":
    unittest.main()