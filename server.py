# UDP Chat server 
import socket, sys
 
#Function to broadcast chat messages to all connected clients
def broadcast_data (message):
    #Do not send the message to the client who has send us the message    
    for addr in CONNECTION_LIST:
        if addr[1] != sender_addr[1]:
            try :
                server_socket.sendto(message,(addr[0],addr[1]))
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example                
                CONNECTION_LIST.remove(addr)
 
 # Main Method
if __name__ == "__main__":

    # Check if the filename and input args have been named properly
    if(len(sys.argv) < 3) :
        print 'Usage : python server.py -sp port'
        sys.exit()
    # Check if port number is an integer
    try:
        PORT = int(sys.argv[2])
    except:
        print 'Please enter proper port'
        sys.exit()
     
   
    CONNECTION_LIST = []        # List to keep track of all clients who have "Greeted" the server
    RECV_BUFFER = 4096          # Advisable to keep it as an exponent of 2    
     
    # Create Server UDP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the server socket to the server ip and the PORT    
    server_socket.bind(("127.0.0.1", PORT))    
 
    print "Server Initialized on port " + str(PORT)
 
    while 1:
        data, addr = server_socket.recvfrom(RECV_BUFFER)
        # New Connection or GREETING        
        if data == "GREETING":
            CONNECTION_LIST.append(addr)                       
        # Data recieved from client, broadcast it
        else:
            # Store the sender address so that we don't send the message back to him
            sender_addr = addr;
            broadcast_data("\r" + '<From ' + str(addr) + '> ' + data)

    # Close the server socket     
    server_socket.close()