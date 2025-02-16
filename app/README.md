REQIREMENT

Minimalist Application Development / Docker / Kubernetes

Tiny App Development: 'SimpleTimeService'

•	Create a simple microservice (which we will call "SimpleTimeService") in any programming language of your choice: Go, NodeJS, Python, C#, Ruby, whatever you like.

•	The application should be a web server that returns a pure JSON response with the following structure, when its / URL path is accessed:

{
  "timestamp": "<current date and time>",
  "ip": "<the IP address of the visitor>"
}

Dockerize SimpleTimeService

•	Create a Dockerfile for this microservice.

•	Your application MUST be configured to run as a non-root user in the container.

Build SimpleTimeService image

•	Publish the image to a public container registry (for example, DockerHub) so we can pull it for testing.

Push your code to a public git repository

•	Push your code to a public git repository in the platform of your choice (e.g. GitHub, GitLab, Bitbucket, etc.). MAKE SURE YOU DON'T PUSH ANY SECRETS LIKE API KEYS TO A PUBLIC REPO!

•	We have a recommended repository structure here.


ACCEPTANCE CRITERIA

Your task will be considered successful if a colleague is able to build/run your container, and the application gives the correct response.

docker build must be the only command needed to build your container, and docker run must be the only command needed to run your container. Your container must run and stay running.

Other criteria for evaluation will be:

•	Documentation: you MUST add a README file with instructions to deploy your application.

•	Code quality and style: your code must be easy for others to read, and properly documented when relevant.

•	Container best practices: your container image should be as small as possible, without unnecessary bloat.

•	Container best practices: your application MUST be running as a non-root user, as specified in the exercise.


SIMPLE_TIME_SERVICE

                            
A minimalist Python microservice that returns the current timestamp and the visitor's IP address in JSON format.

________________________________________
Table of Contents

1.	Overview
2.	Prerequisites
3.	Repository Structure
4.	How to Run Locally
5.	How to Run Using Docker
6.	How to Use the Service
7.	How to Deploy to DockerHub
8.	How to Push Code to GitHub
9.	Troubleshooting
10.	Best Practices

________________________________________

Overview

The SimpleTimeService is a simple Python microservice built using Flask. It serves as a web server that returns a JSON response when accessed. The response includes:

•	The current date and time (timestamp).

•	The IP address of the visitor (ip).

The application is containerized using Docker, runs as a non-root user, and is published to a public container registry (e.g., DockerHub). The code is hosted in a public Git repository.

________________________________________

Prerequisites

Before starting, ensure you have the following installed:

1.	Python 3.9 or later.

2.	Docker installed on your machine.

3.	A DockerHub account (or any other container registry account)
  
4.	Git installed for version control.

________________________________________
Repository Structure

Copy

app/

├── app.py                # Python microservice code

├── Dockerfile            # Dockerfile for containerization

├── requirements.txt      # Python dependencies

├── README.md             # Documentation

└── .gitignore            # Git ignore file

________________________________________

How to Run Locally

Step 1: Clone the Repository

              git clone https://github.com/yashasgit/Particle41-DevOps-Team-Challenge.git

              cd Particle41-DevOps-Team-Challenge

              cd app

Step 2: Install Dependencies and python3-pip and docker

              sudo apt  install docker.io

              sudo apt install python3-pip

              sudo apt-get install requirements.txt

Step 3: Run the Application

             python app.py

Step 4: Access the Service

Open your browser or use curl to access the service: (local host = public ip address)

          Curl http://localhost:5000

________________________________________

How to Run Using Docker

Step 1: Build the Docker Image

           docker build -t simple-time-service:latest .

Step 2: Run the Docker Container

         docker run -d -p 5000:5000 simple-time-service:latest

Step 3: Access the Service

           Open your browser or use curl to access the service:

            curl http://localhost:5000

________________________________________

How to Use the Service

Once the service is running (either locally or in a Docker container), you can interact with it using the following methods:

1. Using a Web Browser
 
1.	Open your web browser.
   
3.	Navigate to http://localhost:5000.
   
5.	You will see a JSON response like this:
   
{

  "ip": "223.185.128.101",
  
  "timestamp": "2025-02-16T17:44:55.975596Z"
  
}

2. Using curl
   
1.	Open a terminal.
   
3.	Run the following command:
   
curl http://localhost:5000

6.	You will see a JSON response like this:
   
Json
{
  "ip": "223.185.128.101",
  
  "timestamp": "2025-02-16T17:44:55.975596Z"
  
}


________________________________________

How to Deploy to DockerHub

Step 1: Log in to DockerHub

          docker login

Step 2: Tag the Docker Image (replace your-dockerhub-username)

         docker tag simple-time-service:latest yashasdocker /simple-time-service:latest

Step 3: Push the Docker Image (replace your-dockerhub-username)

          docker push  yashasdocker /simple-time-service:latest

Step 4: Pull and Run the Image (replace your-dockerhub-username)

        docker pull yashasdocker /simple-time-service:latest

        docker run -d -p 5000:5000  yashasdocker /simple-time-service:latest

________________________________________

How to Push Code to GitHub

Step 1: Initialize a Git Repository

         git init

Step 2: Add Files to the Repository

      git add .

Step 3: Commit the Changes

       git commit -m "Initial commit: SimpleTimeService microservice"

Step 4: Add the Remote Repository

       git remote add origin https://github.com/yashasgit/Particle41-DevOps-Team-Challenge.git

Step 5: Push the Code

        git branch -M main

        git push -u origin main

________________________________________

Troubleshooting

1. Permission Denied for Docker
2. 
If you encounter permission issues while running Docker commands:

•	Add your user to the docker group:

       sudo usermod -aG docker $USER

       newgrp docker

•	Alternatively, use sudo:

       sudo docker build -t simple-time-service:latest .

4. Port Conflict

If port 5000 is already in use, change the host port in the docker run command:

        docker run -d -p 5001:5000 simple-time-service:latest

6. Repository Not Found

Ensure the remote repository URL is correct:

         git remote set-url origin https://github.com/yashasgit/Particle41-DevOps-Team-Challenge.git

________________________________________

Best Practices

1.	Non-Root User:

o	The application runs as a non-root user (myuser) inside the container for security.

2.	Minimal Image Size:

o	The python:3.9-slim base image is used to keep the container lightweight.


