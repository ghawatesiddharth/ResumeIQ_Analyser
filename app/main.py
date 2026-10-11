from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router


app = FastAPI(
    title="ResumeIQ API",
    description=(
        "AI-powered resume analysis and "
        "job matching API."
    ),
    version="1.0.0",
)


# =========================================
# CORS CONFIGURATION
# =========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Local React development
        "http://localhost:5173",
        "http://127.0.0.1:5173",

        # Dockerized React frontend
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================
# API ROUTES
# =========================================

app.include_router(router)


# =========================================
# ROOT ENDPOINT
# =========================================

@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeIQ API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }