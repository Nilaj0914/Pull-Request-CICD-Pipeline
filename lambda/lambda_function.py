import json
#test change
def lambda_handler(event, context):
    return{
        'statusCode': 200,
        'body': json.dumps('Hello lambda, this is a new workflow file')
    }