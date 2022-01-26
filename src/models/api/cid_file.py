from alchemize import Attr, JsonMappedModel


class CidFile(JsonMappedModel):
    __mapping__ = {
        "id": Attr("id", str),
        "name": Attr("name", str),
        "status": Attr("status", str),
        "created": Attr("created", str),
        "reads": Attr("reads", object),
        "type": Attr("type", int),
        "is_public": Attr("is_public", bool),
        "folder_id": Attr("folder_id", object),
        "wfs_processed": Attr("wfs_processed", object),
        "wfs_available": Attr("wfs_available", [object]),
    }

    def __init__(self, id: str = None, name: str = None, status: str = None, created: str = None,
                 reads: object = None, type: int = None, is_public: bool = None, folder_id: object = None,
                 wfs_processed: object = None, wfs_available: [object] = None):
        self.id = id
        self.name = name
        self.status = status
        self.created = created
        self.reads = reads
        self.type = type
        self.is_public = is_public
        self.folder_id = folder_id
        self.wfs_processed = wfs_processed
        self.wfs_available = wfs_available
