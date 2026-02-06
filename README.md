# Simple CRUD API

API REST simples desenvolvida com **FastAPI** para demonstrar operações básicas de **CRUD** utilizando banco de dados relacional.

Este projeto faz parte de uma coleção de projetos com foco em **backend** para fins de estudo e portfólio.

---

## 🚀 Tecnologias Utilizadas
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

## 📦 Funcionalidades
- Criar item
- Listar itens
- Buscar item por ID
- Deletar item
- Documentação automática com Swagger

---

## 🗂️ Estrutura do Projeto
```text
simple-crud-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       └── items.py
```

## 📌 Sobre os Itens

Um item representa um objeto genérico de cadastro, contendo:
- Nome
- Descrição

Esse modelo foi escolhido para simplificar o aprendizado de CRUD.

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd simple-crud-api
```

### 2️⃣ Criar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
```
Ativar no Windows:
```powershell
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar a aplicação
```bash
python -m uvicorn app.main:app --reload
```
A API estará disponível em:

http://127.0.0.1:8000

Documentação Swagger: http://127.0.0.1:8000/docs

---

## 🔗 Endpoints Principais

Criar item
```http
POST /items/
```

Exemplo de body:
```json
{
  "name": "Mouse Gamer",
  "description": "Mouse com 6 botões e RGB"
}
```
Listar itens
```http
GET /items/
```
Buscar item por ID
```http
GET /items/{item_id}
```
Deletar item
```http
DELETE /items/{item_id}
```


