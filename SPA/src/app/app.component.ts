import { Component } from '@angular/core';
import { io, Socket } from 'socket.io-client';
import { Observable } from 'rxjs';

interface ServerResponse {
  message: string;
}

@Component({
  selector: 'app-root',
  template: `
    <p *ngFor="let item of serverMessage">{{ item }}</p>
    <input type="text" name="mes" id="mes" [(ngModel)]="mes"> <br>
    <button (click)="sendDataToServer()">Gửi dữ liệu lên server</button>
  `,
})
export class AppComponent {
  private socket: Socket;
  serverMessage:string[] = [];
  mes: string = ''

  constructor() {
    // Kết nối tới server
    this.socket = io('http://localhost:8282', {path: '/sockets'});

    this.socket.on('connect', ()=> {
      console.log("Connected")
    });
    // Lắng nghe sự kiện từ server
    this.socket.on('server_response', (data: string) => {
      this.serverMessage.unshift(data)
      console.log(this.serverMessage, data)
    });
}

sendDataToServer() {
// Gửi dữ liệu lên server
this.socket.emit('custom_event', this.mes );
}
}
