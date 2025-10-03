import streamlit as st

from utils import st_login, st_sidebar, st_chat

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
        st_login.st_login()
        
    else:      
        # Sidebar com informações do usuário
        option = st_sidebar.st_sidebar()
        
        if option == 'Chatbot':
            st_chat.st_chat()
            
        elif option == 'Upload':
            st.subheader('Upload | Propostas')
        
if __name__ == "__main__":
    main()