from fastapi import FastAPI
import requests

app = FastAPI()


@app.post("/webhook")
async def webhook(data: dict):
    # print(data.get('message'))

    print(data['message']['from']['id'])
    response = requests.post('https://api.telegram.org/bot6890679636:AAG-uD7EUlf5CCj8QUTIp3lZcVLTtKOeSwA/sendMessage',{
        'chat_id': data['message']['from']['id'],
        'text': "pong"
    })
    print(response.content.decode('utf-8'))
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)