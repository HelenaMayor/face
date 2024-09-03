import streamlit as st
import requests

# Acceder a las variables de entorno desde streamlit.secrets
app_id = st.secrets["APP_ID"]
app_secret = st.secrets["APP_SECRET"]
redirect_uri = "https://d5dzt7ecdm8lntbmvtn3oh.streamlit.app/"  
auth_url = (
    f"https://www.facebook.com/v20.0/dialog/oauth?"
    f"client_id={app_id}&redirect_uri={redirect_uri}&scope=public_profile"
)
https://www.facebook.com/v20.0/dialog/oauth?
  client_id={app-id}
  &redirect_uri={"https://www.domain.com/login"}
  &state={"{st=state123abc,ds=123456789}"}
if st.button("Login with Facebook"):
    st.write("Redirigiendo a Facebook para autenticación...")
    st.markdown(f"[Login con Facebook]({auth_url})", unsafe_allow_html=True)

# Manejar la redirección (Streamlit se encarga de los query params en la URL base)
if 'code' in st.query_params:
    auth_code = st.query_params['code'][0]
    
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
        st.write("Login exitoso, token de acceso obtenido.")
    else:
        st.write("Error al obtener el token de acceso")
