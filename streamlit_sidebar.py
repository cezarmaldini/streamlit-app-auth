import streamlit as st
from streamlit_option_menu import option_menu

# Navegação da Aplicação
with st.sidebar:
    option = option_menu(
        menu_title="Navegação",
        options=["Vagas", "Upload", "Relatórios"],
        icons=["database-add", "folder-plus", "robot"],
        menu_icon="card-list",
        default_index=0
    )
          
    # Botão de logout na sidebar
    if st.button("🚪 Sair", use_container_width=True):
        st.logout()
        st.rerun()