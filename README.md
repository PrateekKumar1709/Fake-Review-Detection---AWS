# Fake Review Detector

## Overview:

In this project I have implemented a syatem (machine learning model) to predict whether a review is fake or not. Furthermore, the system also provides additional information about the review like probability score for the review, sentiment etc.

## Architecture:

![image](https://github.com/PrateekKumar1709/Fake-Review-Detection-AWS/blob/main/screenshots/Architecture.png)

## Tech Stack:

Main Tech Stack includes:
AWS S3
AWS Sagemaker
AWS API Gateway
AWS Cognito
AWS Elasticsearch service
AWS Codebuild
AWS Cloudformation
AWS Comprehend
Kibana (for Data Visualisation)
ReactJS / NodeJS(Front End)
REST

## Implementation:

In order to detect fake reviews we would first obtain data from the Yelp Open Data Set regarding businesses, users, reviews etc. The next and most important step in building thei application is the Machine Learning model development. As part of this the first step is to analyse the data. An initial EDA (Exploratory Data Analysis) will be done to investigate which features can help identify fake reviews. Various techniques like stop word removal, stemming, tokenization etc. will be done as part of the EDA and data processing using AWS Comprehend. Then feature engineering will be performed to normalise the data. Once this is done the next step would be to use the labelled data to train the model using AWS sagemaker. Then the model validation will be performed to tune the hyperparameter using the test data to improve the accuracy of the model. Once the model development is complete the model artifacts will be stored in AWS S3 bucket to be used later for review detection. Using this model we will detect the fake review on the actual data and then store the result data in Elasticsearch for a quick analysis in Kibana dashboards which are user intuitive and easy to understand.   

## Flow:

The user logs into the application and signs in using the AWS Cognito service. The user is presented with the home page of the application. 
The user can then upload the review using the upload review API. The API sends the user input to the lambda function where the review is cleaned, tokenized etc. and then run through the model to predict whether the review is fake or authentic and calculates the probability score and then stored in elasticsearch for analysis later.
When the user clicks on the show result button another API - Show Review is called which invoke another lambda function which fetches the result form elasticsearch and returns it back to the user on the application screen with result and probability score.
Lastly when the user clicks on the show analytics button a new screen is displayed with a dashboard which shows details about the review to the user. The user can also see past reviews which were upload in the application and the results for the same. The dashboard is very interactive and provides drill down capabilities.

## API Description:

fakeReviewDetector

/uploadReview::
 POST::
   description: Sends a review that the user has input
   produces::
   - application/json
   responses::
     '200':
       description:: Successfully Uploaded
       schema::
         type:: string

/showReview:
 GET:
   description: Fetches the result of the review (Fake or Authentic)
   produces:
   - application/json
   responses:
     '200':
       description: Result
       schema:
         type: string


## Result:

The application provides the user with detailed information about the review like authenticity, probability score, sentiment etc. with a dynamic dashboard which has an accuracy of approx 80%.
This can be very beneficial for business and consumers to distinguish authentic reviews from fake ones.


