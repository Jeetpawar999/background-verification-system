from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(
    title="Background Verification System",
    version="1.0.0",
    description="AI Powered Background Verification System"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(router)

# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "Background Verification System Running"
    }

# Health Check Endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }