from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_efs as efs


class CdkEfsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        """ If you want to use an existing VPC, uncomment the 
        following, specify the VPC ID you want to use.
        """
        # vpc = ec2.Vpc.from_lookup(
        #     self, "MyVPC",
        #     vpc_id="vpc-12345678"
        # )

        """ This will build a new VPC. Comment this out if you are
        using an existing one declared above.
        """
        vpc = ec2.Vpc(
            self, "MyVpc",
            cidr="10.10.0.0/16"
        )

        # Example EFS filesystem
        # All options: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_efs/FileSystem.html
        efs_filesystem = efs.FileSystem(
            self, "ExampleEFSFileSystem",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE)
        )
