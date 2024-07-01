FROM public.ecr.aws/lambda/python:3.9 as lambda

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install requests pandas beautifulsoup4 lxml
RUN pip install --no-cache-dir -r requirements.txt

CMD ["my_lambda_function.lambda_handler"]