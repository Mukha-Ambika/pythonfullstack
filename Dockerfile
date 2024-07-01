FROM public.ecr.aws/lambda/python:3.9 as lambda

COPY ./* ./sharbo-app/

RUN pip install requests pandas beautifulsoup4 lxml
RUN pip install --no-cache-dir -r requirements.txt

CMD ["app.my_lambda_function.lambda_handler"]