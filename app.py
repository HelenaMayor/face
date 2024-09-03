import streamlit as st
import requests
import pickle

# Cargar las credenciales de Facebook desde facebook.pkl
with open('facebook.pkl', 'rb') as file:
    facebook_config = pickle.load(file)

app_id = facebook_config['app_id']
app_secret = facebook_config['app_secret']
redirect_uri = 'https://your-app-name.streamlitapp.com/callback'

auth_url = (
    f"https://www.facebook.com/v20.0/dialog/oauth?"
    f"client_id={app_id}&redirect_uri={redirect_uri}&scope=publish_video"
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
