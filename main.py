from fastapi import FastAPI
from disco import  models
from disco.database import engine
from disco.routers import disco, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(disco.router)
app.include_router(user.router)
