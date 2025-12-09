"""
AlugAI - Aplicação Principal
Sistema de precificação inteligente de aluguel de imóveis no Distrito Federal
"""

import streamlit as st
from pathlib import Path
import sys

# Adiciona o diretório raiz ao path para importações
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from utils import config

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
    st.info("Use o menu acima para navegar entre as páginas!")
    st.markdown("---")
    st.markdown("### 📞 Suporte")
    st.markdown("Dúvidas? Entre em contato através da página **Sobre**")

# Página inicial
def main():
    """Página inicial do AlugAI"""
    
    st.title("🏠 AlugAI - Precificação Inteligente de Aluguel")
    st.markdown("---")
    
    # Apresentação
    st.markdown("""
    ### Bem-vindo ao AlugAI! 🎉
    
    Sistema inteligente de precificação de aluguel de imóveis no Distrito Federal, 
    utilizando modelos de Machine Learning para estimar valores de aluguel com precisão.
    """)
    
    # Cards de funcionalidades
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 💰 Estimativa de Preço
        Obtenha uma estimativa precisa do valor de aluguel baseada em características do imóvel.
        """)
        st.info("Use a página **Estimativa de Preço** no menu lateral")
    
    with col2:
        st.markdown("""
        ### 🔍 Buscar Imóveis
        Explore imóveis disponíveis no dataset e compare preços anunciados com estimativas do modelo.
        """)
        st.info("Use a página **Buscar Imóveis** no menu lateral")
    
    with col3:
        st.markdown("""
        ### 📊 Comparativo Regional
        Compare preços médios por região e visualize tendências de mercado.
        """)
        st.info("Use a página **Comparativo Regional** no menu lateral")
    
    st.markdown("---")
    
    # Informações técnicas
    st.markdown("### 🛠️ Tecnologias Utilizadas")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Backend:**
        - Python
        - Flask
        - XGBoost (ML)
        - Scikit-learn
        """)
    
    with col2:
        st.markdown("""
        **Frontend:**
        - Streamlit
        - Plotly (Visualizações)
        - Pandas
        """)
    
    st.markdown("---")
    
    # Status da API
    st.markdown("### 🔌 Status da Conexão")
    import os
    import requests
    
    API_URL = os.getenv('API_URL', 'http://localhost:5020')
    
    try:
        response = requests.get(f"{API_URL}/health", timeout=3)
        if response.status_code == 200:
            st.success(f"✅ Backend conectado: {API_URL}")
        else:
            st.warning(f"⚠️ Backend respondeu com status {response.status_code}")
    except requests.exceptions.RequestException:
        if API_URL == 'http://localhost:5020':
            st.info("ℹ️ Modo local - Backend não detectado (normal se não estiver rodando localmente)")
        else:
            st.error(f"❌ Não foi possível conectar ao backend: {API_URL}")
            st.info("💡 Verifique se o backend está online e se a variável API_URL está configurada corretamente")

if __name__ == "__main__":
    main()

