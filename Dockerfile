FROM jayanta525/python3-chromedriver:111.0

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD src /usr/bin
RUN mkdir /app
WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]