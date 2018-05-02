bind = "127.0.0.1:8000"
workers = 4
preload_app = True
worker_class = "egg:meinheld#gunicorn_worker"
threads = 8
