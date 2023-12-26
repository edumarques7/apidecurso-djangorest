import requests

class TesteCursos:
    headers = {'Authorization': 'Token 6f5228ec34ab80b5971258c1e6ce90636b79c631'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "curso de progamacao com ruby00009",
            "url": "https://www.rub533y3.com.br"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "novo curso de rub003",
            "url": "https://www.novocursoderubly119.com"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}7/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo curso de ruby 001",
            "url": "https://www.rulby921.com"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}9/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0