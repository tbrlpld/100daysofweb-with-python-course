# URL Shortener

Simple URL shortener do be hosted on AWS Lambda via Zappa. 

A simple Flask app creates the endpoints to interact with. 
Data is stored in a AWS DynamoDB. 


## Testing and Development

### Setup
Install the package in editable mode:
```shell
python -m pip install -e .
```

Install the development dependencies:
```shell
python -m pip install -e ".[develop]"
```

Testing (and development for that matter) requires a running local instance of Dynamo DB. The easiest way to get there is to have Docker on the testing machine, and download and run the local version of DynamoDB. See also:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html
https://hub.docker.com/r/amazon/dynamodb-local

To get the official DynamoDB docker image:
```shell
docker pull amazon/dynamodb-local
```

Then start the local container with:
```shell
docker run -p 8000:8000 amazon/dynamodb-local
```

### Running the Tests

Run the tests simply with 
```shell
pytest
```


### Deployment

This requires that AWS certificate for authentication and authorization is installed on the machine from which you are deploying. See this guide to setup AWS credential on your machine: https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/

Once this is in place, the initial deployment can be done with Zappa like so:
```shell
$ zappa deploy production
Deploying..
Your application is now live at: https://7k6anj0k99.execute-api.us-east-1.amazonaws.com/production
```

For development deployment, use `dev` instead of `production`. 

To an updated version of the Lambda function use:
```shell
$ zappa update production
Updating..
Your application is now live at: https://7k6anj0k99.execute-api.us-east-1.amazonaws.com/production
```

For more info, see the [Zappa README on GitHub](https://github.com/Miserlou/Zappa)

