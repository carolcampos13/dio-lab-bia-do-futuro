# Base de Conhecimento

## Dados Utilizados

Disponível na pasta data:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `base_conhecimento.json` | JSON | Base de conhecimento |
| `dados_cliente.json` | JSON | Dados do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados originais do repositório base foram substituídos por um modelo de autoria própria. Foi desenvolvida uma estrutura personalizada em JSON para segmentar as regras financeiras estáveis (base de conhecimento) e as variáveis dinâmicas do perfil de teste do usuário.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON são lidos e desserializados pelo backend em Python no início da execução da aplicação. Em seguida, essas estruturas de dados são injetadas diretamente nas diretrizes de contexto enviadas à API do modelo de linguagem.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O arquivo base_conhecimento.json irá no system prompt para informar a IA o que pode ser dito ou não e serão consultados dinamicamente quando necessário.

---

## Exemplo de Contexto Montado


=== CONTEXTO DO SISTEMA (BASE DE CONHECIMENTO) ===
- Regras de Reserva:
  * CLT: 3 a 6 meses de custo de vida.
  * Autônomo: 6 a 12 meses de custo de vida.
- Marcos de Evolução:
  * Marco 1: Juntar 1 mês de custo de vida.
  * Marco 2: Alcançar 3 meses.
  * Marco 3: Alcançar 6 meses.
  * Marco Final: Alcançar 12 meses.
- Investimentos Recomendados (Baixo Risco):
  * Tesouro Selic (Título Público, Liquidez Diária D+1).
  * CDB 100% do CDI (Título Bancário, Liquidez Diária Imediata, Proteção FGC).

=== DADOS DO CLIENTE ATUAL ===
- Nome: João
- Tipo de Profissão: Autônomo
- Renda Mensal: R$ 3.000,00
- Custo de Vida Mensal: R$ 2.000,00

=== STATUS ATUAL DA RESERVA ===
- Meta Final (12 meses): R$ 24.000,00
- Total Guardado: R$ 150,00
- Último Depósito: R$ 50,00
- Progresso Atual: Focado no Marco 1 (Faltam R$ 1.850,00 para atingir 1 mês de custo de vida).

---
