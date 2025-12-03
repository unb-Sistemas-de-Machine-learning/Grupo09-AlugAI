"""
Página de histórico de consultas
"""

import streamlit as st
import pandas as pd
from datetime import datetime
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
    """Exibe a página de histórico"""
    
    st.title("📜 Histórico de Consultas")
    st.markdown("Revise suas consultas anteriores e acompanhe suas buscas")
    
    st.markdown("---")
    
    # Verificar se há histórico
    if not st.session_state.consultas:
        st.info("📭 Você ainda não realizou nenhuma consulta. Comece buscando imóveis ou estimando preços!")
        return
    
    # Estatísticas rápidas
    total_consultas = len(st.session_state.consultas)
    consultas_busca = sum(1 for q in st.session_state.consultas if q.get("type") == "busca")
    consultas_estimativa = sum(1 for q in st.session_state.consultas if q.get("type") == "estimativa")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Consultas", total_consultas)
    
    with col2:
        st.metric("Buscas Realizadas", consultas_busca)
    
    with col3:
        st.metric("Estimativas Geradas", consultas_estimativa)
    
    st.markdown("---")
    
    # Filtros
    col1, col2 = st.columns(2)
    
    with col1:
        filter_type = st.selectbox(
            "Filtrar por Tipo",
            ["Todos", "Busca", "Estimativa"]
        )
    
    with col2:
        sort_order = st.selectbox(
            "Ordenar por",
            ["Mais Recentes", "Mais Antigas"]
        )
    
    # Filtrar e ordenar consultas
    filtered_queries = st.session_state.consultas.copy()
    
    if filter_type != "Todos":
        query_type = "busca" if filter_type == "Busca" else "estimativa"
        filtered_queries = [q for q in filtered_queries if q.get("type") == query_type]
    
    if sort_order == "Mais Recentes":
        filtered_queries.reverse()
    
    st.markdown(f"### 📋 Consultas ({len(filtered_queries)} encontradas)")
    
    # Exibir consultas
    for idx, query in enumerate(filtered_queries):
        with st.expander(f"🔍 {query.get('type', 'Consulta').title()} - {query.get('timestamp', 'Sem data')}", expanded=(idx == 0)):
            if query.get("type") == "busca":
                st.markdown("**Tipo:** Busca de Imóveis")
                st.markdown(f"""
                - **Tipo de Imóvel:** {query.get('property_type', 'N/A')}
                - **Bairro:** {query.get('neighborhood', 'N/A')}
                - **Área:** {query.get('min_area', 0)} - {query.get('max_area', 0)} m²
                - **Quartos:** {query.get('rooms', 'N/A')}
                - **Banheiros:** {query.get('bathrooms', 'N/A')}
                - **Vagas:** {query.get('parking_spaces', 'N/A')}
                - **Mobiliado:** {query.get('furniture', 'N/A')}
                - **Faixa de Preço:** {helpers.format_currency(query.get('min_price', 0))} - {helpers.format_currency(query.get('max_price', 0))}
                """)
                
                if st.button(f"🔁 Repetir Busca", key=f"repeat_busca_{idx}"):
                    st.info("Redirecionando para página de busca...")
            
            elif query.get("type") == "estimativa":
                st.markdown("**Tipo:** Estimativa de Preço")
                st.markdown(f"""
                - **Tipo de Imóvel:** {query.get('property_type', 'N/A')}
                - **Bairro:** {query.get('neighborhood', 'N/A')}
                - **Área:** {query.get('area', 0)} m²
                - **Quartos:** {query.get('rooms', 'N/A')}
                - **Banheiros:** {query.get('bathrooms', 'N/A')}
                - **Vagas:** {query.get('parking_spaces', 'N/A')}
                - **Mobiliado:** {'Sim' if query.get('furniture') else 'Não'}
                - **Condomínio:** {helpers.format_currency(query.get('hoa', 0))}
                """)
                
                if query.get("announced_price"):
                    st.markdown(f"- **Preço Anunciado:** {helpers.format_currency(query.get('announced_price', 0))}")
                
                if st.button(f"🔁 Nova Estimativa", key=f"repeat_estimativa_{idx}"):
                    st.info("Redirecionando para página de estimativa...")
            
            # Botão para remover
            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button(f"🗑️ Remover", key=f"remove_{idx}"):
                    st.session_state.consultas.remove(query)
                    st.rerun()
    
    st.markdown("---")
    
    # Ações em lote
    st.markdown("### ⚙️ Ações")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🗑️ Limpar Todo o Histórico", use_container_width=True):
            st.session_state.consultas = []
            st.rerun()
    
    with col2:
        # Exportar para CSV
        if filtered_queries:
            df_export = pd.DataFrame(filtered_queries)
            csv = df_export.to_csv(index=False)
            st.download_button(
                label="📥 Exportar CSV",
                data=csv,
                file_name=f"historico_consultas_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    with col3:
        if st.button("📊 Ver Estatísticas", use_container_width=True):
            st.info("Estatísticas detalhadas serão exibidas aqui")

# Executar quando o arquivo é executado diretamente pelo Streamlit
show()

