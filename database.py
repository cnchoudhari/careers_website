from sqlalchemy import create_engine, text
import os

connection_string = os.environ['CONNECTION_STRING']
engine = create_engine(connection_string, echo=True)


def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs
