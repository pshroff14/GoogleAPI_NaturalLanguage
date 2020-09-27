from google.cloud import language
from google.cloud.language import enums, types


#Authentication import
from gcloud.aio.auth import IamClient
from gcloud.rest.auth import Token
client = IamClient()
pubkeys = await client.list_public_keys()
token = Token()
print(token.get())
print("-----------------")



def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = [
        ('text', text),
        ('score', sentiment.score),
        ('magnitude', sentiment.magnitude),
    ]
    for k, v in results:
        print('{:10}: {}'.format(k, v))

text = "Hello today is a great and sunny day"
analyze_text_sentiment(text)




