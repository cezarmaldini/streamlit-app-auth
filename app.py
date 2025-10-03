import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Configurar a página
st.set_page_config(
    page_title="Tático Soluções",
    page_icon="🎯",
    layout='wide'
)

def main():
    st.title("🎯 Tático Soluções")

    # Verificar se o usuário está logado
    if not st.user.is_logged_in:
        # Tela de login
        st.info("🔐 Faça login para acessar a aplicação")
            
        st.subheader("Bem-vindo!")
        st.write("""
        Esta é uma aplicação protegida com Microsoft Entra ID.
            
        **Recursos disponíveis após login:**
        - Chatbot IA
        - Upload de Propostas
        - Perfil do usuário
        """)

        st.subheader("Login")
        st.write("Clique no botão abaixo para fazer login:")
            
        # Botão de login centralizado
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("🚀 Entrar com Microsoft", 
                            type="primary", 
                            use_container_width=True,
                            key="login_button"):
                try:
                    st.login(provider="microsoft")
                except Exception as e:
                    st.error(f"Erro no login: {e}")
                    st.info("Verifique se as credenciais estão corretas no secrets.toml")
        
    else:      
        # Sidebar com informações do usuário
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
        
        if option == 'Chatbot':
            st.subheader('Chat | Propostas')
            
        elif option == 'Upload':
            st.subheader('Upload | Propostas')
        
if __name__ == "__main__":
    main()