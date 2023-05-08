from sqlalchemy import create_engine, text

connection_string = "mysql+mysqlconnector://y8pvdxo2u3xt0e64oe73:pscale_pw_7a0JBIH8TlMh4q3QmI5TtTVuqQn0zlTZYGcb1D5SoxN@aws.connect.psdb.cloud/careers_website?charset=utf8mb4"
engine = create_engine(connection_string, echo=True)


def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs
