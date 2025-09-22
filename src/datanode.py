import os

class DataNode:
    def __init__(self, node_id, storage_dir="data/chunks"):
        self.node_id = node_id
        self.storage_dir = os.path.join(storage_dir, node_id)
        os.makedirs(self.storage_dir, exist_ok=True)

    def store_chunk(self, chunk_id, data):
        path = os.path.join(self.storage_dir, chunk_id + ".txt")
        with open(path, "w") as f:
            f.write(data)

    def read_chunk(self, chunk_id):
        path = os.path.join(self.storage_dir, chunk_id + ".txt")
        if os.path.exists(path):
            with open(path, "r") as f:
                return f.read()
        return None
