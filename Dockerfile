# FROM python:3.12-slim
FROM python

RUN useradd -r -s /sbin/nologin appuser

WORKDIR /src

COPY --chown=appuser app.py .

USER appuser

EXPOSE 8000

ENTRYPOINT ["python", "/src/app.py"]