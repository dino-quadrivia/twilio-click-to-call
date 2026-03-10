# Twilio Click-to-Call

A simple web app that lets you call a UK phone number from your iPhone using Twilio. You tap a button on a webpage, Twilio calls your iPhone first, and when you answer, it connects you to the UK destination number.

## How it works

1. You open the web app in your browser and tap "Call Now"
2. Twilio calls your iPhone
3. You answer the call on your iPhone
4. Twilio bridges you to the UK destination number
5. You're connected — using your normal Phone app, no SIP or softphone needed

The backend uses the Twilio Calls API with inline TwiML to create a two-leg bridge call.

## Prerequisites

- A Twilio account ([console.twilio.com](https://console.twilio.com))
- A Twilio voice-capable UK phone number (requires a UK regulatory bundle)
- UK enabled in Geographic Permissions (Twilio Console > Voice > Settings > Geo Permissions)
- On a trial account: both your iPhone number and the UK destination number must be verified in the Console

## Setup

```bash
cd ~/workspace/call
source .venv/bin/activate
cp .env.example .env
```

Edit `.env` with your values:

```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_NUMBER=+44xxxxxxxxxx
MY_IPHONE_NUMBER=+385xxxxxxxxx
UK_DESTINATION_NUMBER=+44xxxxxxxxxx
```

- **TWILIO_ACCOUNT_SID** and **TWILIO_AUTH_TOKEN** — found on the main dashboard at [console.twilio.com](https://console.twilio.com)
- **TWILIO_NUMBER** — your Twilio UK phone number in E.164 format
- **MY_IPHONE_NUMBER** — your iPhone number in E.164 format (e.g. +385...)
- **UK_DESTINATION_NUMBER** — the UK number you want to call in E.164 format (e.g. +442079460123)

## Run

```bash
source .venv/bin/activate
uvicorn main:app --reload
```

Open `http://localhost:8000` in your browser and tap "Call Now".
