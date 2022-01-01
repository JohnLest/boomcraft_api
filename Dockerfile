FROM python:3.9
WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY ./api/ /
RUN ls -la /
CMD ["uvicorn", "startup:app", "--host", "0.0.0.0", "--port", "8000"]

