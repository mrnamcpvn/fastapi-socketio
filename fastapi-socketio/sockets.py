from main import socket_manager as sm


@sm.on('join')
async def handle_join(sid, *args, **kwargs):
    await sm.emit('lobby', 'User joined')
