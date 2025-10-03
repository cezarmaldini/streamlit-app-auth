import streamlit as st

def st_button_login():
    # CSS personalizado para o botão
    st.markdown("""
    <style>
    .microsoft-login-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff;
        color: #5e5e5e;
        border: 1px solid #8c8c8c;
        border-radius: 2px;
        padding: 8px 12px;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.2s;
        text-decoration: none;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    .microsoft-login-btn:hover {
        background-color: #f5f5f5;
    }

    .microsoft-logo {
        width: 21px;
        height: 21px;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # HTML para o botão
    st.markdown("""
    <div style="display: flex; justify-content: center; margin: 20px;">
        <a href="#" class="microsoft-login-btn">
            <svg class="microsoft-logo" viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg">
                <path fill="#f35325" d="M1 1h10v10H1z"/>
                <path fill="#81bc06" d="M12 1h10v10H12z"/>
                <path fill="#05a6f0" d="M1 12h10v10H1z"/>
                <path fill="#ffba08" d="M12 12h10v10H12z"/>
            </svg>
            Sign in with Microsoft
        </a>
    </div>
    """, unsafe_allow_html=True)