
from typing import List, Optional,Annotated
from pydantic import BaseModel
from operator import add

class BloodRequestState(BaseModel):
    request_id: str
    donors: Annotated[List[dict], add]
    hospital_verification_data: dict
    ranked_donors: Annotated[List[str], add]
    batch: Annotated[List[str], add]
    responses: Annotated[List[dict], add]
    request_data: dict
    accepted_donor: Optional[str]
    current_batch: int
    max_batches: int
    status: str  
