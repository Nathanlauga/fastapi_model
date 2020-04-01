from typing import List
from pydantic import BaseModel

class Data(BaseModel):
    """

    """
    age: float
    fnlwgt: int
    educational_num: int
    capital_gain: int
    capital_loss: int
    hours_per_week: int

def payload_to_list(dat: Data) -> List:
    return [
        dat.age,
        dat.fnlwgt,
        dat.educational_num,
        dat.capital_gain,
        dat.capital_loss,
        dat.hours_per_week
        ]