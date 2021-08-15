import boto3

iam = boto3.client('iam')
sts = boto3.client('sts')

# Get the arn represented by the currently configured credentials
arn = sts.get_caller_identity()['Arn']

# Create an arn representing the objects in a bucket
bucket_objects_arn = 'arn:aws:s3:::%s/*' % 'my-test-bucket'

# Run the policy simulation for the basic s3 operations
results = iam.simulate_principal_policy(
    PolicySourceArn=arn,
    ResourceArns=[bucket_objects_arn],
    ActionNames=['s3:PutObject', 's3:GetObject', 's3:DeleteObject']
)
for result in results['EvaluationResults']:
    print("%s - %s" % (result['EvalActionName'], result['EvalDecision']))