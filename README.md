# home-assignment-replace <BR>
Home assignment to find and replace strings <BR>
## Task: <BR>
Two departments, integration and finance, have lambda functions they need to deploy to AWS. <BR>
Each department has three environments <BR>
Write code to create a new AWS template file, based the file template.yaml and the parameters in each json file <BR>
The input parameters for the script should be: <BR>
1. department name <BR>
2. target environment <BR>

For example, the command: <BR>
` script --department integration --environment dev `
    
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
1. encode whitespace in route53Url parameter
