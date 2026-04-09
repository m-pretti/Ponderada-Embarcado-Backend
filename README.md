# Estação Meteorológica IoT - Backend & Dashboard

Este projeto consiste em um sistema completo de monitoramento meteorológico, integrando um simulador de sensores, um servidor backend em Flask, e um dashboard web com visualização de dados em tempo real e gerenciamento.

## Funcionalidades

- **Coleta de Dados**: Recebimento de dados de temperatura e umidade via API REST (JSON).
- **Persistência**: Armazenamento utilizando SQLite.
- **Dashboard**: Visualização gráfica da variação de temperatura usando Chart.js.
- **CRUD Completo**: Interface para listar, editar e excluir registros do histórico.
- **Simulador IoT**: Script Python que simula o comportamento de um sensor físico enviando dados via HTTP.

## Estrutura do Projeto

```text
Ponderada-Embarcado-Backend/
├── src/
│   ├── static/
│   │   └── css/
│   │       └── style.css      # Estilização centralizada
│   ├── templates/
│   │   ├── index.html         # Dashboard com gráfico
│   │   ├── historico.html     # Listagem e exclusão
│   │   └── editar.html        # Formulário de edição
│   ├── app.py                 # Servidor Flask (Rotas e API)
│   ├── database.py            # Módulo de persistência (CRUD)
│   └── schema.sql             # Definição das tabelas SQL
├── simulador.py               # Simulador de sensor IoT
├── requirements.txt           # Dependências do projeto
├── .gitignore                 # Arquivos ignorados pelo Git
└── dados.db                   # Banco de dados SQLite (Gerado automaticamente)
```

## Como Executar

### Preparar o Ambiente

```bash
# Clone o repositório
git clone https://github.com/m-pretti/Ponderada-Embarcado-Backend
cd Ponderada-Embarcado-Backend

# Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Iniciar o Servidor

```bash
python3 src/app.py
```
O servidor estará disponível em `http://localhost:5000`.

### Iniciar o Simulador em outro terminal

```bash
python3 simulador.py
```

O simulador começará a enviar dados de temperatura e umidade a cada 5 segundos.

## Como Testar

1. **Visualização**: Acesse `http://localhost:5000` para ver o gráfico de temperatura atualizando.
2. **Listagem**: Clique em "Ver Histórico Completo" para ver todos os registros salvos.
3. **Edição**: Na página de histórico, clique em "Editar", altere os valores no formulário e salve.
4. **Exclusão**: No histórico, clique em "Excluir" e confirme para remover um registro do banco de dados.

## Decisões de Arquitetura

Devido à ausência de hardware físico no momento do desenvolvimento, optei por construir esse Simulador de Sensores em Python. Este script utiliza a biblioteca `requests` para realizar requisições POST ao servidor, simulando perfeitamente o comportamento que um módulo ESP32 ou Arduino teria ao enviar dados de sensores reais.