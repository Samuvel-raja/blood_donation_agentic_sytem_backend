from fastapi import Request

async def email_reply(request: Request):

    form = await request.form()

    sender = form.get("sender")

    body = form.get("body-plain")

    print(sender)

    print(body)

    return {
        "status": "received"
    }