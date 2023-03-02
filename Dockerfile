FROM python:3.10

#директория /app - в переменную окружения HOME
ENV HOME /app
#и она будет рабочей директорией, WORKDIR автоматически создаёт директорию в том случае, если она не существует
WORKDIR $HOME

COPY requirements.txt .
RUN python -m pip install --no-cache -r requirements.txt

COPY . .
CMD ["python", "run.py"]
