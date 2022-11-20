# home-assignment-replace
Home assignment to find and replace strings
## Task:
Two departments have lambda functions they need to deploy to AWS.
Each department has an AWS account, and three environments for each account
Write code to create a new AWS template file, based the input parameters in each json file
The input parameters for the script should be:
1. department name
2. target environment
For example, the command:
script --department integration --environment dev
Will change this part in template.yaml file:
```
    Properties:
      FunctionName: ${_awsStackName_}
      CodeUri: .
      MemorySize: ${_memorySize_}
      Role: ${_lambdaRole_}
      Handler: ${_handler_}
      Runtime: ${_runtime_}
    Metadata:
      BuildMethod: ${_buildMethod_}
```
to create the following output:
```
    Properties:
      FunctionName: integrationDevtack
      CodeUri: .
      MemorySize: 1MB
      Role: integrationDevRole
      Handler: lambda_function.lambda_handler
      Runtime: python3.9
    Metadata:
      BuildMethod: python3.9
```
## Bonus points:
1. escape whitespace in awsStackName parameter
