ARG BASE_IMAGE=messager_base_image
ARG BASE_IMAGE_TAG=latest

FROM $BASE_IMAGE:$BASE_IMAGE_TAG

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--debug", "--host", "0.0.0.0", "--port", "80"]
