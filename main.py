from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic_settings import BaseSettings
from twilio.rest import Client

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    twilio_account_sid: str
    twilio_auth_token: str
    twilio_number: str  # Your Twilio GB number, e.g. +44...
    my_iphone_number: str  # Your iPhone number in E.164, e.g. +385...
    uk_destination_number: str  # UK number to call, e.g. +4420...

    model_config = {"env_file": ".env"}


settings = Settings()
twilio_client = Client(settings.twilio_account_sid, settings.twilio_auth_token)

app = FastAPI(title="Twilio Click-to-Call")


@app.get("/")
async def index():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.post("/call")
async def make_call():
    """Bridge call: Twilio calls your iPhone, then connects to the UK number."""
    twiml = (
        f'<Response><Dial callerId="{settings.twilio_number}">'
        f"<Number>{settings.uk_destination_number}</Number>"
        f"</Dial></Response>"
    )

    try:
        call = twilio_client.calls.create(
            to=settings.my_iphone_number,
            from_=settings.twilio_number,
            twiml=twiml,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "calling", "call_sid": call.sid}


app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
