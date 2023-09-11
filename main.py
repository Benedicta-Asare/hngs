from fastapi import FastAPI
from datetime import datetime 

app = FastAPI()



@app.get("/api/")
def get_info(slack_name: str, track: str):
    current_day = datetime.now().strftime("%A")
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track
        }