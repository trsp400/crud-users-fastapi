from fastapi import FastAPI
from routers import users, items, documents

def create_app():
  app = FastAPI()
  
  app.include_router(users.router, prefix="/users", tags=["users"])
  app.include_router(items.router, prefix="/items", tags=["items"])
  app.include_router(documents.router, prefix="/documents", tags=["documents"])
  
  @app.get("/health", tags=["healthcheck"], summary="Performs a healthcheck")
  def read_root():
    return {"message": "up"}
  
  return app

app = create_app()