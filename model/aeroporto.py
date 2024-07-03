from dataclasses import dataclass

@dataclass
class Aeroporto:
    ID : int
    IATA_CODE : str
    AIRPORT : str
    CITY : str
    STATE : str
    COUNTRY : str
    LATITUDE : float
    LONGITUDE : float
    TIMEZONE_OFFSET : float

    def __str__(self) -> str:
        return f"{self.ID}"

    def __hash__(self):
        return hash(self.ID)
