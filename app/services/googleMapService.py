import httpx

from app.tools.googlemapTool import get_places_details


class HospitalVerificationService:
    async def verify_hospital(self,hospital_name: str,address: str):
        return await get_places_details(hospital_name, address)
        