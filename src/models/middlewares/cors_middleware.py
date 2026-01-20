from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):
    """
    Configures and applies the CORSMiddleware to the FastAPI application instance.
    """
    
    origins = [
        "http://localhost",
        "http://localhost:3000", 
        "http://127.0.0.1:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,           
        allow_methods=["*"],             
        allow_headers=["*"],            
    )
