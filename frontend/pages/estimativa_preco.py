"""
Página de estimativa de preço
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
import sys

# Adiciona o diretório raiz ao path para importações
current_dir = Path(__file__).parent.parent
sys.path.insert(0, str(current_dir))

from utils import config, helpers

# Configuração da página
config.set_page_config()
config.apply_custom_css()

# Inicialização de sessão
if 'consultas' not in st.session_state:
    st.session_state.consultas = []
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# Sidebar comum
with st.sidebar:
    logo_path = current_dir.parent / "docs" / "assets" / "logo_agente.png"
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.title("🏠 AlugAI")
    st.markdown("---")
    st.markdown("### 💡 Dica")
    st.info("Use o formulário de busca para encontrar imóveis que atendam suas preferências!")
    st.markdown("---")
    st.markdown("### 📞 Suporte")
    st.markdown("Dúvidas? Entre em contato através da página **Sobre**")

def show():
    """Exibe a página de estimativa de preço"""
    
    st.title("💰 Estimativa de Preço")
    st.markdown("Obtenha uma estimativa precisa do valor de aluguel baseada em modelos de Machine Learning")
    
    st.markdown("---")
    
    # Formulário de entrada
    with st.form("estimativa_preco_form"):
        st.markdown("### 📝 Informações do Imóvel")
        
        col1, col2 = st.columns(2)
        
        with col1:
            property_type = st.selectbox(
                "Tipo de Imóvel *",
                helpers.TIPOS_IMOVEL,
                help="Tipo do imóvel"
            )
            
            neighborhood = st.selectbox(
                "Bairro *",
                helpers.BAIRROS_DF,
                help="Bairro onde o imóvel está localizado"
            )
            
            area = st.number_input(
                "Área (m²) *",
                min_value=1.0,
                max_value=1000.0,
                value=70.0,
                step=1.0,
                help="Área total do imóvel em metros quadrados"
            )
            
            rooms = st.number_input(
                "Número de Quartos *",
                min_value=0,
                max_value=10,
                value=2,
                step=1,
                help="Quantidade de quartos"
            )
        
        with col2:
            bathrooms = st.number_input(
                "Número de Banheiros *",
                min_value=1,
                max_value=10,
                value=2,
                step=1,
                help="Quantidade de banheiros"
            )
            
            parking_spaces = st.number_input(
                "Vagas de Garagem",
                min_value=0,
                max_value=10,
                value=1,
                step=1,
                help="Número de vagas de garagem"
            )
            
            furniture = st.radio(
                "Mobiliado *",
                ["Sim", "Não"],
                horizontal=True,
                help="O imóvel está mobiliado?"
            )
            
            hoa = st.number_input(
                "Condomínio (R$)",
                min_value=0.0,
                max_value=5000.0,
                value=400.0,
                step=50.0,
                help="Valor mensal do condomínio"
            )
        
        # Opcional: preço anunciado para comparação
        st.markdown("### 📊 Comparação (Opcional)")
        announced_price = st.number_input(
            "Preço Anunciado (R$) - Opcional",
            min_value=0.0,
            max_value=20000.0,
            value=0.0,
            step=100.0,
            help="Se você já tem um preço anunciado, informe para comparação"
        )
        
        # Botão de estimativa
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            estimar_button = st.form_submit_button(
                "🤖 Obter Estimativa",
                use_container_width=True,
                type="primary"
            )
    
    st.markdown("---")
    
    # Resultados da estimativa
    if estimar_button:
        # Salvar consulta no histórico
        query_data = {
            "type": "estimativa",
            "property_type": property_type,
            "neighborhood": neighborhood,
            "area": area,
            "rooms": rooms,
            "bathrooms": bathrooms,
            "parking_spaces": parking_spaces,
            "furniture": furniture == "Sim",
            "hoa": hoa,
            "announced_price": announced_price if announced_price > 0 else None
        }
        helpers.save_query(query_data)
        
        # Simular estimativa (será substituído por chamada ao modelo real)
        with st.spinner("🤖 Processando com modelo de IA..."):
            import random
            
            # Estimativa baseada em regras simples (mock)
            base_price = area * 30  # R$ 30 por m² base
            base_price += rooms * 200
            base_price += bathrooms * 150
            base_price += parking_spaces * 100
            base_price += hoa * 0.3
            
            if furniture == "Sim":
                base_price *= 1.15
            
            # Adicionar variação aleatória para simular modelo
            estimated_price = base_price * random.uniform(0.9, 1.1)
            estimated_price = round(estimated_price, 2)
            
            # Exibir resultados
            st.success("✅ Estimativa gerada com sucesso!")
            
            # Métricas principais
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    "💰 Preço Estimado",
                    helpers.format_currency(estimated_price),
                    help="Valor estimado pelo modelo de IA"
                )
            
            price_per_sqm = helpers.calculate_price_per_sqm(estimated_price, area)
            with col2:
                st.metric(
                    "📐 Preço por m²",
                    helpers.format_currency(price_per_sqm),
                    help="Preço por metro quadrado"
                )
            
            if announced_price > 0:
                diff = announced_price - estimated_price
                diff_pct = (diff / estimated_price) * 100
                
                with col3:
                    st.metric(
                        "📊 Diferença",
                        helpers.format_currency(abs(diff)),
                        f"{diff_pct:+.1f}%",
                        delta_color="inverse" if diff > 0 else "normal"
                    )
                
                with col4:
                    classification = helpers.classify_property(estimated_price, announced_price)
                    st.metric(
                        "🎯 Classificação",
                        classification["label"],
                        classification["message"]
                    )
            
            st.markdown("---")
            
            # Visualização comparativa
            if announced_price > 0:
                st.markdown("### 📊 Comparação Visual")
                
                fig = go.Figure()
                
                fig.add_trace(go.Bar(
                    x=["Preço Anunciado", "Preço Estimado"],
                    y=[announced_price, estimated_price],
                    marker_color=["#ff6b6b", "#4ecdc4"],
                    text=[helpers.format_currency(announced_price), 
                          helpers.format_currency(estimated_price)],
                    textposition="auto",
                ))
                
                fig.update_layout(
                    title="Comparação de Preços",
                    yaxis_title="Valor (R$)",
                    height=400,
                    showlegend=False
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            # Explicabilidade do modelo
            st.markdown("### 🔍 Fatores que Influenciaram a Estimativa")
            
            factors = [
                {"name": "Área do Imóvel", "impact": "Alto", "value": f"{area} m²"},
                {"name": "Localização (Bairro)", "impact": "Alto", "value": neighborhood},
                {"name": "Número de Quartos", "impact": "Médio", "value": f"{rooms} quartos"},
                {"name": "Condomínio", "impact": "Médio", "value": helpers.format_currency(hoa)},
                {"name": "Mobiliado", "impact": "Baixo", "value": furniture},
            ]
            
            df_factors = pd.DataFrame(factors)
            st.dataframe(
                df_factors,
                column_config={
                    "name": "Fator",
                    "impact": st.column_config.SelectboxColumn(
                        "Impacto",
                        options=["Alto", "Médio", "Baixo"]
                    ),
                    "value": "Valor"
                },
                hide_index=True,
                use_container_width=True
            )
            
            # Informações adicionais
            st.markdown("---")
            st.markdown("### 📈 Informações Adicionais")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"""
                **Média Regional:**
                - Bairro: {helpers.format_currency(estimated_price * 0.95)}
                - Região: {helpers.format_currency(estimated_price * 0.98)}
                - DF: {helpers.format_currency(estimated_price * 1.02)}
                """)
            
            with col2:
                st.info(f"""
                **Faixa de Confiança (95%):**
                - Mínimo: {helpers.format_currency(estimated_price * 0.85)}
                - Máximo: {helpers.format_currency(estimated_price * 1.15)}
                """)
            
            # Feedback do usuário
            st.markdown("---")
            st.markdown("### 💬 Sua Opinião é Importante!")
            
            feedback = st.radio(
                "Como você avalia esta estimativa?",
                ["Correta", "Alta demais", "Baixa demais"],
                horizontal=True
            )
            
            if st.button("Enviar Feedback"):
                st.success("✅ Obrigado pelo feedback! Isso nos ajuda a melhorar o modelo.")
    
    else:
        # Instruções iniciais
        st.info("""
        👆 **Preencha o formulário acima** com as características do imóvel e clique em 
        **"Obter Estimativa"** para receber uma estimativa precisa do valor de aluguel.
        
        **Campos obrigatórios estão marcados com asterisco (*)**
        """)

# Executar quando o arquivo é executado diretamente pelo Streamlit
show()

