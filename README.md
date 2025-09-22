Mini Google File System – Distributed Storage System

A simplified simulation of the Google File System (GFS) implemented in Python.
This project demonstrates how distributed storage, metadata management, chunk replication, and recovery work in modern distributed file systems.

🚀 Features

NameNode → Handles metadata and maps files to chunks.

DataNodes → Store chunks of data across multiple nodes.

Replication Manager → Ensures fault tolerance via replication.

Client Interface → Provides read/write functionality to interact with the system.

Chunking → Splits files into fixed-size blocks for efficient storage.



 Project Structure
Mini-Google-File-System-Distributed-Storage-System/
│── src/
│   ├── namenode.py          
│   ├── datanode.py         
│   ├── replication.py       
│   ├── client.py            
│   ├── __init__.py
│
│── data/
│   └── chunks/              
│
│── app.py                  
│── requirements.txt         
│── README.md
