REFERENCE: https://issuetracker.google.com/issues/122953704


https://cloud.google.com/functions/docs/concepts/iam
https://cloud.google.com/functions/docs/quickstart-console
https://cloud.google.com/functions/docs/securing/function-identity#updating_the_identity_of_an_existing_function

Python dependencies:
https://cloud.google.com/functions/docs/concepts/python-runtime

gcloud app deploy -v patch-cf 
TEST ENDPOINT: http://patch-cf-dot-wp-phpso2-8738.appspot.com/ 
TEST ENDPOINT https://drogon-flex.appspot.com 


========FROM vision-api project

dev_appserver.py app.yaml 
## curl -H "Content-Type: application/json" --data @photoPortrait.json "http://localhost:8080/info" 
## curl -H "Content-Type: application/json" --data @photoPortrait.json "http://localhost:8080/info" 
"gsutil cp -r gs://cmosquera-dev.appspot.com/* ." 
gcloud app deploy -v imageapi-py27 
gcloud app deploy -v imageapi-py27-v2 
"pip install GoogleAppEngineCloudStorageClient -t lib" 
curl -H "Content-Type: application/json" --data @photoPortrait.json "https://cmosquera-dev.appspot.com/info" 
