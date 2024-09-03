import streamlit as st
import requests

# Acceder a las variables de entorno desde streamlit.secrets
app_id = st.secrets["APP_ID"]
app_secret = st.secrets["APP_SECRET"]
redirect_uri = st.secrets["REDIRECT_URI"]

auth_url = (
    f"https://www.facebook.com/v20.0/dialog/oauth?"
    f"client_id={app_id}&redirect_uri={redirect_uri}&scope=public_profile"
)

# Botón para iniciar el proceso de autorización
if st.button("Login with Facebook"):
    st.write("Redirigiendo a Facebook para autenticación...")
    st.markdown(f"[Login con Facebook]({auth_url})", unsafe_allow_html=True)

# Manejar la redirección
if 'code' in st.query_params:
    auth_code = st.query_params['code'][0]
    
    # Intercambiar el código por un token de acceso
    token_url = "https://graph.facebook.com/v20.0/oauth/access_token"
    params = {
        'client_id': app_id,
        'redirect_uri': redirect_uri,
        'client_secret': app_secret,
        'code': auth_code
    }

    response = requests.get(token_url, params=params)
    data = response.json()

    if 'access_token' in data:
        access_token = data['access_token']
        st.write(f"User Access Token: {access_token}")
    else:
        st.write("Error al obtener el token de acceso")
