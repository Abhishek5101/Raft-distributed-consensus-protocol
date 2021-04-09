# evervault-challenge

### Installation and Running

clone the repository locally 

```git clone https://github.com/Abhishek5101/evervault-challenge.git```

- The setup is pre-populated with a cluster of 3 nodes. To boot-up that cluster, open 3 terminal windows for each cluster and another one for a client. 
 - To start each of the servers - run the start_server script with the respective names and ports of the pre-populated servers. You can register or deregister more servers 
without halting up the cluster.

```
python3 start_server.py abhi 10000
python3 start_server.py dec 100001
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