import random
from typing import List, Optional
import databases
import sqlalchemy
from fastapi import FastAPI, Body
from pydantic import BaseModel
from sqlalchemy import select, ForeignKey
from sqlalchemy.sql.functions import count
from starlette.responses import JSONResponse

DATABASE_URL = "sqlite:///./jobdatabases.db"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
Job_Table = sqlalchemy.Table(
    'Job_Table', metadata,
    sqlalchemy.Column('job_id', sqlalchemy.String, primary_key=True),
    sqlalchemy.Column('job_name', sqlalchemy.String),
    sqlalchemy.Column('location', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('skills', sqlalchemy.String),
)
Job_Application = sqlalchemy.Table(
    'Job_Application', metadata,
    sqlalchemy.Column('first_name', sqlalchemy.String),
    sqlalchemy.Column('last_name', sqlalchemy.String),
    sqlalchemy.Column('job_id', sqlalchemy.String, ForeignKey('Job_Table.job_id')),
    sqlalchemy.Column('email_id', sqlalchemy.String),
    sqlalchemy.Column('it_skills', sqlalchemy.String),
    sqlalchemy.Column('qualification', sqlalchemy.String),
    sqlalchemy.Column('yearofexp', sqlalchemy.String)
)
Candidate_Table = sqlalchemy.Table(
    'Candidate_Table', metadata,
    sqlalchemy.Column('job_id', sqlalchemy.String, ForeignKey('Job_Application.job_id')),
    sqlalchemy.Column('first_name', sqlalchemy.String),
    sqlalchemy.Column('email_id', sqlalchemy.String),
    sqlalchemy.Column('it_skills', sqlalchemy.String),
    sqlalchemy.Column('qualification', sqlalchemy.String),
    sqlalchemy.Column('yearofexp', sqlalchemy.String),
)
class Delete(BaseModel):
    job_id: str
class CandidateAll(BaseModel):
    job_id: str
    first_name: str
    email_id: str
    it_skills: str
    qualification: str
    yearofexp: str
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class all(BaseModel):
    job_id: str
    job_name: str
    location: str
    discription: str
    skills: str
class ApplicantAll(BaseModel):
    job_id: str
    first_name: str
    last_name: str
    email_id: str
    it_skills: str
    qualification: str
    yearofexp: str
class DeleteApplicant(BaseModel):
    first_name: str
    last_name: str

@app.get("/")
async def home():
    return JSONResponse(content={"message": "Hello"})

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/select/")
async def read_records():
    query = Job_Table.select()
    return await database.fetch_all(query)
random_number = random.randint(10000, 99999)
@app.post("/insert", response_model=all)
async def insert_record(job_name:str, location:str, description:str, skills:str):
    # Check the record is already exist or not
    query1 = select([count(1)]).where((Job_Table.c.job_id == random_number))
    val = await database.fetch_one(query1)
    if val == (0,):
        query = Job_Table.insert().values(job_id=random_number, job_name=job_name, location=location,
                                          description=description, skills=skills)
        last_record_id = await database.execute(query)
        result = JSONResponse(content={"message": "Record inserted"})
    else:
        result = JSONResponse(content={"message": "record already exists"})
    return result

async def getting(job_id):
    global jobna,loca,desc,skil
    query = Job_Table.select().where(Job_Table.c.job_id == job_id)
    val = await database.fetch_one(query)
    jobna=val[1]
    loca=val[2]
    desc=val[3]
    skil=val[4]
@app.put("/update/", response_model=all)
async def update_record(job_id:str, job_name:Optional[str]=None, location:Optional[str]=None, description:Optional[str]=None,
                        skills:Optional[str]=None,):
    global result
    query1 = select([count(1)]).where((Job_Table.c.job_id == job_id))
    val = await database.fetch_one(query1)
    if val == (0,):
        result = JSONResponse(status_code=200, content={"message": "jod id not found"})
    elif val == (1,):
        await getting(job_id)
        jobnameval = jobna
        locavar = loca
        descvar = desc
        skillvar = skil
        if job_name ==None:
            job_name=jobnameval
        if location==None:
            location=locavar
        if description==None:
            description=descvar
        if skills==None:
            skills=skillvar
        query = Job_Table.update().where(Job_Table.c.job_id == job_id).values(job_name=job_name,
                                                                                  location=location,
                                                                                  description=description,
                                                                                  skills=skills)
        record = await database.execute(query)
        result = JSONResponse(content={"message": "updated"})
    else:
        result = JSONResponse(content={"message": "error"})
    return result


@app.delete("/delete/", response_model=Delete)
async def delete_record(job_id_var:str):
    # check the job_id is exist or not
    query1 = select([count(1)]).where((Job_Table.c.job_id == job_id_var))
    val = await database.fetch_one(query1)

    if val == (0,):
        result = JSONResponse(content={"message": "jod id not found"})
    elif val == (1,):
        # Deleting records
        query = Job_Table.delete().where(Job_Table.c.job_id == job_id_var)
        record = await database.execute(query)
        result = JSONResponse(content={"message": "Record deleted"})
    else:
        result = JSONResponse(content={"message": "error"})
    return result

@app.post("/insert applicant records", response_model=ApplicantAll)
async def insert_applicant_records(job_id:str,first_name:str,last_name:str,email_id:str,it_skills:str,qualification:str,yearofexp:str):
    global result
    query1 = select([count(1)]).where((Job_Table.c.job_id == job_id))
    val = await database.fetch_one(query1)
    if val == (0,):
        result = JSONResponse(content={"message": "Invalid Job Id"})
    elif val == (1,):

        query = Job_Application.insert().values(job_id=job_id, first_name=first_name,
                                                 last_name=last_name, email_id=email_id,
                                                 it_skills=it_skills, qualification=qualification,
                                                 yearofexp=yearofexp)
        record = await database.execute(query)
        result=JSONResponse(content={"message": "Record inserted"})
    else:
        result = JSONResponse(content={"message": "Error"})
    return result

@app.get("/select applicant records", response_model=List[ApplicantAll])
async def read_candiate_records():
    query = Job_Application.select()
    return await database.fetch_all(query)


@app.post("/insert candidate records", response_model=CandidateAll)
async def insert_candidate_records(job_id:str,first_name:str,email_id:str,it_skills:str,qualification:str,yearofexp:str):
    global result
    query1 = select([count(1)]).where((Job_Table.c.job_id == job_id))
    val = await database.fetch_one(query1)
    if val == (0,):
        result = JSONResponse(content={"message": "Invalid Job Id"})
    elif val == (1,):
        query2 = Candidate_Table.insert().values(job_id=job_id, first_name=first_name,
                                                  email_id=email_id,
                                                  it_skills=it_skills,
                                                  qualification=qualification,
                                                  yearofexp=yearofexp)
        record1 = await database.execute(query2)
        result=JSONResponse(content={"message": "Record inserted"})
    else:
        result = JSONResponse(content={"message": "Error"})
    return result
@app.delete("/delete applicant records", response_model=DeleteApplicant)
async def delete_applicant_record(first_name:str,last_name:str):
    query1 = select([count(1)]).where(
        (Job_Application.c.first_name == first_name and Job_Application.c.last_name == last_name))
    val = await database.fetch_one(query1)
    if val == (0,):
        result = JSONResponse(status_code=200, content={"message": "Record not found"})
    elif val == (1,):
        # Deleting records
        query = Job_Application.delete().where(
            Job_Application.c.first_name == first_name and Job_Application.c.last_name == last_name)
        record = await database.execute(query)
        result = JSONResponse(content={"message": "Record deleted"})
    else:
        result = JSONResponse(content={"message": "error"})
    return result
