FROM python:3.7.4

WORKDIR /app

COPY ./ /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]

EXPOSE 8001