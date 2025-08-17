import streamlit as st

# Título e descrição
st.set_page_config(page_title="Morango do Amor", page_icon="🍓", layout="centered")
st.title("🍓 Morango do Amor - Calculadora de Vendas")
st.write("Calcule facilmente o resultado das suas vendas no dia!")

# Entrada do usuário
quantidade = st.number_input("Digite a quantidade de vendas no dia:", min_value=0, step=1)

# Valores fixos
valor_bruto = 10
valor_recebido = 10 - 8
valor_a_prestar = 10 - 2

# Cálculos
valor_total_vendas = valor_bruto * quantidade
valor_liquido_vendas = valor_recebido * quantidade
valor_a_pagar = valor_a_prestar * quantidade

# Exibição dos resultados
st.subheader("📊 Resultados")
st.metric(label="Valor Bruto", value=f"R$ {valor_total_vendas:.2f}")
st.metric(label="Valor Recebido", value=f"R$ {valor_liquido_vendas:.2f}")
st.metric(label="Valor a Pagar", value=f"R$ {valor_a_pagar:.2f}")

# Observação final
st.info("Digite a quantidade de vendas e veja o resultado automático! 🎉")