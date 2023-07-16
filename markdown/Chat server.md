# Chat server

## Task Link
[Rosetta Code - Chat server](https://rosettacode.org/wiki/Chat_server)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.net.*;
import java.util.*;

public class ChatServer implements Runnable
{
  private int port = 0;
  private List<Client> clients = new ArrayList<Client>();
  
  public ChatServer(int port)
  {  this.port = port;  }
  
  public void run()
  {
    try
    {
      ServerSocket ss = new ServerSocket(port);
      while (true)
      {
        Socket s = ss.accept();
        new Thread(new Client(s)).start();
      }
    }
    catch (Exception e)
    {  e.printStackTrace();  }
  }

  private synchronized boolean registerClient(Client client)
  {
    for (Client otherClient : clients)
      if (otherClient.clientName.equalsIgnoreCase(client.clientName))
        return false;
    clients.add(client);
    return true;
  }

  private void deregisterClient(Client client)
  {
    boolean wasRegistered = false;
    synchronized (this)
    {  wasRegistered = clients.remove(client);  }
    if (wasRegistered)
      broadcast(client, "--- " + client.clientName + " left ---");
  }
  
  private synchronized String getOnlineListCSV()
  {
    StringBuilder sb = new StringBuilder();
    sb.append(clients.size()).append(" user(s) online: ");
    for (int i = 0; i < clients.size(); i++)
      sb.append((i > 0) ? ", " : "").append(clients.get(i).clientName);
    return sb.toString();
  }
  
  private void broadcast(Client fromClient, String msg)
  {
    // Copy client list (don't want to hold lock while doing IO)
    List<Client> clients = null;
    synchronized (this)
    {  clients = new ArrayList<Client>(this.clients);  }
    for (Client client : clients)
    {
      if (client.equals(fromClient))
        continue;
      try
      {  client.write(msg + "\r\n");  }
      catch (Exception e)
      {  }
    }
  }

  public class Client implements Runnable
  {
    private Socket socket = null;
    private Writer output = null;
    private String clientName = null;
    
    public Client(Socket socket)
    {
      this.socket = socket;
    }
    
    public void run()
    {
      try
      {
        socket.setSendBufferSize(16384);
        socket.setTcpNoDelay(true);
        BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        output = new OutputStreamWriter(socket.getOutputStream());
        write("Please enter your name: ");
        String line = null;
        while ((line = input.readLine()) != null)
        {
          if (clientName == null)
          {
            line = line.trim();
            if (line.isEmpty())
            {
              write("A name is required. Please enter your name: ");
              continue;
            }
            clientName = line;
            if (!registerClient(this))
            {
              clientName = null;
              write("Name already registered. Please enter your name: ");
              continue;
            }
            write(getOnlineListCSV() + "\r\n");
            broadcast(this, "+++ " + clientName + " arrived +++");
            continue;
          }
          if (line.equalsIgnoreCase("/quit"))
            return;
          broadcast(this, clientName + "> " + line);
        }
      }
      catch (Exception e)
      {  }
      finally
      {
        deregisterClient(this);
        output = null;
        try
        {  socket.close();  }
        catch (Exception e)
        {  }
        socket = null;
      }
    }
    
    public void write(String msg) throws IOException
    {
      output.write(msg);
      output.flush();
    }
    
    public boolean equals(Client client)
    {
      return (client != null) && (client instanceof Client) && (clientName != null) && (client.clientName != null) && clientName.equals(client.clientName);
    }
  }
  
  public static void main(String[] args)
  {
    int port = 4004;
    if (args.length > 0)
      port = Integer.parseInt(args[0]);
    new ChatServer(port).run();
  }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python

import socket
import thread
import time

HOST = ""
PORT = 4004

def accept(conn):
    """
    Call the inner func in a thread so as not to block. Wait for a 
    name to be entered from the given connection. Once a name is 
    entered, set the connection to non-blocking and add the user to 
    the users dict.
    """
    def threaded():
        while True:
            conn.send("Please enter your name: ")
            try:
                name = conn.recv(1024).strip()
            except socket.error:
                continue
            if name in users:
                conn.send("Name entered is already in use.\n")
            elif name:
                conn.setblocking(False)
                users[name] = conn
                broadcast(name, "+++ %s arrived +++" % name)
                break
    thread.start_new_thread(threaded, ())

def broadcast(name, message):
    """
    Send a message to all users from the given name.
    """
    print message
    for to_name, conn in users.items():
        if to_name != name:
            try:
                conn.send(message + "\n")
            except socket.error:
                pass

# Set up the server socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)
server.bind((HOST, PORT))
server.listen(1)
print "Listening on %s" % ("%s:%s" % server.getsockname())

# Main event loop.
users = {}
while True:
    try:
        # Accept new connections.
        while True:
            try:
                conn, addr = server.accept()
            except socket.error:
                break
            accept(conn)
        # Read from connections.
        for name, conn in users.items():
            try:
                message = conn.recv(1024)
            except socket.error:
                continue
            if not message:
                # Empty string is given on disconnect.
                del users[name]
                broadcast(name, "--- %s leaves ---" % name)
            else:
                broadcast(name, "%s> %s" % (name, message.strip()))
        time.sleep(.1)
    except (SystemExit, KeyboardInterrupt):
        break

```

