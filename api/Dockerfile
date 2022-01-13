FROM python:3.9
RUN mkdir api
COPY ./requirements.txt /api/
RUN pip install --no-cache-dir -r /api/requirements.txt
WORKDIR /api/scripts/
CMD ["python", "app.py"]
