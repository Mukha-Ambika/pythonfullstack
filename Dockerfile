FROM public.ecr.aws/lambda/python:3.9 as lambda

RUN pip install requests pandas beautifulsoup4 lxml
RUN pip install --no-cache-dir -r requirements.txt

COPY my_lambda_function.py ./

CMD ["my_lambda_function.lambda_handler"]