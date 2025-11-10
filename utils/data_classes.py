from dataclasses import dataclass, asdict

@dataclass
class AOI:
    name: str
    filename: str
    lat: str
    lon: str
    crm_link: str
    crm_local: float = "null"
    bbox_lat: float = 0.25
    bbox_lon: float = 0.25