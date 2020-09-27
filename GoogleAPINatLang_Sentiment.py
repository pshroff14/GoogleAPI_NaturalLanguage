
from google.cloud import language

client=language.LanguageServiceClient()
annotate=client.analyze_sentiment("hello this is a great time to run")
print_result(annotate)