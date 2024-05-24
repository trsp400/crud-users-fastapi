from fastapi import FastAPI
from routers import users, items

def create_app():
  app = FastAPI()
  
  app.include_router(users.router, prefix="/users", tags=["users"])
  app.include_router(items.router, prefix="/items", tags=["items"])
  
  @app.get("/health", tags=["healthcheck"], summary="Performs a healthcheck")
  def read_root():
    return {"message": "up"}
  
  return app

app = create_app()