from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, INT, NVARCHAR, VARCHAR

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    ID = Column(INT(), primary_key=True)
    FirstName = Column(NVARCHAR(100))
    LastName = Column(NVARCHAR(100))

class Schools(Base):
    __tablename__ = 'Schools'
    ID = Column(INT(), primary_key=True)
    BasicSchoolId = Column(INT())

class BasicSchools(Base):
    __tablename__ = 'BasicSchools'
    ID = Column(INT(), primary_key=True)
    Name = Column(VARCHAR(500))

class Communities(Base):
    __tablename__ = 'Communities'
    ID = Column(INT(), primary_key=True)
    BasicCommunityId = Column(INT())

class BasicCommunities(Base):
    __tablename__ = 'BasicCommunities'
    ID = Column(INT(), primary_key=True)
    Name = Column(VARCHAR(150))

class UserComSchRelations(Base):
    __tablename__ = 'UserComSchRelations'
    ID = Column(INT(), primary_key=True)
    UserId = Column(INT())
    CommunityId = Column(INT())
    SchoolId = Column(INT())

class TRSClasses(Base):
    __tablename__ = 'TRSClasses'
    ID = Column(INT(), primary_key=True)
    SchoolId = Column(INT())

class DatabaseManagement():
    def __init__(self):
        self.engine = create_engine("mssql+pymssql://sa:sunneT2009@192.168.1.7\sql2012/20191219_engage_Qa", echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def query_user_id(self, First_Name, Last_Name):
        result = self.session.query(Users).filter(Users.FirstName == First_Name, Users.LastName == Last_Name).first()
        user_id = result.ID
        return user_id

    def query_basic_school_id(self, School_Name):
        result = self.session.query(BasicSchools).filter(BasicSchools.Name == School_Name).first()
        basic_school_id = result.ID
        return basic_school_id

    def query_school_id(self, Basic_School_Id):
        result = self.session.query(Schools).filter(Schools.BasicSchoolId == Basic_School_Id).first()
        school_id = result.ID
        return school_id

    def delete_user_school_relation(self, User_Id, School_Id):
        self.session.query(UserComSchRelations).filter(UserComSchRelations.UserId == User_Id, UserComSchRelations.SchoolId == School_Id).delete()
        self.session.commit()

    def query_basic_community_id(self, Community_Name):
        result = self.session.query(BasicCommunities).filter(BasicCommunities.Name == Community_Name).first()
        basic_community_id = result.ID
        return basic_community_id

    def query_community_id(self, Basic_Community_Id):
        result = self.session.query(Communities).filter(Communities.BasicCommunityId == Basic_Community_Id).first()
        community_id = result.ID
        return community_id

    def delete_user_community_relation(self, Community_Id, User_Id):
        self.session.query(UserComSchRelations).filter(UserComSchRelations.CommunityId == Community_Id, UserComSchRelations.UserId == User_Id).delete()
        self.session.commit()

    def delete_TRS_Class(self, School_Id):
        self.session.query(TRSClasses).filter(TRSClasses.SchoolId == School_Id).delete()
        self.session.commit()

if __name__ == '__main__':
    db_se = DatabaseManagement()
    db_se.delete_user_school_relation(30325, 5904)
