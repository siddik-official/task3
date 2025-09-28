# LCM Calculator API

A simple web API that calculates the Lowest Common Multiple (LCM) of two natural numbers.

## API Endpoint

`GET /official_siddik_gmail_com?x={number}&y={number}`

### Parameters:
- `x`: Natural number (positive integer > 0)
- `y`: Natural number (positive integer > 0)

### Response:
- Returns the LCM as a plain string containing only digits
- Returns "NaN" if either parameter is invalid (missing, non-integer, zero, negative, or non-numeric)

### Examples:
- `/official_siddik_gmail_com?x=6&y=8` → `24`
- `/official_siddik_gmail_com?x=12&y=18` → `36`
- `/official_siddik_gmail_com?x=-5&y=3` → `NaN`
- `/official_siddik_gmail_com?x=abc&y=5` → `NaN`

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:5000`

## Deployment

This app is configured for deployment on platforms like Render, Railway, or Heroku using gunicorn.