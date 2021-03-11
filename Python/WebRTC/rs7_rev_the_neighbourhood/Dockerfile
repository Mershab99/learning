FROM python:3.9
ENV PYTHONBUFFERED=1

RUN pip install aiortc aiohttp

RUN mkdir /code
ADD . /code/
WORKDIR /code/


EXPOSE 8080

ENTRYPOINT []
CMD ["python" , "./server.py"]
