class ReplicationManager:
    def __init__(self, datanodes, replication_factor=2):
        self.datanodes = datanodes
        self.replication_factor = replication_factor

    def replicate(self, chunk_id, data):
        """Store chunk across multiple DataNodes"""
        assigned_nodes = []
        for node in self.datanodes[:self.replication_factor]:
            node.store_chunk(chunk_id, data)
            assigned_nodes.append(node.node_id)
        return assigned_nodes
