import multiprocessing


accesslog = "-"
workers = multiprocessing.cpu_count() * 2 + 1
application_path = "conf/asgi.py"
bind = "0.0.0.0:8000"
ca_certs = "/certs/cert.pem"
keyfile = "/certs/private.key"