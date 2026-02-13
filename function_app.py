import azure.functions as func
import json
from datetime import datetime, timezone

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="ping")
def ping(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({
            "status": "ok",
            "message": "Azure Function is running",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "method": req.method,
            "url": req.url
        }),
        mimetype="application/json",
        status_code=200
    )
