"""
Página de busca de imóveis
"""

import streamlit as st
import pandas as pd
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
    """Exibe a página de busca de imóveis"""
    
    st.title("🔍 Buscar Imóveis")
    st.markdown("Encontre imóveis que atendam suas preferências e veja a classificação automática de custo-benefício")
    
    st.markdown("---")
    
    # Formulário de busca
    with st.form("buscar_imoveis_form"):
        st.markdown("### 📝 Preferências do Imóvel")
        
        col1, col2 = st.columns(2)
        
        with col1:
            property_type = st.selectbox(
                "Tipo de Imóvel",
                ["Todos"] + helpers.TIPOS_IMOVEL,
                help="Selecione o tipo de imóvel desejado"
            )
            
            neighborhood = st.selectbox(
                "Bairro",
                ["Todos"] + helpers.BAIRROS_DF,
                help="Selecione o bairro desejado"
            )
            
            min_area = st.number_input(
                "Área Mínima (m²)",
                min_value=0,
                max_value=500,
                value=0,
                step=10,
                help="Área mínima em metros quadrados"
            )
            
            max_area = st.number_input(
                "Área Máxima (m²)",
                min_value=0,
                max_value=500,
                value=300,
                step=10,
                help="Área máxima em metros quadrados"
            )
        
        with col2:
            rooms = st.slider(
                "Número de Quartos",
                min_value=0,
                max_value=5,
                value=(1, 4),
                help="Faixa de número de quartos"
            )
            
            bathrooms = st.slider(
                "Número de Banheiros",
                min_value=1,
                max_value=5,
                value=(1, 3),
                help="Faixa de número de banheiros"
            )
            
            parking_spaces = st.slider(
                "Vagas de Garagem",
                min_value=0,
                max_value=5,
                value=(0, 2),
                help="Faixa de número de vagas"
            )
            
            furniture = st.radio(
                "Mobiliado",
                ["Todos", "Sim", "Não"],
                horizontal=True
            )
        
        # Filtros adicionais
        st.markdown("### 💰 Faixa de Preço")
        
        col1, col2 = st.columns(2)
        with col1:
            min_price = st.number_input(
                "Preço Mínimo (R$)",
                min_value=0,
                max_value=10000,
                value=1000,
                step=100
            )
        with col2:
            max_price = st.number_input(
                "Preço Máximo (R$)",
                min_value=0,
                max_value=10000,
                value=5000,
                step=100
            )
        
        # Botão de busca
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            buscar_button = st.form_submit_button(
                "🔍 Buscar Imóveis",
                use_container_width=True,
                type="primary"
            )
    
    st.markdown("---")
    
    # Resultados da busca
    if buscar_button:
        # Salvar consulta no histórico
        query_data = {
            "type": "busca",
            "property_type": property_type,
            "neighborhood": neighborhood,
            "min_area": min_area,
            "max_area": max_area,
            "rooms": rooms,
            "bathrooms": bathrooms,
            "parking_spaces": parking_spaces,
            "furniture": furniture,
            "min_price": min_price,
            "max_price": max_price
        }
        helpers.save_query(query_data)
        
        # Gerar resultados mock (será substituído por busca real)
        with st.spinner("Buscando imóveis..."):
            properties = helpers.generate_mock_properties(count=8)
            
            # Aplicar filtros
            filtered_properties = []
            for prop in properties:
                if property_type != "Todos" and prop["property_type"] != property_type:
                    continue
                if neighborhood != "Todos" and prop["neighborhood"] != neighborhood:
                    continue
                if not (min_area <= prop["area"] <= max_area):
                    continue
                if not (rooms[0] <= prop["rooms"] <= rooms[1]):
                    continue
                if not (bathrooms[0] <= prop["bathrooms"] <= bathrooms[1]):
                    continue
                if not (parking_spaces[0] <= prop["parking_spaces"] <= parking_spaces[1]):
                    continue
                if furniture == "Sim" and not prop.get("furniture", False):
                    continue
                if furniture == "Não" and prop.get("furniture", False):
                    continue
                if not (min_price <= prop["announced_price"] <= max_price):
                    continue
                
                filtered_properties.append(prop)
            
            if filtered_properties:
                st.success(f"✅ Encontrados {len(filtered_properties)} imóveis que atendem suas preferências!")
                
                # Classificar por vantajosidade
                for prop in filtered_properties:
                    classification = helpers.classify_property(
                        prop["estimated_price"],
                        prop["announced_price"]
                    )
                    prop["classification"] = classification
                
                # Ordenar por vantajosidade (mais vantajosos primeiro)
                filtered_properties.sort(key=lambda x: x["classification"]["diff_pct"])
                
                # Exibir resultados
                st.markdown("### 📋 Resultados da Busca")
                
                for prop in filtered_properties:
                    st.markdown(helpers.create_property_card(prop), unsafe_allow_html=True)
                    
                    # Botões de ação
                    col1, col2, col3 = st.columns([1, 1, 1])
                    with col1:
                        if st.button(f"💰 Ver Detalhes", key=f"details_{prop['id']}"):
                            st.info(f"Detalhes completos do imóvel {prop['id']} serão exibidos aqui")
                    with col2:
                        if st.button(f"📊 Comparar Preços", key=f"compare_{prop['id']}"):
                            st.info("Redirecionando para página de comparação...")
                    with col3:
                        if st.button(f"⭐ Favoritar", key=f"fav_{prop['id']}"):
                            if prop['id'] not in st.session_state.favoritos:
                                st.session_state.favoritos.append(prop['id'])
                                st.success("Adicionado aos favoritos!")
                            else:
                                st.info("Já está nos favoritos")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ Nenhum imóvel encontrado com os filtros selecionados. Tente ajustar suas preferências.")
                
                # Sugestões
                st.info("💡 **Dicas:**\n"
                       "- Tente aumentar a faixa de preço\n"
                       "- Considere outros bairros\n"
                       "- Ajuste o número de quartos ou área")
    
    else:
        # Mensagem inicial
        st.info("👆 Preencha o formulário acima e clique em 'Buscar Imóveis' para começar sua busca!")

# Executar quando o arquivo é executado diretamente pelo Streamlit
show()

