import os
from iebank_api import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable from Azure or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
