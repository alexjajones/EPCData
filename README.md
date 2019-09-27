# EPC Data

# Simple answer
As the amount of data is small, requires infrequent imports and is not time critical I would recommend a simple configurable script that imports/processes/exports the data on a cron schedule as shown in this codebase.

The application is wrapped in docker and would be hosted on a managed platform (ECS/Fargate) and scheduled with cloudwatch event rules (https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html)

## How to run locally
Run application `docker-compose up`
Run tests
 - `python3.7 -m pip install -r requirements-dev.txt`
 - `python3.7 -m pytest -q test`

# Production example
As can be seen from the DataPipeline.png I would recommend a systems more akin to this as the data requirements grow.
 - Visability of all task history
 - Centralised and managed datalake with SQL interface (BigQuery)
 - Paper trail of where data has been around the system (good for GDPR)
 - Task dependency management
 - Secrets management
 - Flexible processing
 - Distributed compute resource frameworks for larger tasks
 - Not tied to any external or internal data stores

#Improvement
 - Finish the downloading and loading of the zip data set
 - Better database user configuration
 - Improved test coverage

# Other

## Configuration
Configuration would be injected to allow passing of secrets and easy multi env deployments (e.g. dev/prod)

## Why postgres?
 - Static well known schema
 - Allows validation
 - Quick and easy to run locally
 
## Considerations
 - Schema migrations