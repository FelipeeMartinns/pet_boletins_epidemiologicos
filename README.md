# PET – Boletins Epidemiológicos

Sistema desenvolvido no contexto do **PET-Saúde** com o objetivo de realizar a
**leitura, processamento e análise de dados epidemiológicos** a partir de arquivos
CSV disponibilizados por plataformas como o DATASUS / TabNet, visando a geração
de boletins epidemiológicos.

---

## Pré-requisitos

Antes de iniciar, é necessário ter instalado:

- **Python 3.8 ou superior**
- **Git**
- **VS Code** (opcional, porém recomendado)

Para verificar se o Python está instalado, execute no terminal:

```bash
python --version
```

Em alguns sistemas Linux, utilize:

```bash
python3 --version
```

---

## Como rodar o projeto

### passo-1 Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/FelipeeMartinns/pet_boletins_epidemiologicos.git
```

Em seguida, entre na pasta do projeto:

```bash
cd pet_boletins_epidemiologicos
```

---

### passo-2 Abrir o projeto no VS Code

#### Windows e Linux:

```bash
code .
```

> Caso o comando `code` não funcione, abra o VS Code manualmente e utilize:
> **Arquivo → Abrir Pasta**

---

### passo-3 Instalar a biblioteca pandas

Com o ambiente virtual ativado (ou diretamente no sistema), execute:

```bash
pip install pandas
```

Caso ocorra erro, tente:

#### Windows:

```bash
python -m pip install pandas
```

#### Linux:

```bash
python3 -m pip install pandas
```

---

### passo-4 Executar o script de processamento

O script principal de leitura e processamento dos dados é o arquivo `dados.py`.

#### Windows:

```bash
python dados.py
```

#### Linux:

```bash
python3 dados.py
```

---

## Estrutura do projeto

```text
pet_boletins_epidemiologicos/
├── dados.py               # Script principal de leitura e processamento dos CSVs
├── sinannet_cnv_zika.csv  # Arquivo CSV de exemplo (dados do TabNet / SINAN)
├── README.md              # Documentação do projeto
├── .gitignore
```

---

## O que o código faz atualmente

Atualmente, o sistema é capaz de:

- Ler arquivos CSV exportados do TabNet
- Realizar a limpeza inicial dos dados
- Identificar as colunas disponíveis
- Processar informações como:
  - Total de casos
  - Distribuição por sexo
  - Organização dos dados por mês de notificação

Essas funcionalidades caracterizam um **teste de consumo e processamento de dados**.

---

## Próximos passos (em desenvolvimento)

- Automatizar o download dos arquivos CSV
- Geração de gráficos e relatórios
- Estruturação automática dos boletins epidemiológicos

---

## Observação para o grupo

Este projeto encontra-se em fase inicial e tem como foco validar a **viabilidade
técnica de leitura e processamento dos dados epidemiológicos**, conforme discutido
no âmbito do PET-Saúde e nas orientações em sala.

---

## Fonte dos dados

- DATASUS / TabNet
