from sqlalchemy import create_engine, text

connection_string = "mysql+mysqlconnector://9gpfwx0bbncomvgv9lu6:pscale_pw_49HbTN1Sgwwxe3zkZt6gQ1VYAQoF2cfrA28Jaq08h73@aws.connect.psdb.cloud/careers_website?charset=utf8mb4"
engine = create_engine(connection_string, echo=True)


def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs
