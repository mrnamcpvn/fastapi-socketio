import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sockets import sio_app

app = FastAPI()
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    return {'message': 'Hello👋 Developers💻'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8282)
