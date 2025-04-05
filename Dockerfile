FROM python:3.12-alpine

# Install Git (required for pbr versioning)
RUN apk add --no-cache git

# Install necessary dependencies for Bandit
RUN apk add --no-cache build-base

# Set the working directory inside the container
WORKDIR /bandit

# Install Bandit via pip
RUN pip install bandit

# Define entrypoint and default command
ENTRYPOINT ["bandit"]
