# Traduzo 💬


É um projeto voltado para treinar a capacidade de criar Controllers, Models, Views e Testes para o Framework Flask.

<details>
<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>

É uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Back-end (pela controller) fornecerá diretamente a camada View, para a pessoa usuária.

</details>

<details>
  <summary><strong>:memo: Habilidades desenvolvidas </strong></summary>

Neste projeto, aprendi a:

- Implementar uma API utilizando arquitetura em camadas MVC;
- Utilizar o Docker para projetos Python;
- Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Escrever testes para APIs para garantir a implementação dos endpoints;
- Interagir com um banco de dados não relacional MongoDB;
- Desenvolver páginas web Server Side.
  
</details>



## Instalando o projeto 🐳

**[1]** Clone o repositório

- Use o comando: `git clone git@github.com:MandyTrajano90/Traduzo.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd Traduzo`

**[2]** Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**[3]** Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

**Escolha uma opção:**

- Lembre de sua escolha para rodar as Seeds

**[4 - Opção A]** Banco e Flask pelo Docker

```bash
docker compose up translate
```

- Recomendada: Dockerfile e Docker-compose já estão prontos para uso, para conectar o MongoDB e o Flask.

**[4 - Opção B]** Banco pelo Docker, Flask localmente pelo ambiente virtual

```bash
docker compose up -d mongodb

python3 src/app.py
```

**[5]** Comece seu desenvolvimento, podendo inclusive já acessar a aplicação pelo navegador na rota <http://127.0.0.1:8000/> caso utilize a padrão do projeto.

**[6]** 💡Dica: Ao rodar a aplicação via docker, algumas variáveis de ambiente estão configuradas. O banco de dados populado ao rodar a aplicação localmente será diferente. Se encontrar alguma divergência, consulte o arquivo [db.py](src/database/db.py) e certifique-se de que está executando os comandos no ambiente escolhido, local ou docker.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, utilizei nesse projeto o linter `Flake8`. Assim o código fica alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se se o ambiente virtual está ativado

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>

  👀 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/7.3.x/contents.html).
  </details>





## 👁️ Dê uma olhada no código



![Tela](src/views/static/images/traduzo.png)



https://github.com/user-attachments/assets/058fefce-4552-42b1-abc1-5d0474c82db4


<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
