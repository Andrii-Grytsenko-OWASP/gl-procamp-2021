from alchemize import Attr, JsonMappedModel

from src.models.api.cid_file import CidFile


class DashboardResponse(JsonMappedModel):
    __mapping__ = {
        "files": Attr("files", [CidFile]),
        "breadcrumbs": Attr("breadcrumbs", [object]),
        "generated": Attr("generated", int),
        "is_public": Attr("is_public", bool),
    }

    def __init__(self, files: [CidFile] = None, breadcrumbs: [object] = None,
                 generated: str = None, is_public: bool = None):
        self.files = files
        self.breadcrumbs = breadcrumbs
        self.generated = generated
        self.is_public = is_public
