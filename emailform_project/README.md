# Django + Google Sheets + n8n Email Automation 🚀

A simple automated email project using:

- Django for frontend
- Google Sheets for storing email submissions
- n8n for sending automated emails

## 💡 How It Works

1. A user enters their email on a Django form.
2. The info is inserted into a Google Sheet.
3. n8n watches the sheet and sends an email if a checkbox is ticked.

## 📁 Project Structure

- `formapp/views.py`: Logic for inserting data to Google Sheets
- `credentials.json`: Google Service Account credentials (keep private!)
- `n8n_workflow.json`: Exported automation workflow
- `test_gsheets.py`: Optional script to test Google Sheets write manually

## 🔐 Setup Guide

1. Create your own `credentials.json` from Google Cloud Console.
2. Create a Google Sheet with columns: `Recipient Email`, `Subject`, `Content`, `Checkbox`, `Status`
3. Import the n8n workflow (optional)
