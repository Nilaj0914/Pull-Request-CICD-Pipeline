# Pull-Request-CICD-Workflow

Built a basic GitHub Actions workflow that automatically detects a CloudFormation YAML file and validates it by deploying a CloudFormation Stack to AWS whenever a Pull Request is created. If all the resources are successfully created, it returns a confirmation message. When the Pull Request is merged to the main branch, the CloudFormation Stack is deleted, thereby deleting the provisioned resources.
