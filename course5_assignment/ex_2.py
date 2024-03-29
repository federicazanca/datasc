import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Netflix stock data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

#print("print head")
#print(netflix_data.head())

#We can also use the pandas read_html function from the pandas library and use the URL for extracting data.
read_html_pandas_data = pd.read_html(url)
#Or you can convert the BeautifulSoup object to a string.
read_html_pandas_data = pd.read_html(str(soup))

netflix_dataframe = read_html_pandas_data[0]

#print("print head")
#print(netflix_dataframe.head())

"""Exercise: Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html. 
Save the text of the response as a variable named html_data."""

url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data = requests.get(url).text

#Parse the html data using beautiful_soup.

bsoup = BeautifulSoup(html_data, 'html5lib')

#Question 1: What is the content of the title attribute?
print(bsoup.title)

#
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in bsoup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

#print the first 5 rows
print("print first 5 rows")
print(amazon_data.head(5))

#Question 2: What are the names of the columns in the data frame?
print("Question 2: What are the names of the columns in the data frame?")
print(amazon_data.head(0))

#Question 3: What is the Open of the last row of the amazon_data data frame?
print("Question 3: What is the Open of the last row of the amazon_data data frame?")
print(amazon_data.tail(1))


read_html_pandas_data = pd.read_html(str(bsoup))

amazon_dataframe = read_html_pandas_data[0]
print(amazon_dataframe.head())

