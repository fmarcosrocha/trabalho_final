from PIL import Image
import requests
import os

class Download:
    def __init__(self, url, path_arquivo):
        self.url = url
        self.path_arquivo = path_arquivo

    def download_file(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Verifica se houve algum erro na requisi��o
            with open(self.path_arquivo, 'wb') as file:
                file.write(response.content)
            print(f"Download completo. Arquivo salvo em: {self.path_arquivo}")
        except requests.exceptions.MissingSchema:
            print("URL inv�lida. Certifique-se de fornecer uma URL v�lida.")
        except requests.exceptions.RequestException as e:
            print(f"Erro na conex�o: {e}")