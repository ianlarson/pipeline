from aws_cdk import (aws_s3 as s3, core, aws_ec2 as ec2)
from aws_cdk.core import Stack, StackProps, Construct, SecretValue
from aws_cdk.pipelines import CdkPipeline, SimpleSynthAction


class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self,
                           "illarsoMyFirstBucket12341234",
                           bucket_name='illarsomyfirstbucket12341234',
                           versioned=False,
                           public_read_access=False,
                           removal_policy=core.RemovalPolicy.DESTROY)

        # vpc = ec2.Vpc(self, "TheVPC",
        #               cidr="10.1.0.0/16")

