# Use AWS Lambda Python base image for Lambda deployment
FROM public.ecr.aws/lambda/python:3.9 as lambda

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first for better caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Command to run the Lambda function handler
CMD ["app.main.handler"]
