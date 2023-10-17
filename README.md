# Weather-Application
The Weather Application is a simple web-based tool that allows users to retrieve weather information for a specified location. It utilizes the OpenWeatherMap API to fetch weather data and displays it to the user. This README provides an overview of the application's features, how to set it up, and usage instructions.

# Features
- Users can input a city, state, and country to get weather information.
- The application displays the weather's main condition, description, temperature, and an icon representing the weather.
- It is built using Flask, a Python web framework, and leverages Bootstrap for styling.
  
# Setup
Follow these steps to set up and run the Weather Application locally:

1. Clone the Repository:
git clone [repository_url]

2. Install Dependencies:
pip install -r requirements.txt

4. Obtain an API Key:
- Visit the OpenWeatherMap website.
- Sign up for an account and obtain an API key.
- Create a .env file in the project directory and add your API key like this:

5. Run the Application:
The application should now be accessible at http://localhost:8080 in your web browser.

# Usage
1. Access the Application:
Open your web browser and go to http://localhost:8080.

2. Input Location Details:
- Enter the name of the city in the "City" field.
- Optionally, enter the state and country details in the respective fields. The state and country fields have default values (VA and US), which can be modified.
Retrieve Weather Information:
- Click the "Find" button to fetch weather information for the specified location.
View Weather Data:

The weather data will be displayed, including the main condition (e.g., Clouds), description (e.g., broken clouds), temperature (in degrees Celsius), and an icon representing the weather.
Try Different Locations:

You can enter different locations and click "Find" to retrieve weather data for various places.

# Project Structure
app.py: The main Flask application script.
templates/index.html: The HTML template for the web page.
requirements.txt: Lists the Python packages required for the application.
weather.py: Contains functions for retrieving weather data from the OpenWeatherMap API.

# Dependencies
Python 3.x
Flask
Bootstrap
Requests
Python-dotenv

# Acknowledgments
This project uses the OpenWeatherMap API to provide weather information.
Styling is achieved using Bootstrap.
Feel free to customize and enhance this Weather Application as needed for your specific use case or integrate it into other projects.
