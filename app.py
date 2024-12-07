from flask_cors import CORS
from iebank_api import app

# Enable CORS for the frontend domain
CORS(app, origins=["https://jwendt-fe-dev.azurewebsites.net"], supports_credentials=True)

if __name__ == '__main__':
    app.run(debug=True)
