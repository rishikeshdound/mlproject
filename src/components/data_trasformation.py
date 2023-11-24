# after ingestion code for  data trasformation,data validation, encoding
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    city: str