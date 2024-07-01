# Use AWS Lambda Python base image for Lambda deployment
FROM public.ecr.aws/lambda/python:3.9 as lambda

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Lambda function handler
CMD ["app.main.handler"]
