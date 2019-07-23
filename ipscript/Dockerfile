FROM python:3.7-alpine
COPY ipscript.py /ipscript
COPY requirements.txt /ipscript
RUN virtualenv ipscriptenv
RUN source ipscriptenv/bin/activate
WORKDIR /ipscript
RUN pip install -r requirements.txt
CMD ["python", "./ipscript.py"]
