# Gorjetta-API
Backend em Python da aplicação Gorjeta

[![Python application](https://github.com/FabioFiorita/Gorjetta-API/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/FabioFiorita/Gorjetta-API/actions/workflows/python-app.yml)

![GitHub repo size](https://img.shields.io/github/repo-size/fabiofiorita/Gorjetta-API?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/fabiofiorita/Gorjetta-API?style=for-the-badge)

- [Gorjetta-API](#gorjetta-api)
  - [🧑‍💻 Integrantes](#-integrantes)
  - [🖥️ Frontend](#️-frontend)
  - [🎯 Funcionalidades](#-funcionalidades)
  - [🖥️ Tecnologias Usadas](#️-tecnologias-usadas)
  - [⚙️ Instale antes de tentar executar os projetos)](#️-instale-antes-de-tentar-executar-os-projetos)
  - [🚀️ Executando os projetos](#️-executando-os-projetos)
  - [💻 Como Rodar](#-como-rodar)

## 🧑‍💻 Integrantes
- [Antonio Victor](https://github.com/Antonio-AV)
- [Ayslan Conti](https://github.com/Aysllan00)
- [Fabio Fiorita](https://github.com/FabioFiorita)
- [Gabriel Cardoso](https://github.com/Gabriel-GCS)

## 🖥️ Frontend
Todo o código desenvolvido para o backend da aplicação está disponível no repositório [Gorjetta](https://github.com/FabioFiorita/Gorjetta)

## 🎯 Funcionalidades
 - [x] - Cálculo de gorjeta utilizando a lógica fuzzy 
 - [x] - Possibilidade de dividir o valor de acordo com a quantidade das pessoas
 - [x] - Valor da gorjeta levando em conta a porcentagem do estabelecimento
  
## 🖥️ Tecnologias Usadas
 - [ReactJS](https://reactjs.org/)
 - [Python](https://www.python.org/)


## ⚙️ Instale antes de tentar executar os projetos)
 - [Python](https://www.python.org/downloads/)

## 🚀️ Executando os projetos

1. Clone o repositório: 
```bash
git clone https://github.com/FabioFiorita/Gorjetta-API && cd Gorjetta-API
```

2. Instale todas as depencências
```bash
pip install -r requirements.txt
```

3. Rode o projeto
```bash
uvicorn main:app --reload
```

4. Teste o projeto
```bash
pytest
```

## 💻 Como Rodar

- Cálculo de gorjeta
```bash
http://127.0.0.1:8000/gorjeta?servico=8&qualidade=10
```

```json
{
    "gorjeta": 16.11111111111111
}
```
