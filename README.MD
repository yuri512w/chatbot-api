Monitoramento de CPU e Memória com Flask

Este projeto implementa uma API simples utilizando Flask para monitorar o uso de CPU e memória do sistema. A API fornece informações em formato JSON sobre o uso atual da CPU, uso da memória, memória total e memória disponível.
Pré-requisitos

Certifique-se de ter os seguintes componentes instalados em seu ambiente:

    Python 3.x
    pip (gerenciador de pacotes do Python)
    Docker (opcional, para execução em contêiner)

Instalação

    Clone o repositório:

git clone https://github.com/seu-usuario/monitor-cpu-memoria.git
cd monitor-cpu-memoria

Crie um ambiente virtual (recomendado):

python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

Instale as dependências:

    pip install -r requirements.txt

Executando a Aplicação
Localmente

Para executar a aplicação localmente:

python app.py

A API estará disponível em http://127.0.0.1:5000/status.
Usando Docker

Para executar a aplicação em um contêiner Docker:

    Construa a imagem Docker:

docker build -t monitor-cpu-memoria .

Inicie o contêiner:

    docker run -d -p 5000:5000 monitor-cpu-memoria

A API estará disponível em http://127.0.0.1:5000/status.
Endpoints da API

    GET /status: Retorna o uso atual da CPU e memória em formato JSON.

    Exemplo de resposta:

    {
      "cpu_usage": "15.0%",
      "memory_usage": "45.3%",
      "total_memory": "8.00 GB",
      "available_memory": "4.38 GB"
    }

Testando a API

Para testar a API, você pode usar ferramentas como Postman ou Insomnia. Alternativamente, a linha de comando curl pode ser utilizada:

curl http://127.0.0.1:5000/status

Observações

    Porta em Uso: Se ao iniciar a aplicação você encontrar um erro indicando que a porta 5000 já está em uso, identifique o processo que está ocupando a porta e encerre-o. No Linux, você pode usar os seguintes comandos:

    sudo lsof -i :5000
    sudo kill -9 <PID>

    Substitua <PID> pelo ID do processo que está utilizando a porta.

    Ambiente de Desenvolvimento: A aplicação está configurada para rodar em modo de desenvolvimento (debug=True). Para uso em produção, certifique-se de desativar o modo de depuração e utilizar um servidor WSGI adequado, como o Gunicorn.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.