# s3-event-pipeline

AWS S3 Event Pipeline using EventBridge, Lambda and CloudWatch

## Week 1: S3 Event Pipeline Setup

### Day 1 - Introduction to S3 Event Pipeline
- Created and configured AWS account for the project
- Installed AWS CLI on local machine
- Verified AWS CLI installation
- Created IAM user with required permissions
- Explored AWS Management Console services

### Day 2 - S3 Bucket Creation
- Created Amazon S3 bucket
- Configured bucket settings
- Enabled versioning
- Enabled server-side encryption
- Tested file upload functionality

### Day 3 - GitHub Repository Setup
- Created GitHub repository for the project
- Added README.md and .gitignore files
- Initialized repository structure
- Performed initial commit
- Linked local project with GitHub repository

### Day 4 - Environment Setup and Configuration
- Configured AWS credentials and environment variables
- Prepared local development environment
- Set up project workspace
- Created project documentation notes
- Verified AWS connectivity through CLI commands

### Day 5 - Week 1 Review
- Reviewed completed tasks
- Verified AWS and GitHub configurations
- Updated project documentation
- Organized project files
- Completed Week 1 deliverables

## Week 1 Outcome

Successfully established the AWS environment, configured Amazon S3, and prepared the GitHub repository for the S3 Event Pipeline project. This provided the foundation for implementing event-driven processing in subsequent weeks.



## Week 2: S3 Event Pipeline Foundation

### Day 8 - S3 Bucket Configuration
- Created S3 bucket
- Enabled versioning
- Configured bucket notifications
- Tested bucket setup

### Day 9 - Lambda Function Development
- Created AWS Lambda function
- Developed Python code for event processing
- Tested Lambda execution

### Day 10 - Event Pipeline Integration
- Created CloudFormation stack
- Integrated S3 event processing architecture
- Tested pipeline components

### Day 11 - Error Handling and Monitoring
- Implemented try-except error handling
- Configured CloudWatch logging
- Viewed CloudWatch metrics
- Created CloudWatch alarm
- Tested monitoring setup

## Technologies Used

- Amazon S3
- AWS Lambda
- Amazon EventBridge
- Amazon CloudWatch
- AWS CloudFormation

## Outcome

Successfully developed a functional S3 Event Pipeline prototype using AWS services.

## Week 3: Event Processing and Notifications

### Day 15 - S3 Bucket Configuration

- Verified S3 bucket configuration
- Reviewed bucket permissions
- Confirmed versioning settings
- Verified event notifications
- Tested bucket functionality

### Day 16 - Lambda Event Processing

- Created AWS Lambda function
- Developed Python code for S3 event handling
- Configured Lambda triggers
- Tested Lambda execution
- Deployed Lambda function

### Day 17 - SNS Notification Integration

- Created Amazon SNS topic
- Configured email subscription
- Tested SNS message delivery
- Integrated SNS with Lambda function

### Day 18 - Event Pipeline Integration

- Integrated S3 bucket with Lambda
- Configured event pipeline execution
- Tested event processing workflow
- Monitored pipeline using CloudWatch
- Reviewed performance optimization

## Week 3 Outcome

Successfully implemented an event-driven architecture using Amazon S3, AWS Lambda, Amazon SNS, EventBridge, and CloudWatch.


## Week 4 

### Completed Tasks

- Integrated AWS CloudTrail for S3 event auditing
- Verified IAM roles and permissions
- Tested pipeline with multiple file scenarios (.txt, .jpg, .pdf)
- Validated data consistency between S3 and DynamoDB
- Fixed Lambda event format bug
- Verified SNS notifications
- Verified CloudWatch logging and monitoring

### Results

- Successfully processed S3 object events
- Stored metadata in DynamoDB
- Sent notifications through SNS
- Audited events using CloudTrail
- Improved reliability through testing and bug fixes

## Week 6 - Performance, Scalability and Security Validation

### Completed Tasks

- Designed and implemented performance and scalability testing.
- Tested pipeline under multiple upload and load conditions.
- Verified pipeline reliability and scalability.
- Implemented and validated CloudWatch monitoring.
- Verified S3, DynamoDB and IAM security configurations.
- Validated CloudTrail auditing and encryption settings.
- Fixed Lambda event processing issues.
- Optimized pipeline using event filtering and DynamoDB indexing.

### Results

- Successful Lambda execution
- Successful DynamoDB updates
- Successful SNS notifications
- No data loss observed
- No critical performance bottlenecks identified
