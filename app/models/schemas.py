from pydantic import BaseModel


class Candidate(BaseModel):
    full_name: str
    dob: str
    address: str
    government_id: str


class VerificationReport(BaseModel):
    overall_status: str
    details: dict