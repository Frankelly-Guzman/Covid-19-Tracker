# Plotly Dash COVID-19 Tracker

This is a Plotly Dash project for tracking COVID-19 data in the United States. It allows users to visualize various COVID-19 statistics over time using interactive graphs. Users can select different metrics from a dropdown menu to view corresponding data.

## Getting Started

To run this project on your local machine, you can follow these steps:

1. Clone the repository:
git clone https://github.com/Frankelly-Guzman/Covid-19-Tracker
cd Covid-19-Tracker

2. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

This will start the Plotly Dash application, and you can access it by opening a web browser and navigating to `http://localhost:8050`.

## Project Structure

The project structure is organized as follows:

- `app.py`: The main application file that contains the Plotly Dash app setup and layout.
- `data/national-history.csv`: The CSV file containing the COVID-19 data for the United States. You can replace this file with more up-to-date data if needed.
- `assets/`: This directory can be used to store any static assets (e.g., images, CSS files) for your app, but it's not used in this project.

## Usage

Once the application is running, you can interact with it in the following way:

1. Open the web browser and navigate to `http://localhost:8050`.

2. You will see the title "COVID-19 Tracker" and a dropdown menu with various COVID-19 metrics to choose from.

3. Select a metric from the dropdown menu, and the graph will update to display the corresponding data over time.

4. The available metrics in the dropdown menu include:
- Positive Cases
- Negative Cases
- Deaths
- Cumulative Hospitalizations
- Total Test Results
- Cumulative ICU
- Cumulative Ventilator

## Customization

You can customize this application in several ways:

- **Data**: You can update the `data/national-history.csv` file with more recent COVID-19 data to keep the information up to date.

- **Styling**: You can customize the app's appearance by modifying the CSS and layout components in the `app.py` file.

- **Additional Features**: You can expand the app by adding more graphs, filters, or interactive elements to provide additional insights into the COVID-19 data.

## Dependencies

- [Dash](https://dash.plotly.com/): A Python web framework for creating interactive, web-based data visualizations.

- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/): A library that provides Bootstrap components for Dash applications.

- [Pandas](https://pandas.pydata.org/): A powerful data manipulation and analysis library in Python.

- [Plotly Express](https://plotly.com/python/plotly-express/): A high-level interface for creating interactive plots with Plotly.

## License

This project is licensed under the MIT License. You are free to use and modify it for your purposes.

## Author

This project was created by Frankelly Guzman.

If you have any questions or need assistance, feel free to contact me at FrankellyRGuzman@gmail.com.

Enjoy tracking COVID-19 data with Plotly Dash!

   
