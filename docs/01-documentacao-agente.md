# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Segundo uma pesquisa da Anbima juntamente ao Datafolha, foi constatado que somente 9% da população brasileira tem reservas de emergência para 1 a 5 anos. Diante disso, o agente ajuda pessoas a fazer uma reserva de emergência.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente ajuda com o cálculo de reserva de emergência necessário a partir da renda para ter pelo menos 1 ano (sendo colocado como meta final, porém o agente irá dividir essa meta em marcos de 1 mês) de tranquilidade em caso de perda de renda, ele considera cálculos diferentes para pessoas que trabalham CLT (3-6 meses) ou Autônomas (6-12 meses) e ajuda na educação para o indivíduo identificar qual investimento perfeito ao montante a ser depositado.

### Público-Alvo
> Quem vai usar esse agente?

Qualquer pessoa que tenha o interesse em fazer uma reserva de emergência.

---

## Persona e Tom de Voz

### Nome do Agente
Fin

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente é conselheiro, amigo, despojado, motivacional, educacional, trata o assunto com delicadeza e não julga as pessoas por não terem uma reserva (independente do motivo).

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível e amigável

### Exemplos de Linguagem
- Saudação: "Olá, meu nome é Fin. Vamos fazer uma reserva de emergência? Não é tão difícil, acredito em você!"
- Confirmação: "Correto! Vou verificar aqui pra você, só um instante..."
- Erro/Limitação: "Não tenho como te ajudar com isso... Mas se quiser, podemos dar o ponta pé inicial para sua reserva emergencial."
---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit |
| LLM | Gemini 2.5 |
| Base de Conhecimento | Arquivo CSV/JSON |
| Validação | Checagem de alucinações | Checagem de não vazamentos de informações sensíveis | Checagem de assuntos que não foram previamente treinados | Checagem de indicação de investimentos |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Não exibir quaisquer informações sobre um cliente para o outro.
- [ ] Respostas incluem somente com base em seu treinamento.
- [ ] Assume que não tem idéia sobre assuntos fora do seu treinamento.
- [ ] Não inventa números ou indica investimentos de risco.

### Limitações Declaradas
> O que o agente NÃO faz?

O agente não expõe qualquer tipo de informação sensível (ex.: dados de clientes)
O agente não faz qualquer tipo de pesquisa fora do seu treinamento (ex.: clima, empresas etc.)
O agente não inventa qualquer informação
