from . import (
    response
)

# Function to return Status. 
def sendStatus (code, header, msg):
    return response(status_code=code,
                    headers={'Content-Type': header},
                    body=msg)