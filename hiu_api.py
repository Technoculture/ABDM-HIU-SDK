from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RequestData(BaseModel):
    data: str


class ResponseData(BaseModel):
    result: str


@app.post("/v0.5/users/auth/fetch-modes", response_model=ResponseData)
async def fetch_auth_modes(request: RequestData):
    return ResponseData(result="Fetch authentication modes")


@app.post("/v0.5/users/auth/init", response_model=ResponseData)
async def init_auth(request: RequestData):
    return ResponseData(result="User authentication initialized")


@app.post("/v0.5/users/auth/confirm", response_model=ResponseData)
async def confirm_auth(request: RequestData):
    return ResponseData(result="User authentication confirmed")


@app.post("/v0.5/users/auth/notify", response_model=ResponseData)
async def auth_notify(request: RequestData):
    return ResponseData(result="Authentication notification sent")


# Patient Identification
@app.post("/v0.5/patients/on-find", response_model=ResponseData)
async def on_find_patient(request: RequestData):
    return ResponseData(result="Patient found")


# Consent Flow
@app.post("/v0.5/consent-requests/init", response_model=ResponseData)
async def init_consent_request(request: RequestData):
    return ResponseData(result="Consent request initialized")


@app.post("/v0.5/consent-requests/on-init", response_model=ResponseData)
async def on_init_consent_request(request: RequestData):
    return ResponseData(result="Consent request initialization processed")


@app.post("/v0.5/consent-requests/on-status", response_model=ResponseData)
async def on_consent_request_status(request: RequestData):
    return ResponseData(result="Consent status updated")


@app.post("/v0.5/consents/hiu/notify", response_model=ResponseData)
async def consent_hiu_notify(request: RequestData):
    return ResponseData(result="HIU notified of consent update")


@app.post("/v0.5/consents/on-fetch", response_model=ResponseData)
async def fetch_consent_artefact(request: RequestData):
    return ResponseData(result="Consent artefact fetched")


# Data Flow
@app.post("/v0.5/health-information/hiu/on-request", response_model=ResponseData)
async def health_info_hiu_request(request: RequestData):
    return ResponseData(result="Health information requested by HIU")


@app.post("/v0.5/health-information/transfer", response_model=ResponseData)
async def health_info_transfer(request: RequestData):
    return ResponseData(result="Health information transferred")


# Subscription Flow
@app.post("/v0.5/subscription-requests/hiu/on-init", response_model=ResponseData)
async def on_init_subscription(request: RequestData):
    return ResponseData(result="Subscription request initialized")


@app.post("/v0.5/subscription-requests/hiu/notify", response_model=ResponseData)
async def subscription_notify(request: RequestData):
    return ResponseData(result="Subscription notification sent")


@app.post("/v0.5/subscriptions/hiu/notify", response_model=ResponseData)
async def subscription_hiu_notify(request: RequestData):
    return ResponseData(result="HIU subscription notified")


# Patient Notification
@app.post("/v0.5/patients/status/notify", response_model=ResponseData)
async def patient_status_notify(request: RequestData):
    return ResponseData(result="Patient status notified")


@app.post("/v0.5/patients/status/on-notify", response_model=ResponseData)
async def patient_status_on_notify(request: RequestData):
    return ResponseData(result="Patient status notification received")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
