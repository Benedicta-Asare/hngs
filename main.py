from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/")
def get_info(slack_name: str, track: str):
    if not slack_name or not track:
        return {
            "status_code": 400,
            "error": "Please provide slack_name and track"
            }
            
    current_day = datetime.now().strftime("%A")
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Benedicta-Asare/hngx/blob/main/main.py",
        "github_repo_url": "https://github.com/Benedicta-Asare/hngx/",
        "status_code": 200
        }