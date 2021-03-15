FROM python

WORKDIR /app

ENV FLASK_APP = api.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4200

CMD ["python", "api.py"]
