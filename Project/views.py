from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import response
def index(request):
    return render(request,'Pro/index.html')

@csrf_exempt
def process_command(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('user_input', '').lower()  # Convert to lowercase for case-insensitivity

        # Simple command processor
        response_text=response.command(user_input)
        # if 'hello' in user_input:
        #     response_text = 'Hello! How can I help you today?'
        # elif 'time' in user_input:
        #     # You can use the 'datetime' module to get the current time
        #     from datetime import datetime
        #     response_text = f'The current time is {datetime.now().strftime("%H:%M:%S")}.'
        # elif 'time' in user_input:
        #     # You can use the 'datetime' module to get the current time
        #     from datetime import datetime
        #     response_text = f'The current time is {datetime.now().strftime("%H:%M:%S")}.'
        # elif 'time' in user_input:
        #     # You can use the 'datetime' module to get the current time
        #     from datetime import datetime
        #     response_text = f'The current time is {datetime.now().strftime("%H:%M:%S")}.'
        # elif 'date' in user_input:
        #     # You can use the 'datetime' module to get the current time
        #     from datetime import datetime
        #     response_text = f'The current date is {datetime.now().date()}.'
        # elif 'time' in user_input:
        #     # You can use the 'datetime' module to get the current time
        #     from datetime import datetime
        #     response_text = f'The current time is {datetime.now().strftime("%H:%M:%S")}.'
        # elif 'time' in user_input:
        #     # You can use the 'datetime' module to get the current time
        #     from datetime import datetime
        #     response_text = f'The current time is {datetime.now().strftime("%H:%M:%S")}.'
        # else:
        #     response_text = f"I'm sorry, I didn't understand that command. Can you please clarify?"

        response_data = {'response': response_text}
        return JsonResponse(response_data)

# Create your views here.dex

