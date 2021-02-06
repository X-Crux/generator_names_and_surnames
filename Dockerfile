FROM python:3.9.1

WORKDIR /usr/src/gen_names

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/gen_names

CMD ["python", "main.py"]
