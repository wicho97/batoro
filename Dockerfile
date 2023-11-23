# base image  
FROM python:3.10
RUN apt-get update
RUN apt-get install -y \
	build-essential \
	python3-dev \
	python3-pip \
	python3-setuptools \
	python3-wheel \
	python3-cffi \
	libcairo2 \
	libpango-1.0-0 \
	libpangocairo-1.0-0 \
	libgdk-pixbuf2.0-0 \
	libffi-dev \
	shared-mime-info

WORKDIR /app/
COPY . /app/

RUN pip install -r requirements.txt
EXPOSE 8000

ENTRYPOINT ["python", "batoro/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

