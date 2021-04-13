from bs4 import BeautifulSoup

data = open("./data.txt", "r")
soup = BeautifulSoup(data, 'html.parser')

courseTitles = soup.find_all('h3')
print(courseTitles)
print('Ran to end!')