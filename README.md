### About ###  
Based on your search input, I search reputable websites and find the cheapest results from each site.  
The results are exported to an excel sheet for easy comparison from low to high prices.  

Why?  
There are numerous websites for custom PC parts and it becomes too difficult to search for the best price.  
It becomes much easier to compare the prices of different online stores when it is automatically tabulated for you.  

How?  
Using Python's BeautifulSoup library I webscrape reputable websites and export it to excel using the Pandas library.  


### Websites searched ###  
IndusTech  
EaseTec  
Computer Zone (CZone)  
Pak Dukaan  


### How to run ###  
Download all the files  
Open the terminal in the same directory and enter the following command: python main.py Your Search.  
An excel workbook will be created with your results in the same directory as the download.  


### Prereqs ###  
Python must be installed on your device.  
BeautifulSoup and Pandas library must be installed on the same device.  


EXAMPLE:  
Command: python main.py Power Supply  
Open file: Power_Supply.xlsx  


### Future Updates ###  
More websites such as Czone and PakDukaan  


### Limitations ###  
1) The number of items retrieved from each site is based on their default setting of how many items they display. So if they display 10 items on default, then at most the 10 cheapest items are retrieved.  
2) The relevance of the results are based on how good the user search is and the website.  
3) Speed of code depends on user internet speed.  
