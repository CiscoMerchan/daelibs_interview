from django.urls import path
from django.urls import path
from .views import day_of_week_average_count

# urlpatterns for the app's API endpoints
urlpatterns = [
    #URL path for the 'day_of_week_average_count' API view
    #When a client makes a GET request to '/traffic/dayOfWeekAverageCount/',
    #with 'start_date' and 'end_date' query parameters in the URL, the
    #'day_of_week_average_count' view function will handle the request.

    path('traffic/dayOfWeekAverageCount/', day_of_week_average_count, name='day_of_week_average_count'),
]
"""With this URL pattern, a client can make a GET request to
/traffic/dayOfWeekAverageCount/?start_date=2023-07-07&end_date=2023-07-21
to get the day of week average count data for the specified date range"""






