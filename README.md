# 🚀 ISS Overhead Notifier

This project checks if the **International Space Station (ISS)** is currently overhead your location **at night** and sends you an email alert.  
It uses Python, public APIs, and Gmail SMTP, and can be automated with GitHub Actions.

---

## 📂 Project Structure
ISS-Notifier

├── main.py   (Python script to check ISS position and send email)

└── .github/workflows/  ( GitHub Actions workflow file )


---

## ⚙️ How It Works
1. **Fetch ISS position** from [Open Notify API](http://api.open-notify.org/iss-now.json).
2. **Check sunrise/sunset times** from [Sunrise-Sunset API](https://sunrise-sunset.org/api).
3. **Determine if ISS is overhead** (within ±5° latitude/longitude of your location).
4. **Check if it’s night** at your location.
5. **Send email alert** using Gmail SMTP if both conditions are true.
6. **Run automatically** via GitHub Actions on a schedule.

---

## 📑 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ISS-Notifier.git
cd ISS-Notifier
2. Add Dependencies
Create a requirements.txt file:

Code
requests
3. Configure GitHub Secrets
Go to Settings → Secrets → Actions in your repository and add:

MY_EMAIL → your Gmail address

MY_PASSWORD → Gmail App Password (not your real password)

4. Update Coordinates
In main.py, set your latitude and longitude:

python
MY_LAT = 13.435979   # Your latitude
MY_LONG = 79.952507  # Your longitude
🚀 GitHub Actions Workflow
Example .github/workflows/iss.yml:

yaml
name: ISS Notifier

on:
  schedule:
    - cron: "*/5 13-23 * * *"   # Runs every 5 minutes between 6:30 PM and 5:30 AM IST
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run ISS notifier
        env:
          MY_EMAIL: ${{ secrets.MY_EMAIL }}
          MY_PASSWORD: ${{ secrets.MY_PASSWORD }}
        run: python main.py
🎉 Example Output
When ISS is overhead at night:

Code
✅ Email sent successfully
When ISS is not overhead:

Code
ℹ️ No email sent (ISS not visible)
