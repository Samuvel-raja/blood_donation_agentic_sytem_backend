
from typing import TypedDict, List, Optional

class BloodRequestState(TypedDict):
    request_id: str
    donors: List[str]
    batch: List[str]
    responses: List[dict]
    request_data: dict
    accepted_donor: Optional[str]
    current_batch: int
    max_batches: int
    status: str  
