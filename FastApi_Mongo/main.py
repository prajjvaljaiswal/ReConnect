from fastapi import FastAPI
from routes.testRouter import testRouter

app = FastAPI()

app.include_router(testRouter)

