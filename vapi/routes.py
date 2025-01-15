from vapi import app

@app.route('/')
def running():
    return 'Server is running'