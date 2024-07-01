FROM public.ecr.aws/lambda/python:3.9 as lambda

WORKDIR /sharbo-app

COPY . .

RUN pip install requests pandas beautifulsoup4 lxml
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "my_lambda_function.handler" ]