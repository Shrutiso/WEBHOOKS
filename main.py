
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(data: dict = Body(...)):

    print("Webhook received!")
    print("Event:", data.get("event"))

    if data.get("event") == "payment.success":
        payment_id = data.get("payment_id")
        amount = data.get("amount")

        return {
            "status": "success",
            "payment_id": payment_id,
            "amount": amount
        }

    return {"status": "received"}
