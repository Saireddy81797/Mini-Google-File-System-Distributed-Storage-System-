from src.namenode import NameNode
from src.datanode import DataNode
from src.replication import ReplicationManager
from src.client import Client

def main():
    # Setup system
    namenode = NameNode()
    datanodes = [DataNode("Node1"), DataNode("Node2"), DataNode("Node3")]
    replication_manager = ReplicationManager(datanodes)
    client = Client(namenode, replication_manager)

    # Demo
    text = "This is a simulated Google File System. Fault-tolerant and replicated!"
    client.write_file("demo.txt", text)

    result = client.read_file("demo.txt")
    print("✅ Recovered content:", result)

if __name__ == "__main__":
    main()
