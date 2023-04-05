from fastapi import FastAPI
from fastapi_socketio import SocketManager
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
socket_manager = SocketManager(app=app, async_mode='asgi', cors_allowed_origins=[])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@socket_manager.on('connect')
def connect(sid):
    print(f'Client {sid} connected')

@socket_manager.on('disconnect')
def disconnect(sid):
    print(f'Client {sid} disconnected')

@socket_manager.on('message')
def message(sid, data):
    print(f'Received message from {sid}: {data}')
    try:
        socket_manager.emit('response', f'Response from server: {data}', room=sid)
    except ConnectionRefusedError:
        print(f'Client {sid} is not connected')

# # Khởi tạo sự kiện khi có kết nối từ client
# @socket_manager.on("connect")
# async def connect(sid, data):
#     print(f"Client {sid} đã kết nối!")
#
#
# # Khởi tạo sự kiện khi có sự kiện tùy chỉnh từ client
# @socket_manager.on("custom_event")
# async def custom_event(sid, data):
#     print(f"Nhận được sự kiện từ client {sid}: {data}")
#     # Gửi dữ liệu về lại client
#     await socket_manager.emit_to(sid, "server_response", {"message": "Hello from server"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9981)
