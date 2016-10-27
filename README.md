# socket-programming
Simple chat room implementation using sockets in Python

Run the server:
`python server.py -sp 9090` runs the server on port 9090

Output:
Server Initialized... 

(Server is left running)

Run the client(s):
`python client.py -sip server-ip -sp 9090`

Send a Message:
` > Hello World! `

Receive a Message:
` <From w.x.y.z:aa>: Hello World! `

Every client connected to the server sees this, where w.x.y.z:aa is the sender's ip address and port.
