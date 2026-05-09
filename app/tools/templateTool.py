TEMPLATES = {
    "otp": {
        "subject": "Your OTP Code",
        "email_html": """
            <h2>Your OTP Code</h2>
            <p>Your OTP is <strong>{otp}</strong>.</p>
            <p>Do not share it.</p>
        """,
        "whatsapp_text": "Your OTP is {otp}. Do not share it.",
        "params": ["otp"]
    },

    "blood_alert": {
        "subject": "Urgent Blood Donation Needed",
        "email_html": """
            <h2>Urgent Blood Requirement</h2>

            <p>
                Blood group <strong>{blood_group}</strong>
                is urgently needed at
                <strong>{hospital}</strong>.
            </p>

            <p>Please help if available.</p>
        """,
        "whatsapp_text":
            "Urgent blood needed for "
            "{blood_group} at {hospital}. Please help.",
        "params": ["blood_group", "hospital"]
    }
}


def render_email(template_name: str, data: dict):
    tpl = TEMPLATES[template_name]

    return {
        "subject": tpl["subject"],
        "html": tpl["email_html"].format(**data)
    }


def render_whatsapp_text(template_name: str, data: dict):
    tpl = TEMPLATES[template_name]

    return tpl["whatsapp_text"].format(**data)


def render_whatsapp_params(template_name: str, data: dict):
    tpl = TEMPLATES[template_name]

    return [
        {
            "type": "text",
            "text": str(data[p])
        }
        for p in tpl["params"]
    ]