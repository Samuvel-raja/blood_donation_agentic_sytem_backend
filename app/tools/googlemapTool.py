
import httpx
from config import settings

async def get_places_details(hospital_name: str, address: str):
    async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.google_maps_places_url}",
                headers={
                    "Content-Type":"application/json",
                    "X-Goog-Api-Key":settings.google_maps_api_key,
                    "X-Goog-FieldMask":
                        (
                            "places.displayName,"
                            "places.formattedAddress,"
                            "places.id,"
                            "places.types"
                        )
                },
                json={
                    "textQuery":
                        (
                            f"{hospital_name} "
                            f"{address}"
                        )
                }
            )
            data = response.json()
            places = data.get("places", [])
            if not places:
                return {
                    "verified": False
                }

            hospital = places[0]
            is_hospital = (
                "hospital"
                in hospital.get("types", [])
            )
            return {
                "verified":is_hospital,
                "place_id":hospital.get("id"),
                "name":hospital.get("displayName", {}).get("text"),
                "address":hospital.get("formattedAddress")
            }