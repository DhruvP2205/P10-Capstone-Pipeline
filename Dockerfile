FROM python:3.12 AS Builder

WORKDIR /Build

COPY . .


FROM python:3.12-slim

WORKDIR /src

COPY --from=builder /Build /usr/local

RUN useradd -r -s /sbin/nologin appuser

COPY . .

RUN chown -R appuser /src

USER appuser

EXPOSE 8000

ENTRYPOINT ["python", "/src/app.py"]