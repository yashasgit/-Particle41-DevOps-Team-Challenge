Task 1: Minimalist Application Development / Docker / Kubernetes

In this task, we will create a simple microservice called SimpleTimeService that returns the current date and time along with the visitor's IP address in JSON format. We will then Dockerize the application, publish it to a public container registry, and push the code to a public Git repository.

________________________________________

Repository Structure

app/

├── app.py                # Python microservice code

├── Dockerfile            # Dockerfile for containerization

├── README.md             # Documentation

└── .dockergnore            # docker ignore file

Step 1: Create the SimpleTimeService Microservice

We will use Python with the Flask framework to create the microservice.

1.1 Install Python3, docker, Flask

First, install Python and docker on your system. Then, install Flask using pip:

     sudo apt install python3-pip -y

     sudo apt  install docker.io -y

     sudo apt install python3-flask -y

1.2 Create the Application

Create a file named app.py with python code:

~1.3 Test the Application Locally

Run the application:

     python app.py

Visit      http://localhost:8080      in your browser or use curl:

curl http://localhost:8080

You should see a JSON response like:
{
  "timestamp": "2023-10-25T12:34:56.789Z",
  "ip": "127.0.0.1"
}
________________________________________

Step 2: Dockerize the Application

2.1 Create a Dockerfile

Create a file named Dockerfile :

2.2 Create a .dockerignore File

Create a .dockerignore file to exclude unnecessary files from the Docker build context:

.git

__pycache__

*.pyc

2.3 Add Your User to the docker Group 

To avoid using sudo for Docker commands, add your user to the docker group:

1.	Add your user to the docker group:
   
        sudo usermod -aG docker $USER

2.	Log out and log back in, or refresh your session:

        newgrp docker
 
3.	Verify that you can run Docker commands without sudo:

        docker ps

2.4 Build the Docker Image

Run the following command to build the Docker image:

     docker build -t simple-time-service .

2.5 Run the Docker Container

Run the container:

          docker run -p 8080:8080 simple-time-service

Test the service:

     Visit http://localhost:8080 in your browser 

________________________________________

Step 3: Publish the Docker Image to a Public Registry

3.1 Tag the Docker Image

Tag the image with your DockerHub username:

     docker tag simple-time-service yashasdocker/simple-time-service:latest (change user name)

3.2 Push the Docker Image

Log in to DockerHub:

     docker login
     
3.3 push the image

     docker push yashasdocker /simple-time-service:latest  (change user name)

________________________________________

Step 4: Push the Code to a Public Git Repository

4.1 Initialize a Git Repository

     git init

4.2 Add Files and Commit

     git add .

     git commit -m "Initial commit: SimpleTimeService microservice"

4.3 Create a Remote Repository

Create a new repository on GitHub,

4.4 Push the Code

     git remote add origin <repository-url>

     git branch -M main

     git push -u origin main



==================================================================================


How to use

==================================================================================

Step 1: Clone the Repository

Run the following command to clone the repository:

     git clone https://github.com/yashasgit/Particle41-DevOps-Team-Challenge.git
     
     cd Particle41-DevOps-Team-Challenge
     
     cd app


Step 2:  Install Python3, Docker, Flask

First, install Python and docker on your system. Then, install Flask using pip:

     sudo apt install python3-pip -y

     sudo apt  install docker.io -y

     sudo apt install python3-flask -y

Step 3:   Add Your User to the docker Group 

To avoid using sudo for Docker commands, add your user to the docker group:

1.	Add your user to the docker group:
   
          sudo usermod -aG docker $USER

2.	Log out and log back in, or refresh your session:
   
          newgrp docker

3.	Verify that you can run Docker commands without sudo:

          docker ps

Step 4:   Pull the Docker Image

Run the following command to pull the image:

     docker pull yashasdocker/simple-time-service:latest

Step 5: Upgrade all installed packages on your Ubuntu system to their latest versions.

     sudo apt-get upgrade -y

Step 6: Build a Docker image from a Dockerfile in the current directory (.)

     docker build -t simple-time-service .

Step 6: Run a Docker container from the image 

     docker run -p 8080:8080 yashasdocker/simple-time-service

Step 6: Test the service

     http://localhost:8080 







