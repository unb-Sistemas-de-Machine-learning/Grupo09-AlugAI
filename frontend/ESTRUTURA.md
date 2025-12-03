# 📁 Estrutura do Frontend AlugAI

## Visão Geral

O frontend do AlugAI foi desenvolvido em Streamlit, seguindo uma arquitetura modular e organizada para facilitar manutenção e expansão futura.

## Estrutura de Diretórios

```
frontend/
├── app.py                          # Aplicação principal e roteamento
├── pages/                          # Módulos de páginas
│   ├── __init__.py
│   ├── home.py                     # Página inicial
│   ├── buscar_imoveis.py           # Busca e filtros de imóveis
│   ├── estimativa_preco.py         # Estimativa de preço com ML
│   ├── comparativo_regional.py     # Análises e mapas regionais
│   ├── historico.py                # Histórico de consultas
│   └── sobre.py                    # Informações do projeto
├── utils/                          # Utilitários e helpers
│   ├── __init__.py
│   ├── config.py                   # Configurações e CSS
│   └── helpers.py                  # Funções auxiliares
├── .streamlit/                     # Configurações do Streamlit
│   └── config.toml
├── requirements.txt                # Dependências Python
├── README.md                       # Documentação principal
├── INICIO_RAPIDO.md                # Guia de início rápido
├── ESTRUTURA.md                    # Este arquivo
├── run.sh                          # Script de execução (Linux/Mac)
├── run.bat                         # Script de execução (Windows)
└── .gitignore                      # Arquivos ignorados pelo Git
```

## Arquitetura

### 1. app.py (Aplicação Principal)
- Configuração inicial do Streamlit
- Gerenciamento de estado da sessão
- Roteamento entre páginas
- Sidebar com navegação

### 2. pages/ (Módulos de Páginas)
Cada página é um módulo independente com função `show()`:

- **home.py**: Apresentação do projeto, estatísticas e call-to-action
- **buscar_imoveis.py**: Formulário de busca completo com filtros e resultados
- **estimativa_preco.py**: Formulário de estimativa e visualização de resultados
- **comparativo_regional.py**: Mapas interativos, gráficos e tabelas comparativas
- **historico.py**: Listagem e gerenciamento do histórico de consultas
- **sobre.py**: Informações sobre o projeto, equipe e tecnologias

### 3. utils/ (Utilitários)

#### config.py
- `set_page_config()`: Configurações da página Streamlit
- `apply_custom_css()`: Estilos CSS customizados

#### helpers.py
- `format_currency()`: Formatação de valores monetários
- `calculate_price_per_sqm()`: Cálculo de preço por m²
- `classify_property()`: Classificação de custo-benefício
- `save_query()`: Salvamento de consultas no histórico
- `create_property_card()`: Geração de cards HTML para imóveis
- `generate_mock_properties()`: Geração de dados mock para desenvolvimento
- Constantes: `BAIRROS_DF`, `TIPOS_IMOVEL`

## Fluxo de Dados

### Busca de Imóveis
1. Usuário preenche formulário
2. Dados são validados e filtrados
3. Consulta é salva no histórico
4. Resultados são exibidos com classificação

### Estimativa de Preço
1. Usuário preenche características do imóvel
2. Dados são enviados para modelo (mock atual)
3. Estimativa é calculada e exibida
4. Comparação com preço anunciado (se fornecido)
5. Fatores de influência são mostrados
6. Consulta é salva no histórico

### Histórico
1. Consultas são recuperadas da sessão
2. Filtros são aplicados
3. Dados são exibidos em formato expandível
4. Exportação para CSV disponível

## Estado da Sessão

O Streamlit mantém estado através de `st.session_state`:

- `consultas`: Lista de consultas realizadas
- `favoritos`: Lista de IDs de imóveis favoritados

## Dependências

### Principais
- `streamlit`: Framework web
- `pandas`: Manipulação de dados
- `plotly`: Visualizações interativas
- `numpy`: Operações numéricas

### Futuras (para integração com ML)
- `scikit-learn`: Modelos de ML
- `xgboost`: Modelo de regressão
- `joblib` ou `pickle`: Carregamento de modelos

## Próximos Passos

1. **Integração com Modelo de ML**
   - Carregar modelo treinado (XGBoost)
   - Substituir estimativas mock por predições reais

2. **Integração com Banco de Dados**
   - Conectar com fonte de dados real
   - Substituir dados mock por consultas reais

3. **Persistência de Dados**
   - Implementar armazenamento de histórico em banco
   - Sistema de favoritos persistente

4. **Melhorias de UX**
   - Loading states mais elaborados
   - Tratamento de erros robusto
   - Validação de formulários aprimorada

5. **Performance**
   - Cache de consultas frequentes
   - Otimização de visualizações
   - Lazy loading de dados

## Convenções de Código

- **Nomes de funções**: snake_case
- **Nomes de classes**: PascalCase
- **Constantes**: UPPER_SNAKE_CASE
- **Docstrings**: Formato Google Style
- **Imports**: Agrupados (stdlib, third-party, local)

## Testes

Estrutura sugerida para testes futuros:
```
tests/
├── test_helpers.py
├── test_pages.py
└── test_integration.py
```

