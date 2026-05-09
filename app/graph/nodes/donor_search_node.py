from app.services.userService import get_users_by_fields

async def donor_search_node(state):
    request = state.request_data
    blood_group = request.get("blood_group", "")
    donors = get_users_by_fields(blood_group=blood_group)
    return {
        "donors": donors
    }