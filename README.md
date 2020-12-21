## Linux

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Start the application:** `export FLASK_APP=chart && flask run`
3. **Refresh the chart:** `curl -X POST 'http://127.0.0.1:5000/refresh'`
4. **Search the chart:** `curl 'http://127.0.0.1:5000/search?author=morgenstern'`

## Windows

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Start the application:** `set FLASK_APP=chart && flask run`
3. **Refresh the chart:** `Invoke-RestMethod -Method 'Post' -Uri 'http://127.0.0.1:5000/refresh'`
4. **Search the chart:** `Invoke-RestMethod -Method 'Get' -Uri 'http://127.0.0.1:5000/search?author=morgenstern'`
