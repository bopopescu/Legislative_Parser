import argparse
from googleapiclient import discovery
import httplib2
import json
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                 '$discovery/rest?version={apiVersion}')

def main(input_text):
  '''Run a sentiment analysis request on text within a passed filename'''

  http = httplib2.Http()

  credentials = GoogleCredentials.get_application_default().create_scoped(
      ['https://www.googleapis.com/auth/cloud-platform'])
  http=httplib2.Http()
  credentials.authorize(http)

  service = discovery.build('language', 'v1beta1',
                            http=http, discoveryServiceUrl=DISCOVERY_URL)

  #review_text = open(movie_review_file, 'r')
  service_request = service.documents().analyzeEntities(
    body={
      'document': {
         'type': 'PLAIN_TEXT',
         'content': input_text,
      }
    })

  response = service_request.execute()
  #polarity = response['documentSentiment']['polarity']
  #magnitude = response['documentSentiment']['magnitude']
  #print('Sentiment: polarity of %s with magnitude of %s' % (polarity, magnitude))
  return response

def callChain(input_text):
  #parser = argparse.ArgumentParser()
  #parser.add_argument(
#    'movie_review_file', help='The filename of the movie review you\'d like to analyze.')
  #args = parser.parse_args()
  return main(input_text)
