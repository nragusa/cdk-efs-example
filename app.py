#!/usr/bin/env python3

from aws_cdk import core

from cdk_efs.cdk_efs_stack import CdkEfsStack

app = core.App()

""" If you would like to use an existing VPC, uncomment out
the following lines and be sure to specify the appropriate values
in cdk.json.
"""
# aws_account = app.node.try_get_context("aws_account")
# aws_region = app.node.try_get_context("aws_region")
# environment = core.Environment(account=aws_account, region=aws_region)

efs_stack = CdkEfsStack(app, "cdk-efs")
""" Uncomment if using an existing VPC, and comment the 
line above.
"""
# efs_stack = CdkEfsStack(app, "cdk-efs", env=environment)
core.Tags.of(efs_stack).add("Project", "EFS Test")
core.Tags.of(efs_stack).add("Environment", "Development")

app.synth()
