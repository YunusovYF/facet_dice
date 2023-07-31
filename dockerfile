FROM python

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src
COPY ./alembic.ini /app
COPY ./migrations /app/migrations

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug" , "--use-colors"]