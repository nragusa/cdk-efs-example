#!/usr/bin/env python3

from aws_cdk import core

from cdk_efs.cdk_efs_stack import CdkEfsStack


app = core.App()
CdkEfsStack(app, "cdk-efs")

app.synth()
