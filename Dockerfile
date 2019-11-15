# Specify a base imgae
FROM python:3.7-slim
LABEL maintainer="mrzeznic"
LABEL version="v0.1"

WORKDIR /usr/app

COPY requirements.txt .

#Install some dependencies
RUN pip install -U --no-cache-dir -r requirements.txt

COPY . .

#Default command
CMD ["python", "take_class.py"]