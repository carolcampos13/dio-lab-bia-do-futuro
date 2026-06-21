# 🤖 Fin — Seu Mentor de Reserva de Emergência

O **Fin** é um assistente financeiro inteligente desenvolvido sob medida para ajudar as pessoas a construírem e manterem uma reserva de emergência estável. Utilizando modelos de linguagem avançados através da API do Gemini e uma interface web interativa em Streamlit, o Fin humaniza o planejamento financeiro, transformando dados complexos em uma jornada visual, amigável e acolhedora.

---

## 🎬 Demonstração em Vídeo

Assista ao nosso Pitch e veja o Fin funcionando na prática, calculando metas em tempo real e interagindo de forma inteligente:

[![Assista ao Pitch do Fin](https://img.shields.io/badge/Clique_Aqui_para_Assistir-Pitch_Fin-E31837?style=for-the-badge&logo=google-drive&logoColor=white)](https://drive.google.com/file/d/16yEZ4ZTdhI6xThe2vPncIz580CK_hnY1/view?usp=sharing)

🔗 [Link direto de acesso no Google Drive](https://drive.google.com/file/d/16yEZ4ZTdhI6xThe2vPncIz580CK_hnY1/view?usp=sharing)

---

## 📁 Estrutura do Repositório

O projeto está organizado de forma modular, separando as camadas de código, dados e documentação técnica:

```text
📁 meu-projeto-fin/
│
├── 📄 .gitignore                 # Arquivos ignorados no controle de versão
├── 📄 README.md                  # Este guia principal do repositório
├── 📄 requirements.txt           # Dependências e bibliotecas do projeto
│
├── 📂 assets/                    # Evidências visuais e capturas de tela dos testes
│   └── 📝 README.md
│
├── 📂 data/                      # Base de dados persistentes (JSON)
│   ├── 📄 base_conhecimento.json # Regras de negócios e conceitos de finanças
│   └── 📄 dados_cliente.json     # Carteira, saldos e progresso do cliente atual
│
├── 📂 docs/                      # Documentação detalhada de cada etapa
│   ├── 📄 01-documentacao-agente.md
│   ├── 📄 02-base-conhecimento.md
│   ├── 📄 03-prompts.md
│   ├── 📄 04-metricas.md
│   └── 📄 05-pitch.md
│
└── 📂 src/                       # Código-fonte da aplicação
    ├── 📝 README.md              # Instruções específicas de execução do código
    └── 🐍 main.py                # Interface Streamlit e integração com a API do Gemini
```

---

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem base)
* **Streamlit** (Interface de usuário interativa)
* **Google GenAI SDK** (Integração com o modelo generativo Gemini)
* **JSON** (Persistência estruturada de dados e base de conhecimento)

---

## 🚀 Como Executar o Projeto

### 1. Instale as Dependências
Abra o terminal na raiz do projeto e execute o comando:
```bash
pip install -r requirements.txt
```

### 2. Inicie a Aplicação com sua API Key
Insira sua chave gerada no Google AI Studio e execute o comando de acordo com o seu sistema operacional:

* **Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="SUA_API_KEY_AQUI"; streamlit run src/main.py
  ```

* **Linux / macOS (Bash):**
  ```bash
  GEMINI_API_KEY="SUA_API_KEY_AQUI" streamlit run src/main.py
  ```

---

## ⚖️ Critérios de Qualidade e Segurança

O Fin foi homologado sob métricas rígidas de qualidade para garantir uma experiência segura:
* **Assertividade:** Respostas precisas com base nos dados reais do cliente.
* **Segurança (Guardrails):** Filtros rígidos que impedem alucinações, vazamento de escopo técnico ou indicação de ativos voláteis.
* **Coerência:** Tom de voz informal, amigável e totalmente adaptado ao perfil financeiro de trabalhadores autônomos.
