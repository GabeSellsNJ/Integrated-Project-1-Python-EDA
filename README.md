# Practicum-Project-4

TITLE: CAR SALES ANALYSIS

Introduction
Within this project is a csv file containing over 50,0000 entries. Each entry contains various information regarding a car sale.
In my analysis, I focused on price, odometer mileage, manufacturer, and condition.

In the first part of my code, I pre-processed the data to fill in any missing data. Most importantly for my analysis, I remove any entries containing sales lower than a $1,000 and greater than $80,000. 

Data Anaylsis 1: Mileage Vs Price
I simply chart (using a scatter plot) price vs mileage (odometer). I removed any outliers with mileage over 450,000 miles.
My hypothesis is intuitive; the more mileage, the less the car is worth.
Observing the chart, my hypothesis is correct. There is a clear negative correlation.

Data Anaylsis 2: Price Distribution
I want to see to the price distribution between manufacturers and condition. I created a dropbox to choose each unique manufacturer. Users can also check the checkbox to see the price distribution between ALL manufacturers. Likewise, users can toggle on/off each condition to see the price distribution between conditions.

How to Run
You can run my pyhton script by opening an IDE (such as VS Code) and finding the location of my app.py file and simply running the file.
Or you may use the Terminal on your computer. Enter "cd" into Terminal along with the absolute path where this poject is located on your computer. Enter "streamlit run app.py" to run the python script.
Or you can can simply view this project in a web browser with the link below:

https://praticum-project-4.onrender.com

