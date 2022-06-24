import streamlit as st
import urllib.parse

# a replica of 
# https://jupyterhub.github.io/nbgitpuller/link


JupyterHubURL = st.text_input('JupyterHub URL', 'https://jupyterhub-redhat-ods-applications.apps.rhods-internal.61tk.p1.openshiftapps.com')
GitRepoURL = st.text_input('Git Repo URL', 'https://github.com/rh-aiservices-bu/streamlit-showcase.git')
GitRef = st.text_input('Git Reference', 'main')
FileToOpen = st.text_input('File to Open', 'Streamlit-Showcase.ipynb')


GeneratedURL=(JupyterHubURL
    +'/hub/user-redirect/git-pull?repo='
    +urllib.parse.quote(GitRepoURL))



# https://jupyterhub-redhat-ods-applications.apps.rhods-internal.61tk.p1.openshiftapps.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Frh-aiservices-bu%2Fstreamlit-showcase&urlpath=lab%2Ftree%2Fstreamlit-showcase%2F

st.write('generated URL:')
st.write('https://jupyterhub-redhat-ods-applications.apps.rhods-internal.61tk.p1.openshiftapps.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Frh-aiservices-bu%2Fstreamlit-showcase.git&urlpath=lab%2Ftree%2Fstreamlit-showcase.git%2FStreamlit-Showcase.ipynb&branch=main')
# st.write(GeneratedURL)
