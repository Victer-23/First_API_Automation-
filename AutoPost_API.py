import requests
import configparser

from urllib3.util import Url
from utilities.resources import *
from payload import *
from payload_deleteBook import *
from utilities.configuration import *

url_addBook=getconfig()['API']['endpoint']+LibraryResoarces.addbook
url_deleteBook=getconfig()['API']['endpoint']+LibraryResoarces.deletebook
headers={"Content-Type": "application/json"}
Addbook_response = requests.post(url_addBook,
                                 json=addBookPayload(isbn=152),
                                 headers=headers, )
Post_response = Addbook_response.json()
print(Post_response)
print(Addbook_response.status_code)

book_id = Post_response['ID']
Del_book = requests.post(url_deleteBook,
                         json=delete_book(book_id),
                         headers=headers, )

# headers={"Content-Type" : "application/json"},)
response_del = Del_book .json()
print(response_del)
print(Del_book .status_code)




