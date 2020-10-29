# Example EFS File System with CDK

The following CDK application will create a new VPC and stand up an EFS file system in it.

You can optionally specify an existing VPC, but will require setting some parameters. More details on that below.

## Getting Started

First, make sure you have all the prerequisites completed. A list of what's needed can be [found here](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites).

Once complete, clone this repository and stand up a virtualenv with the required modules installed:

```
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

The synthesized CloudFormation template gets printed to stdout, and a version of it gets created in the directory `cdk.out`.

When you're ready to deploy, simply run:

```
$ cdk deploy
```

## Use an existing VPC

If instead you'd like to use a VPC that already exists, you'll need to make a few edits. There are commented examples to help out.

1. Edit `cdk_efs/cdk_efs_stack.py` and specify the VPC ID of the VPC you'd like to use. There is an example in the file for you. Also, remove the existing `vpc` declaration.
2. Edit `cdk.json` and specify an appropriate AWS Accound ID and AWS region.
3. Edit `app.py` and uncomment out lines 13 - 15, remove line 17, amd uncomment line 21.

That's it! When you synthesize the app, it will create a new file locally, `cdk.context.json`, which will have information related to your VPC. When you deploy, it will use the information in this file to stand up the resources appropriately.

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation
