class Client:
    def __init__(self, namenode, replication_manager):
        self.namenode = namenode
        self.replication_manager = replication_manager

    def write_file(self, file_name, content):
        print(f"📂 Writing file '{file_name}' to Mini-GFS...")
        chunks = self.namenode.create_file(file_name, content)
        for chunk_id, chunk_data in chunks:
            self.replication_manager.replicate(chunk_id, chunk_data)

    def read_file(self, file_name):
        print(f"📖 Reading file '{file_name}' from Mini-GFS...")
        chunk_ids = self.namenode.get_chunks(file_name)
        if not chunk_ids:
            return None
        content = ""
        for node in self.replication_manager.datanodes:
            for chunk_id in chunk_ids:
                data = node.read_chunk(chunk_id)
                if data:
                    content += data
                    break
        return content
