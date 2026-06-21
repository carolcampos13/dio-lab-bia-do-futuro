import streamlit as st
import json
import os
from google import genai

# 1. ENCONTRA O CAMINHO ABSOLUTO DOS ARQUIVOS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define os caminhos subindo uma pasta (..) e entrando em 'data'
CONHECIMENTO_PATH = os.path.join(BASE_DIR, "..", "data", "base_conhecimento.json")
CLIENTE_PATH = os.path.join(BASE_DIR, "..", "data", "dados_cliente.json")

# Carrega a base de conhecimento
with open(CONHECIMENTO_PATH, 'r', encoding='utf-8') as f:
    base_conhecimento = json.load(f)

# Inicializa os dados do cliente na memória se não existirem
if "dados_cliente" not in st.session_state:
    with open(CLIENTE_PATH, 'r', encoding='utf-8') as f:
        st.session_state.dados_cliente = json.load(f)

# Função de salvar atualizada com o caminho absoluto
def salvar_dados_cliente():
    """Grava o estado atual da memória de volta no arquivo JSON."""
    with open(CLIENTE_PATH, 'w', encoding='utf-8') as f:
        json.dump(st.session_state.dados_cliente, f, ensure_ascii=False, indent=2)

# === 2. CONFIGURAÇÃO DO PROMPT DE SISTEMA (CORRIGIDO) ===

# Geramos os textos do JSON fora do prompt primeiro para evitar confusão de chaves
dados_conhecimento_txt = json.dumps(base_conhecimento, ensure_ascii=False, indent=2)
dados_joao_txt = json.dumps(st.session_state.dados_cliente, ensure_ascii=False, indent=2)

system_prompt_completo = f"""
Você é um agente financeiro inteligente chamado Fin, especializado em mentoria para reservas de emergência.
O seu objetivo principal é fazer com que as pessoas consigam chegar a meta final de 12 meses para ter a reserva de emergência perfeita.
Somente 9% da população brasileira tem uma reserva de emergência.

REGRAS:
1. Você será amigável, acolhedor, despojado e gentil o tempo todo. Não julgue o usuário.
2. Você responderá em linguagem informal e acessível, como se fosse um amigo.
3. Você só responderá com base nos dados fornecidos na Base de Conhecimento abaixo.
4. Sempre que houver uma pergunta fora do escopo, peça desculpas de forma amigável, assuma que não sabe e retorne ao assunto da reserva.
5. Você não irá inventar dados ou estimativas financeiras de maneira alguma.
6. Você sempre irá respeitar o sigilo do cliente e nunca exporá dados de outros usuários.
7. Use as informações do cliente atual para parabenizá-lo e calcular os próximos marcos de forma personalizada.
8. ATENÇÃO: Faça os cálculos matemáticos você mesmo e responda apenas o texto puro com os valores finais. NUNCA exiba códigos, chaves ou termos técnicos de programação como 'st.session_state' ou dicionários na sua resposta. Você fala como um humano e não como um script.

=== BASE DE CONHECIMENTO (Regras e Investimentos) ===
{dados_conhecimento_txt}

=== DADOS DO CLIENTE ATUAL ===
{dados_joao_txt}
"""

# 3. INICIALIZAÇÃO DO CLIENTE GOOGLE GENAI
client = genai.Client()

config = genai.types.GenerateContentConfig(
    system_instruction=system_prompt_completo,
    temperature=0.7
)

# 4. DESIGN DA BARRA LATERAL (Ajustado para a estrutura correta do JSON)
with st.sidebar:
    st.header("📊 Seu Progresso")
    
    dados = st.session_state.dados_cliente
    
    # 🔍 ACESSANDO OS CORDÕES CORRETOS DO JSON (image_6458c7.png)
    perfil = dados.get("perfil_cliente", {})
    historico = dados.get("historico_reserva", {})
    
    nome_cliente = perfil.get("nome", "Cliente")
    st.subheader(f"Olá, {nome_cliente}!")
    st.divider()
    
    meta_total = historico.get("meta_final_12_meses", 0.0)
    guardado_atual = historico.get("total_guardado_atual", 0.0)
    
    # Métricas visuais na tela
    st.metric(label="Sua Meta Perfeita (12 Meses)", value=f"R$ {meta_total:,.2f}")
    st.metric(label="Total Guardado em Conta", value=f"R$ {guardado_atual:,.2f}")
    
    porcentagem = (guardado_atual / meta_total) * 100 if meta_total > 0 else 0
    st.progress(min(porcentagem / 100, 1.0))
    st.caption(f"Você já conquistou **{porcentagem:.1f}%** da sua reserva!")
    
    st.divider()
    st.subheader("💰 Atualizar Saldo")
    
    valor_input = st.number_input("Quanto você poupou hoje?", min_value=0.0, step=50.0, format="%.2f")
    
    if st.button("➕ Adicionar à Reserva"):
        if valor_input > 0:
            # Altera a chave exata dentro do bloco historico_reserva na memória
            st.session_state.dados_cliente["historico_reserva"]["total_guardado_atual"] += valor_input
            # Salva no disco
            salvar_dados_cliente()
            st.success(f"R$ {valor_input:,.2f} adicionados com sucesso!")
            st.rerun()

# 5. CORPO PRINCIPAL DO CHAT
st.title("💰 Fin - Seu Mentor de Reserva de Emergência")
st.subheader("Construindo sua tranquilidade financeira passo a passo.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": '''Olá, meu nome é Fin! Seu assistente de reservas emergenciais!
         Vamos fazer uma reserva de emergência? Não é tão difícil, acredito em você!'''}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 6. FLUXO DE INTERAÇÃO DO CHAT
if prompt := st.chat_input("Como posso te ajudar com a sua reserva hoje?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    contents = []
    for msg in st.session_state.messages:
        role = "model" if msg["role"] == "assistant" else "user"
        contents.append(
            genai.types.Content(
                role=role,
                parts=[genai.types.Part.from_text(text=msg["content"])]
            )
        )

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=contents,
                config=config
            )
            
            resposta_do_fin = response.text
            response_placeholder.write(resposta_do_fin)
            st.session_state.messages.append({"role": "assistant", "content": resposta_do_fin})
            
        except Exception as e:
            # Se der erro 503 ou qualquer oscilação de rede, o app exibe o aviso mas não quebra
            st.error(f"Eita, o Fin ficou pensativo devido à alta demanda nos servidores. Vamos tentar de novo? Erro: {e}")