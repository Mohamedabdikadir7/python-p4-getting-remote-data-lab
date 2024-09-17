import requests
import json

class GetRequester:

# def __init__(self, url):
# # url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
# # response = requests.get(url)
# # return requests.content
  def __init__(self, url):
# The code here should be indented
   self.url = url
  def get_response_body(self):
   response = requests.get(self.url)
   return response.content

  def load_json(self):
   response_body = self.get_response_body() 
   return json.loads(response_body) 
