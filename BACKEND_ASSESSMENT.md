# Backend Assessment - Traffic API

This project is a backend assessment for a Traffic API built using Django and Django REST framework. The API provides functionality to retrieve average counts for each day of the week based on a date range provided in the API request.

## Requirements

To run this project, you need Python 3.10 or higher installed on your system. You can download the latest version from the official Python website: [Download Python](https://www.python.org/downloads/)

## Setup

1. Clone this repository to your local machine.

2. Create a virtual environment and install the required dependencies:

   ```
   python -m venv venv
   source venv/bin/activate  # For Windows, use 'venv\Scripts\activate'
   pip install -r requirements.txt

Run the Django development server:

```python manage.py runserver
The server will be running at http://127.0.0.1:8000/
```

## API Endpoints
- Get Day of Week Average Count
- URL: /traffic/dayOfWeekAverageCount/
- Method: GET
- Query Parameters:
  * start_date: The start date of the date range (format: YYYY-MM-DD).
  * end_date: The end date of the date range (format: YYYY-MM-DD).
- Response: Returns the average count for each day of the week in JSON format.


### traffic_api\views.py
- The `day_of_week_average_count` view function handles the API request for day of week average count.
- It checks if both 'start_date' and 'end_date' are provided in the request, and if any of them is missing, it raises a ValueError and TypeError with a custom error message.
- The view queries the database using Django's SensorEvent model to get the average count for each day of the week within the specified date range.
- The average counts are calculated using Django's Avg function and filters (using the Q class) to filter data for each day of the week.
- The results are returned in the desired JSON format as the API response.

### traffic_api\urls.py
- The URL pattern for the day_of_week_average_count API view is defined in this file.
- Clients can make a GET request to `/traffic/dayOfWeekAverageCount/` with `start_date` and `end_date` query parameters to get the day of week average count data for the specified date range.

### urls.py (daelibs_interview)
- The main URL configuration for the daelibs_interview project is defined in this file.
- It includes the app's URLs from the traffic_api app using the include function. This allows the traffic API endpoints to be accessed from the root level of the project.

## Learnings and Challenges

### What I've Done
- I implemented the API functionality for day of week average count based on a date range using Django and Django REST framework.
- I learned how to work with Django's models and perform complex queries using the Q class for filtering and the Avg class for calculating averages.
- I separated the Django syntax from the REST framework syntax to achieve the desired functionality.
- I added exception handling in the view function to check if both 'start_date' and 'end_date' are provided in the request and raise appropriate errors if they are missing.

### Challenges
- Understanding how to use the Q class to build complex queries using the | (OR) and & (AND) operators was initially challenging.
- Getting familiar with the Avg class and how to use it in conjunction with filters to calculate averages required some research.

### Next Steps
or further improvement and enhancement, the following steps can be taken:

- Implement a test suite for testing the functionality and behavior of the API.
- Implement authentication and authorization for secure API access.
- Add pagination for handling large amounts of data in the API responses.
- Document the API endpoints and their usage for other developers.
- Implement API versioning to manage future changes and updates to the API.

## Conclusion
In this backend assessment, I gained a deeper understanding of Django, Django REST framework, and working with complex data queries. I learned the importance of breaking down problems into smaller pieces and asking the right questions to efficiently solve challenges. Working in a team environment or seeking help in community forums can be beneficial when facing roadblocks. I will continue to improve my skills and knowledge to become a more proficient developer.
