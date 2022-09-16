# pytmob

#Django-version
  Django==2.2.28

# crear entorno virtual
  python3 -m venv venv
  ## activar el entorno
  source venv/bin/activate

# Instalación de requerimientos
  pip install -r requirements.txt

# Crear super usuario para credenciales en el admin
  python manage.py createsuperuser
  
# Correr los test
  python manage.py test
