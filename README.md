# Prediction Endpoint
This Repository is a prediction endpoint for Reverse Image Search Engine. With the use of gitHub actions 
I have configured CI-CD on the main branch. If any changes happens in Main branch it will deploy it on ec2 instance.

## Architectures 
![EndpointArchitecture](https://user-images.githubusercontent.com/40850370/194845911-ea1b68f5-22db-4190-ab94-eca46f6a9d37.png)
![Endpoint](https://user-images.githubusercontent.com/40850370/194845906-fc28aeb7-c2b2-4524-8814-4192cd5311bc.png)

## User Interface
![plot](snippets/snip1.png)

## Infrastructure Needed
1. GitHub Actions
2. Elastic Container Registry
3. S3 Bucket and Mongo
4. Elastic Cloud Compute

## Project Setup

Get Aws Access Creds and update in Secrets.
```bash
export AWS_ACCESS_KEY_ID=<access-key>
export AWS_SECRET_ACCESS_KEY=<secret-key>
export AWS_REGION=<aws-region>

export AWS_BUCKET_NAME=<bucket-name>

export AWS_ECR_LOGIN_URI=<ecr-login-uri>
export ECR_REPOSITORY_NAME=<ecr-repository-name>
```

## Cost Involved
```text
EC2 Instance : 	2vCPUs $0.0928 	On-Demand Price/hr*
ECR Repository : Storage is $0.10 per GB / month for data stored in private or public repositories.
    Data Transfer IN : $0.00 per GB
    Data Transfer OUT **: $0.1093 per GB / Next 9.999 TB / month
S3 Standard: $0.025 per GB / First 50 TB / Month
```
