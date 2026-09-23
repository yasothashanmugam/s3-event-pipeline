# AWS Serverless Data Processing Pipeline

## Problem Statement

Organizations often need to process files uploaded to cloud storage and perform actions such as metadata extraction, notifications, monitoring, and auditing. Manually handling these tasks can be time-consuming, error-prone, and difficult to scale. A serverless and event-driven solution is required to automatically process uploaded files, store metadata, send notifications, and provide monitoring and security controls while minimizing operational overhead.

## Solution

This project implements an AWS Serverless Data Processing Pipeline using Amazon S3, AWS Lambda, DynamoDB, SNS, CloudWatch, CloudTrail, IAM, and EventBridge.

Whenever a file is uploaded to an Amazon S3 bucket, an event is generated and triggers an AWS Lambda function. The Lambda function processes the uploaded file, extracts metadata, stores the metadata in a DynamoDB table, and sends notifications through Amazon SNS. CloudWatch is used for monitoring, logging, and alerting, while CloudTrail provides auditing and activity tracking. Security controls such as IAM roles, encryption, and access restrictions are implemented to ensure secure operation of the pipeline.

The project also includes performance testing, scalability validation, reliability testing, error handling, monitoring, and security compliance verification.

## Setup Steps

### Week 1 - Environment Setup and Foundation

#### Day 1
- Created AWS account and configured project environment
- Installed AWS CLI
- Verified AWS CLI installation
- Created IAM user and assigned permissions
- Explored AWS Management Console services

#### Day 2
- Created Amazon S3 bucket
- Configured bucket settings
- Enabled bucket versioning
- Enabled server-side encryption
- Tested file upload functionality

#### Day 3
- Created GitHub repository
- Added README and project structure
- Configured Git and GitHub integration
- Performed initial commit

#### Day 4
- Configured AWS credentials
- Set up development environment
- Prepared project workspace
- Verified AWS connectivity

#### Day 5
- Reviewed Week 1 activities
- Verified configurations
- Updated documentation
- Completed Week 1 deliverables

---

### Week 2 - Event Pipeline Foundation

#### Day 8
- Configured S3 bucket notifications
- Tested S3 event configuration

#### Day 9
- Created AWS Lambda function
- Developed event processing logic
- Tested Lambda execution

#### Day 10
- Created CloudFormation stack
- Integrated S3 event pipeline
- Tested event-driven workflow

#### Day 11
- Implemented CloudWatch logging
- Configured monitoring and alarms
- Added Lambda error handling

---

### Week 3 - Event Processing and Notifications

#### Day 15
- Verified S3 configuration
- Reviewed permissions and versioning

#### Day 16
- Configured Lambda event processing
- Connected S3 and Lambda
- Tested event handling

#### Day 17
- Created SNS topic and subscription
- Integrated SNS notifications

#### Day 18
- Integrated complete pipeline
- Verified event processing workflow
- Monitored execution using CloudWatch

---

### Week 4 - Auditing and Validation

#### Completed Activities
- Integrated CloudTrail auditing
- Verified IAM roles and permissions
- Tested different file scenarios
- Validated DynamoDB consistency
- Fixed Lambda event format issues
- Verified SNS notifications
- Verified CloudWatch monitoring

---

### Week 5 - Advanced Event Processing

#### Completed Activities
- Configured S3 event notifications
- Implemented event filtering
- Verified Lambda trigger execution
- Tested S3 versioning functionality
- Optimized event processing workflow

---

### Week 6 - Performance, Scalability and Security Validation

#### Completed Activities
- Designed performance testing scenarios
- Performed load and stress testing
- Verified scalability and reliability
- Implemented security validation
- Verified encryption and IAM controls
- Validated CloudTrail auditing
- Optimized DynamoDB performance using GSI
- Improved Lambda error handling
- Verified CloudWatch monitoring and alerts

### Final Outcome

The project successfully implements a serverless event-driven architecture using AWS services. Uploaded files are automatically processed through Lambda, metadata is stored in DynamoDB, notifications are delivered through SNS, and monitoring, auditing, security, scalability, and reliability requirements are validated using CloudWatch and CloudTrail.


## Screenshots

### S3 Bucket
This screenshot shows the Amazon S3 bucket used in the project. Versioning and encryption are enabled, and uploaded files trigger the event-driven pipeline.

![S3 Bucket](screenshots/S3-bucket.png)

---

### Lambda Function
This screenshot shows the AWS Lambda function responsible for processing S3 object creation events, storing metadata in DynamoDB, and sending SNS notifications.

![Lambda Function](screenshots/Lambda-function.png)

---

### DynamoDB Table
This screenshot shows the DynamoDB table used to store metadata about uploaded S3 objects, including bucket name and object key information.

![DynamoDB Table](screenshots/dynamodb-table.png)

---

### SNS Topic
This screenshot shows the Amazon SNS topic configuration used for sending email notifications whenever a file is successfully processed by the pipeline.

![SNS Topic](screenshots/sns-topic.png)

---

### CloudWatch Logs
This screenshot shows CloudWatch logs generated by the Lambda function, including successful execution details, monitoring information, and troubleshooting logs.

![CloudWatch Logs](screenshots/cloudwatch-logs.png)

---

### CloudTrail Event History
This screenshot shows CloudTrail event history used for auditing AWS resource activities and verifying security-related actions performed within the project.

![CloudTrail Event History](screenshots/cloudtrail-events.png)
