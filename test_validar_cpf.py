import unittest
from validar_cpf import validar_cpf
class TestValidarCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf('11718625750'))

    def test_cpf_invalido_digitos_iguais(self):
        self.assertFalse(validar_cpf('88888888888'))

    def test_cpf_invalido_com_letras(self):
        self.assertFalse(validar_cpf('abcd1234567'))

    def test_cpf_invalido_com_caracteres_especiais(self):
        self.assertFalse(validar_cpf('123.456.789-10'))

    def test_cpf_invalido_com_menos_digitos(self):
        self.assertFalse(validar_cpf('1234567899'))

    def test_cpf_invalido_com_mais_digitos(self):
        self.assertFalse(validar_cpf('123456789012867'))

    def test_cpf_invalido_digito_verificador(self):
        self.assertFalse(validar_cpf('11718625751'))

if __name__ == '__main__':
    unittest.main()