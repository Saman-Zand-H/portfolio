import multiprocessing


bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 1000
worker_connections = 2000
timeout = 120
app = "conf.wsgi:application"