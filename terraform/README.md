Terraform and Cloud: create the infrastructure to host your container.

REQUIREMENT:

Using Terraform, create the following infrastructure in AWS (or equivalent):

•	If server-based:

o	A VPC with 2 public and 2 private subnets.

o	An ECS/EKS or equivalent cluster deployed to that VPC.

o	A ECS/EKS task/service resource to run your container.

o	The tasks and/nodes must be on the private subnets only.

o	A load balancer deployed in the public subnets to offer the service.


Terraform EKS Cluster with ALB
This Terraform project provisions an Amazon EKS (Elastic Kubernetes Service) cluster with worker nodes, a VPC, public and private subnets, an Application Load Balancer (ALB), and associated resources. The infrastructure is designed to be highly available and secure.
________________________________________
Table of Contents
1.	Prerequisites
2.	Project Structure
3.	Resources Created
4.	How to Use
	
Step 1: Set Up AWS Credentials

Step 2: Clone the Repository

Step 3: Initialize Terraform

Step 4: Plan and Apply

6.	Outputs
7.	Clean Up
8.	Troubleshooting
9.	Contributing

________________________________________
Prerequisites
Before using this Terraform project, ensure you have the following:
1.	AWS Account:
o	An AWS account with sufficient permissions to create EKS clusters, VPCs, subnets, IAM roles, and other resources.
2.	AWS CLI:
o	Install the AWS CLI and configure it with your credentials:
               aws configure

3.	Terraform: 
o	Install Terraform (v1.0.0 or higher).

          sudo snap install terraform --classic


5.	SSH Key Pair:
o	Create an SSH key pair in the AWS region (ap-south-1) where the EKS cluster will be deployed. Replace yashaskey in the aws eks node group resource with your key pair name.
________________________________________
Project Structure
The project is organized as follows:

.
├── main.tf              # Main Terraform configuration

├── README.md            # Documentation

________________________________________
Resources Created
This Terraform configuration creates the following resources:
1.	VPC:
   
o	A VPC with CIDR block 10.0.0.0/16.

3.	Subnets:
   
o	Two public subnets (10.0.1.0/24, 10.0.2.0/24) with internet access.

o	Two private subnets (10.0.3.0/24, 10.0.4.0/24) for EKS worker nodes.

5.	Internet Gateway (IGW):

o	Attached to the VPC for public subnet internet access.

7.	NAT Gateway:
   
o	Allows private subnets to access the internet for updates and downloads.

9.	EKS Cluster:
   
o	A managed Kubernetes cluster with a control plane in private subnets.

11.	EKS Node Group:

o	Worker nodes for the EKS cluster, deployed in private subnets.

13.	Application Load Balancer (ALB):

o	A public-facing ALB to route traffic to applications running in the EKS cluster.

15.	IAM Roles:

o	Roles for the EKS cluster and worker nodes with necessary permissions.

17.	Security Groups:

o	Security groups for EKS nodes and the ALB.

________________________________________
How to Use

Step 1: Set Up AWS Credentials

Ensure your AWS credentials are configured. You can set them as environment variables or use the AWS CLI:

      aws cli

export AWS_ACCESS_KEY_ID="your-access-key-id"

export AWS_SECRET_ACCESS_KEY="your-secret-access-key"

export AWS_DEFAULT_REGION="ap-south-1"

Default output format [None]: json

Step 2: Clone the Repository

Clone this repository to your local machine:

         git clone https://github.com/yashasgit/Particle41-DevOps-Team-Challenge.git 

         cd Particle41-DevOps-Team-Challenge

         cd terraform

Step 3: Initialize Terraform

Initialize Terraform to download the required providers:

         terraform init



Step 4: Plan and Apply

1.	Plan:

Generate an execution plan to review the changes:

           terraform plan

3.	Apply:

Apply the configuration to create the resources:

            terraform apply

Confirm the action by typing yes when prompted.

________________________________________
Outputs

After applying the configuration, Terraform will output the following:

1.	EKS Cluster Name:

eks_cluster_name = "my-eks-cluster"

3.	ALB DNS Name:

alb_dns_name = "app-load-balancer-229508187.ap-south-1.elb.amazonaws.com"

You can access your application using the ALB DNS name.

________________________________________
Clean Up

To destroy all resources created by this Terraform configuration, run:

              terraform destroy

Confirm the action by typing yes when prompted.

________________________________________
Troubleshooting

1.	SSH Key Pair Not Found:

o	Ensure the SSH key pair (yashaskey) exists in the ap-south-1 region. (Replace it with your key pair name.)

3.	IAM Role Permissions:

o	Ensure the IAM roles have the required permissions. Attach the following policies:

	AmazonEKSClusterPolicy

	AmazonEKSVPCResourceController

	AmazonEKSWorkerNodePolicy

	AmazonEKS_CNI_Policy

	AmazonEC2ContainerRegistryReadOnly

	Here I gave AdministratorAccess (not recommended)

