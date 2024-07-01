FROM public.ecr.aws/lambda/python:3.9 as lambda

COPY requirements.txt .

RUN pip install requests pandas beautifulsoup4 lxml
RUN pip install --no-cache-dir -r requirements.txt

COPY ./* ./sharbo-app/

CMD [ "my_lambda_function.lambda_handler" ]