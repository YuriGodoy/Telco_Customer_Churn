
import unittest

from repo_git.metrics import calcular_media


class TestCalcularMedia(unittest.TestCase):

    def test_media_simples(self):
        resultado = calcular_media([10, 20, 30])
        self.assertEqual(resultado, 20)

    def test_media_decimal(self):
        resultado = calcular_media([2, 3])
        self.assertEqual(resultado, 2.5)

    def test_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()
