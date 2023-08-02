# Import the required modules and functions from Django and Django REST framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from main.models import SensorEvent # Import the SensorEvent model from main/models.py
from django.db.models import Avg, Q
# Create your views here.
# A function that handles the API request for day of week average count
@api_view(['GET']) # handle HTTP GET requests.
def day_of_week_average_count(request):
    """ The exception  check if both 'start_date' and 'end_date' are provided in the request.
    If any of them is missing, raise a ValueError with a custom error message to inform the
    user that both parameters are require"""
    try:
        # Get the start_date and end_date from the query parameters
        """Django rest framework document: 'For clarity inside your code, we recommend
         using request.query_params instead of the Django's standard request.GET. Doing
         so will help keep your codebase more correct and obvious - any HTTP method type
         may include query parameters, not just GET requests.'"""
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        # Ensure both 'start_date' and 'end_date' are provided in the request
        if not start_date or not end_date:
            # If not provided, return an error response
            return Response({'error': 'Both start_date and end_date are required.'}, status=400)

        # Query the database to get average count for each day of the week from the Main app's SensorEvent model
        average_counts = SensorEvent.objects.filter(event_datetime__range=[start_date, end_date]).values('sensor__id',
                                                                                               'sensor__name').annotate(
            # Calculate average counts for each day of the week using Django's Avg function and filters
            mon_avg_count=(Avg('id', filter=Q(event_datetime__week_day=2)), 2),
            tue_avg_count=(Avg('id', filter=Q(event_datetime__week_day=3)), 2),
            wed_avg_count=(Avg('id', filter=Q(event_datetime__week_day=4)), 2),
            thu_avg_count=(Avg('id', filter=Q(event_datetime__week_day=5)), 2),
            fri_avg_count=(Avg('id', filter=Q(event_datetime__week_day=6)), 2),
            sat_avg_count=(Avg('id', filter=Q(event_datetime__week_day=7)), 2),
            sun_avg_count=(Avg('id', filter=Q(event_datetime__week_day=1)), 2),
        )

        # Return the results in the desired JSON format as the API response
        return Response({'results': average_counts})

    except (ValueError, TypeError):
        """Handle errors with invalid date formats in the request parameters,
        and let know the user which parameter is require"""
        raise ParseError('Invalid date format. Use YYYY-MM-DD.')
