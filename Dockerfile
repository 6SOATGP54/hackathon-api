FROM public.ecr.aws/lambda/python:3.13
LABEL maintainer="https://github.com/6SOATGP54"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH="/app"

# Comando padrão da AWS Lambda para rodar um handler
CMD ["vapi.routes.lambda_handler"]