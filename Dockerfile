FROM python:3.7

ADD blinds.py /

RUN pip3 install web.py==0.51
RUN pip3 install bluepy
COPY soma3.py /soma3.py



CMD [ "python3", "blinds.py" ]