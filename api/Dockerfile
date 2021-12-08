FROM python:3.10
RUN mkdir api
COPY ./requirements.txt /api/
RUN pip install -r /api/requirements.txt
WORKDIR /api/scripts/
CMD ["python", "app.py"]
