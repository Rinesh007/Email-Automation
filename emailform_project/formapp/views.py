from django.shortcuts import render, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def submit_email(request):
    if request.method == 'POST':
        try:
            print("Form submitted.")
            email = request.POST.get('email')
            username = email.split('@')[0]
            print(f"Email received: {email}")

            display_name = username.replace('.', ' ').replace('_', ' ').title()


            scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
            client = gspread.authorize(creds)
            print("Google Sheets authenticated.")

            sheet = client.open("Emails").sheet1
            print("Opened spreadsheet successfully.")

            subject = "Thanks for Signing Up! Let's Stay Connected!"
            content = (
                f"Hey {display_name},\n\n"
                "Thanks for signing up to receive our updates. We’re thrilled to have you with us.\n"
                "Stay tuned for exciting news, tips, and exclusive offers coming your way soon!\n\n"
                "If you have any questions, just hit reply—we love hearing from you.\n\n"
                "Cheers,\n"
            )
            checkbox = ""
            status = ""

            sheet.insert_row([email, subject, content, checkbox, status],2)
            print("Row appended.")

            return redirect('success')

        except Exception as e:
            print(f"Error: {e}")
            return render(request, 'submit.html', {'error': str(e)})

    return render(request, 'submit.html')
def success(request):
    return render(request, 'success.html')
