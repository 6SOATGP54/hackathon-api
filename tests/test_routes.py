import unittest
from vapi import app

class FlaskAppTestCase(unittest.TestCase):
    
    # Testa a rota principal
    def test_running_endpoint(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Server is running')

    # Testa o endpoint de download
    def test_download_endpoint(self):
        with app.test_client() as client:
            response = client.post('/download/zip', data={})  # Simula um POST básico
            self.assertEqual(response.status_code, 200)

    # Testa o endpoint POST do AWS
    def test_aws_post_endpoint(self):
        with app.test_client() as client:
            response = client.post('/aws/post/test', data=b'{"key":"value"}')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    app.config['TESTING'] = True  # Certificando que está em modo de teste
    unittest.main()