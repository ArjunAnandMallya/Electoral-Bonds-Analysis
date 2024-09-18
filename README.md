Electoral Bonds Analysis with Flask and SQL

**Name:** Arjun Anand Mallya  
**Roll No:** 23110039  
 

## Overview
The website was created using HTML, ChartJS, CSS, JS, FLASK, Jinja, and Bootstrap.  

**Steps for converting PDF to CSV:**
The PDFs were converted to CSV using the "import fitz.py". Once converted to CSV using fitz, the 2 tables (encashed and purchased) were imported to SQL Workbench under the database name "elecbonds". Then, the following steps were performed:
1. The names of the columns were modified (Spaces and "/n" were removed)
2. Commas were removed from the denominations
3. In denominations, the commas were replaced with ""

**Steps to run:**
1. Import the SQL dump ("DCCDUMP.sql") after making the testing user
2. Run the "main.py"

## About the website
The Flask code is in the "main.py" file. All the HTML files are present in the "templates" folder. All the charts on the website have been plotted using ChartJS.

## Main Page
![Main Page](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/f6f9476a-55f2-4d2b-91bb-b796a9b3a2c1)

## Answers
## Answers to Question 1 :
For questin1, there is a dropdown to select a particular column to search on.  Once a column is chosen, the user can search using the search bar. 
The dropdown looks like this:
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/e57b6e75-b1aa-456a-ae18-cd1a7a20b5c1)
When searching for Bond Number 10418 in the encashed table, we get
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/f6430630-c20c-475c-b284-43258626e024)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/b6693865-1210-41ef-b235-16fa66b8398b)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/4259ec62-b623-498c-a81c-6ff5bfda4d92)

![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/b59148e3-dcf9-4e40-9c79-20e6df581f05)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/0bad0d81-1beb-4748-b1e9-54475538708d)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/9e6c8a5e-51c0-4779-922b-38099bd488a7)


## Answers to Question 2:
For question 2, the user is prompted with a search bar, and can enter any particular political party to view, the table , bar chart between total bond value by year, and number of bonds per year.  There are also 2 save buttons to save each chart.
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/08eeb6c5-c914-4624-88b7-75c1805dd6d6)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/00c04589-a880-40f0-8625-48cfcae44621)
When the save button is clicked, the chart gets saved automatically in png form.  
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/45ad106a-d6f2-42d4-abe4-e30b33bbef37)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/36a24601-cbbc-4b2c-b955-c1bad4a20361)

## Answer to Question 3:
For question 3, the user is prompted with a search bar, and can enter any particular indivdual or company to view, the table , bar chart between total bond value by year, and number of bonds per year.  There are also 2 save buttons to save each chart.
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/8d11ae2f-f092-44b0-9fd0-4cf31812637d)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/fb21e624-1d18-4266-a902-c5531e00bff1)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/f7c75e87-f116-4344-b928-4c4749a4122f)
## Answers to Question 4:
For qn 4 , the user can enter a particular political party.  Once submited, an alluvial diagram of companies that donated to the party is shown.  This chart can also be downloaded with the help of a button.  Below, the alluvial diagram, there is a table showing the same.  
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/41db7077-c298-4ae9-8b30-f45743249566)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/d4a26e1b-5922-4456-8377-1b3e461aaefd)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/5b533288-a09f-4b3b-9873-9b8e6808f58f)

## Answers to Question 5:
For qn 5 , the user can enter a particular company/individual.  Once submited, an alluvial diagram of parties that the company donated to is shown.  This chart can also be downloaded with the help of a button.  Below, the alluvial diagram, there is a table showing the same. 
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/79a289c9-5e22-437d-abf7-14d38d6b6ab0)
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/09201372-93a4-4868-891d-5824b18cdea3)

![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/b1a2ad55-586b-4beb-a343-5d30b114cfc0)

## Answers to Question 6:
For qn 6, a pie chart showing the donations to all the parties will be visible once the button on the main page is clicked.  There is an option to the download the chart as well.  
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/96cb5dbb-c616-4f65-bda8-bb6dfbe1f8d1)

## Answers to Bonus:
For the bonus, a graph between total donations to parties for a particular individual is plotted using a line chart (ChartJS).  
![image](https://github.com/ArjunAnandMallya/DCC_Assignment_4_23110039/assets/166755572/a8a23ef9-cb8d-41ac-8b12-392c4fce32b7)


















