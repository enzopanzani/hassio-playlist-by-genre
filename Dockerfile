FROM ghcr.io/home-assistant/amd64-base-debian:bookworm

ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install mutagen && \
    apt-get clean

COPY run.sh /
COPY playlist_by_genre.py /data/
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
