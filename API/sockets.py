import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)


@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid})


@sio_server.event
async def chat(sid, message):
    await sio_server.emit('chat', {'sid': sid, 'message': message})


# Khởi tạo sự kiện khi có sự kiện tùy chỉnh từ client
@sio_server.event
async def custom_event(sid, data):
    print(f"Nhận được sự kiện từ client {sid}: {data}")
    # Gửi dữ liệu về lại client
    await sio_server.emit("server_response", data)


@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')
