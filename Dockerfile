FROM public.ecr.aws/lambda/python:3.9 as lambda

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# COPY ./* ./sharbo_app/

COPY app /app
WORKDIR /app

# COPY my_lambda_function.py ./

CMD [ "my_lambda_function.handler" ]