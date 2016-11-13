import argparse
from googleapiclient import discovery
import httplib2
import json
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                 '$discovery/rest?version={apiVersion}')

def main():
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
         'content': "Kye is a stupid motherfucker. Kye should feel ashamed of himself. Nobody should like Kye or Jesson. Jesson is also stupid. Stupid is as stupid does.",
      }
    })

  response = service_request.execute()
  #polarity = response['documentSentiment']['polarity']
  #magnitude = response['documentSentiment']['magnitude']
  #print('Sentiment: polarity of %s with magnitude of %s' % (polarity, magnitude))
  return response

def callChain():
  #parser = argparse.ArgumentParser()
  #parser.add_argument(
#    'movie_review_file', help='The filename of the movie review you\'d like to analyze.')
  #args = parser.parse_args()
  return main()
