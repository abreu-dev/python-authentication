import uvicorn

HOST = 'localhost'
PORT = 5001
RELOAD = True

if __name__ == '__main__':
    uvicorn.run('app:app', host=HOST, port=PORT, reload=RELOAD)
