FROM public.ecr.aws/lambda/python:3.9 as lambda

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "app.main.handler" ]