# Web-Scraper
This Python script scrapes the website Spiceworks for reviews of LogicMonitor competitors and exports them to a .csv file.

I initially wrote this script because I was looking for a way to automate the prospecting process of outbound sales.

This project allowed me to use my technical skills in a unique way to facilitate the sales process by consolidating review
data in a single navigable file.

I used the Requests library to perform the initial HTTP request to pull website data into the program.
After the HTTP request, the lxml library was used to convert the data into a navigable tree.
This tree is then searched for HTML tags and attributes related to the desired data.

The .csv file has columns consisting of reviewer name, reviewed technology, and star score out of five.

This .csv file was used to find individuals who were dissatisfied with their monitoring tool in order to facilitate the sales
process.
