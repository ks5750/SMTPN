from socket import *


def smtp_client(port=587, mailserver='smtp.gmail.com'):
    msg = "\r\n Hello there NYU network test"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
         # print('220 reply not received from server.')

    # Send HELO command and # print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        # print('250 reply not received from server.')

    # Send MAIL FROM command and # print server response.
    # Fill in start
    mailFromComm = "MAIL FROM:<nyusaswat@gmail.com>\r\n"
    clientSocket.send(mailFromComm.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    if recv2[:3] != '250':
        # print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and # print server response.
    # Fill in start
    rcptToComm = "RCPT TO:<nyusaswat@gmail.com>\r\n"
    clientSocket.send(rcptToComm.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    if recv3[:3] != '250':
        # print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and # print server response.
    # Fill in start
    dataComm = "DATA\r\n"
    clientSocket.send(dataComm.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    if recv4[:3] != '250':
        # print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recvMsg = clientSocket.recv(1024).decode()
    # print(recvMsg)
    if recvMsg[:3] != '250':
        # print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    initQuit = "QUIT\r\n"
    clientSocket.send(initQuit.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    if recv5[:3] != '250':
        # print('250 reply not received from server.')
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(587, 'smtp.gmail.com')
