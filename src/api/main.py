from uvicorn import run

HOST = 'localhost'
PORT = 5001
RELOAD = True

if __name__ == '__main__':
    run('app:app', host=HOST, port=PORT, reload=RELOAD)
