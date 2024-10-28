FROM python:3.12

WORKDIR /usr/src/app

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/bash", "-c", "python bot.py"]