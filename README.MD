# Raft-distributed-consensus-protocol

### Installation and Running

clone the repository locally 

```git clone https://github.com/Abhishek5101/Raft-distributed-consensus-protocol.git```

- The setup is pre-populated with a cluster of 3 nodes. To boot-up that cluster, open 3 terminal windows for each server and another one for a client. 
 - To start each of the servers - run the start_server script with the respective names and ports of the pre-populated servers. You can register or deregister more servers 
without halting up the cluster.

```
python3 start_server.py abhi 10000
python3 start_server.py dec 10001
python3 start_server.py shane 10002
```

 - Finally in a fourth window, connect the client to the leader of the server. It only takes the port of the
leader server as an argument.

```
python3 start_client.py 10000
```
\
example commands to run on the client termainal to interact with the server cluster

To add an entry as a key-value from the client termninal

`client|@set test_key test_value`

To get a value

`client|@get key`

To delete a value

`client|@delete key`

To show all data

`client|@show`

\
![demo](assets/raft_3_nodes_demo.gif)

- A brief explanation:
In the demo above, we start a cluster of three servers named Abhi, Dec and Shane. After randomized timeouts, the server Shane becomes the leader of the cluster and then we connect our client to that server. Our client then issues the command `client|@get evervault` where `evervault` is the key and the client requests the value for that key from the server. Note that `client|@` is required precursor to every command the client issues and we parse it in code. The request `client|@get evervault` gets a response `b'shane|10002@encryption'` back where `10002` is the port of the leader server and `encryption` is the value result of `evervault` key.
- Similarly, you can give other read or write commands like `set key`, `get key`,`delete key`, `show`. 
- Sometimes the write commands may close the socket connection and you would have to fire up the client again. I am working on fixing that soon.  
