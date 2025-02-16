from fastapi import FastAPI
from routes.testRouter import testRouter
from routes.login import loginRouter

app = FastAPI()

app.include_router(testRouter)
app.include_router(loginRouter)
