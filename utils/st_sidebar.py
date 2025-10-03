import streamlit as st
from streamlit_option_menu import option_menu


def st_sidebar():
    with st.sidebar:
        option = option_menu(
            menu_title="Navegação",
            options=["Chatbot", "Upload"],
            icons=["robot", "folder-plus"],
            menu_icon="card-list",
            default_index=0
        )
        with st.expander("👤 Perfil", expanded=True):
            st.write(f"**Nome:** {st.user.name}")
            st.write(f"**Email:** {st.user.email}") 
                
        # Botão de logout na sidebar
        if st.button("Sair", use_container_width=True):
            st.logout()
            st.rerun()
    
    return option