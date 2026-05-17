FROM python:3.11-slim

WORKDIR /app

COPY Solutions/ ./Solutions/

CMD ["/bin/bash"]
