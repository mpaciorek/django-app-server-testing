# KONFIGURACJA WIELOWĄTKOWA Z 4 wątkami na proces
#

bind = "127.0.0.1:8100"
workers = 4
preload_app = True
worker_class = "gevent"
threads = 4
