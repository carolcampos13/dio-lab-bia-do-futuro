# # Código da Aplicação

Esta pasta contém a implementação em código do assistente financeiro **Fin**.

## ## Estrutura do Projeto

A arquitetura completa do diretório está estruturada visualmente da seguinte forma, separando claramente as camadas de código, documentação e dados persistentes:

```text
📁 meu-projeto-fin/
│
├── 📂 assets/                # Evidências visuais e capturas dos testes de qualidade
│   ├── 📝 README.md
│   └── 📸 ... (imagens de teste e da interface)
│
├── 📂 data/                  # Base de dados persistentes do sistema (JSON)
│   ├── 📄 base_conhecimento.json
│   └── 📄 dados_cliente.json
│
├── 📂 docs/                  # Documentação detalhada das etapas do desafio
│   ├── 📄 01-documentacao-agente.md
│   ├── 📄 02-base-conhecimento.md
│   ├── 📄 03-prompts.md
│   ├── 📄 04-metricas.md
│   └── 📄 05-pitch.md
│
├── 📂 examples/              # Exemplos e referências do template
│   └── 📝 README.md
│
├── 📂 src/                   # Código-fonte principal da aplicação
│   ├── 📝 README.md          # Guia de documentação e execução do código (Este arquivo)
│   └── 🐍 main.py            # Interface Streamlit e integração com a Gemini API
│
├── 📄 .gitignore             # Arquivos ignorados no controle de versão
├── 📄 README.md              # Documentação principal na raiz do repositório
└── 📄 requirements.txt       # Dependências e bibliotecas do projeto
```

## ## Requisitos de Instalação (`requirements.txt`)

As dependências necessárias para a execução deste projeto estão listadas na raiz do repositório. Certifique-se de utilizar o SDK oficial mais recente do Google GenAI:

```text
streamlit
google-genai
```

## ## Como Rodar a Aplicação

Siga o passo a passo abaixo no terminal para configurar o ambiente e executar o assistente localmente:

### ### 1. Instalar as Dependências
Navegue até a raiz do projeto e execute o comando para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### ### 2. Executar o Streamlit com a Chave de API
Para garantir a segurança da aplicação, a chave de API do Gemini deve ser injetada como uma variável de ambiente em tempo de execução. 

Substitua `SUA_API_KEY_AQUI` pelas suas credenciais geradas no Google AI Studio e execute o comando correspondente ao seu terminal:

* **No Windows (PowerShell):**
```powershell
  $env:GEMINI_API_KEY="SUA_API_KEY_AQUI"; streamlit run src/main.py
  ```

* **No Linux / macOS (Bash) ou Prompt de Comando (CMD):**
```bash
  GEMINI_API_KEY="SUA_API_KEY_AQUI" streamlit run src/main.py
  ```

---
*Nota: A aplicação inicializará automaticamente o painel dinâmico da barra lateral integrado aos dados persistentes do cliente João e abrirá a interface do chat de mentoria financeira no seu navegador padrão.*
```
