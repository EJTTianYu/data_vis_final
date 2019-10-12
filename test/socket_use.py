# coding=utf-8

import socket

if __name__ == "__main__":
    # 1.创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定端口(端口号可以修改)
    tcp_server_socket.bind(("", 6666))
    # 3.等待接收客户端的连接请求
    service_client_socket, ip_port = tcp_server_socket.accept()
    print(ip_port)
    # 4.接收客户端发送的http请求报文数据
    recv_data = service_client_socket.recv(4096)
    # 5.显示原始http请求报文数据
    print(recv_data)
    service_client_socket.close()
    tcp_server_socket.close()
