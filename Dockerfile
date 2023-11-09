FROM python:3.11.6

EXPOSE 8501

WORKDIR /app

CMD python -m venv env
CMD env/Scripts/activate

COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

RUN mkdir -p /app/helpers
COPY helpers/ /app/helpers/

COPY main.py .

CMD streamlit run main.py