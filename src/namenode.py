import os
import uuid

class NameNode:
    def __init__(self):
        # file_name → list of chunk_ids
        self.metadata = {}

    def create_file(self, file_name, content, chunk_size=64):
        """Split file into chunks and register metadata"""
        chunks = []
        for i in range(0, len(content), chunk_size):
            chunk_id = str(uuid.uuid4())[:8]
            chunk_data = content[i:i+chunk_size]
            chunks.append((chunk_id, chunk_data))
        self.metadata[file_name] = [c[0] for c in chunks]
        return chunks

    def get_chunks(self, file_name):
        """Return list of chunk IDs for given file"""
        return self.metadata.get(file_name, [])
