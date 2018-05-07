# KONFIGURACJA WIELOWĄTKOWA Z 8 wątkami na proces
#
bind = "127.0.0.1:8100"
workers = 4
preload_app = True
worker_class = "egg:meinheld#gunicorn_worker"
