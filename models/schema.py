from pydantic import BaseModel
from typing import List, Optional

class LabTest(BaseModel):
    lab_test_name: str
    lab_test_value: float
    bio_reference_range: str
    lab_test_out_of_range: bool

class LabTestResponse(BaseModel):
    is_success: bool
    data: List[LabTest]
    error: Optional[str] = None
