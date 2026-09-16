from typing import Any
import httpx

URL_BASE = "https://reqres.in/api/users"


def executar_desafio_crud() -> None:
    print("=== MINI-DESAFIO: 4 MÉTODOS HTTP NA REQRES (HTTPX) ===\n")

    with httpx.Client(timeout=5.0) as client:
        # ------------------------------------------------------------------
        # TODO 1: Implemente a busca (GET) do usuário de ID 2
        # ------------------------------------------------------------------
        # resp_get = client.get(...)
        # Verifique o status code (200) e imprima o nome e e-mail do usuário
        print(client.get(url=URL_BASE+"/2"))
        # ------------------------------------------------------------------
        # TODO 2: Implemente o cadastro (POST) com seu nome e cargo
        # ------------------------------------------------------------------
        # payload_post = {"name": "...", "job": "..."}
        # resp_post = client.post(URL_BASE, json=payload_post)
        # Verifique o status code (201) e imprima o ID gerado


        print(client.post(url=URL_BASE,json={ "name": "Roger","job":"Coder"}))


        # ------------------------------------------------------------------
        # TODO 3: Implemente a atualização completa (PUT) do usuário de ID 2
        # ------------------------------------------------------------------
        # payload_put = {"name": "...", "job": "..."}
        # resp_put = client.put(f"{URL_BASE}/2", json=payload_put)
        # Verifique o status code (200) e imprima o timestamp updatedAt
        # ------------------------------------------------------------------
        print(client.put(url=URL_BASE+"/2",json={ "name": "Roger","job":"Coder"}))



        # TODO 4: Implemente a exclusão (DELETE) do usuário de ID 2
        # ------------------------------------------------------------------
        # resp_delete = client.delete(...)
        # Verifique se o status code retornado é exatamente 204
        print(client.delete(URL_BASE))

        
        pass


if __name__ == "__main__":
    executar_desafio_crud()