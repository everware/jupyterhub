# Configuration file for jupyterhub.

c = get_config()

# Authenticator
c.JupyterHub.authenticator_class = 'jupyterhub.NoAuthenticator'

# spawn with custom docker containers
c.JupyterHub.spawner_class = 'dockerspawner.CustomDockerSpawner'

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from IPython.utils.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
