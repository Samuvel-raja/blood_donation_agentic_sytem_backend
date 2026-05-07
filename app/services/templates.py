TEMPLATES = {
    "otp": {
        "text": "Your OTP is {otp}. Do not share it.",
        "params": ["otp"]
    },
    "blood_alert": {
        "text": "Urgent blood needed for {blood_group} at {hospital}. Please help.",
        "params": ["blood_group", "hospital"]
    }
}

def render_email(template_name: str, data: dict) -> str:
    tpl = TEMPLATES[template_name]
    return tpl["text"].format(**data)

def render_whatsapp_params(template_name: str, data: dict):
    tpl = TEMPLATES[template_name]
    return [
        {"type": "text", "text": data[p]}
        for p in tpl["params"]
    ]