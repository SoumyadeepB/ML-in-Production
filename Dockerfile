#Base Image
FROM python:3.7.3-stretch
#Create working directory
RUN mkdir /app
#Switch to working directory
WORKDIR /app
#Copy all files
COPY . .
#Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#Run
CMD ["python","upload.py"]