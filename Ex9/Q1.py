from urllib.parse import urlparse
from urllib.request import urlopen
import sqlalchemy
import xmltodict
from datetime import datetime
from sqlalchemy.orm import declarative_base
engine = sqlalchemy.create_engine("sqlite:///my_database.db", echo=True)   

Base = declarative_base()

# Define the "KNS_KnessetDates" table:
class KNS_KnessetDates(Base):
    __tablename__ = 'KNS_KnessetDates'    
    # Define the columns in the user table:
    KnessetDateID = sqlalchemy.Column(sqlalchemy.Integer , primary_key= True)
    KnessetNum = sqlalchemy.Column(sqlalchemy.Integer , unique=False, nullable = False)
    Name = sqlalchemy.Column(sqlalchemy.String(50) , unique=False, nullable = False)
    Assembly = sqlalchemy.Column(sqlalchemy.Integer , unique=False, nullable = False)
    Plenum = sqlalchemy.Column(sqlalchemy.Integer, unique=False, nullable = False)
    PlenumStart = sqlalchemy.Column(sqlalchemy.DateTime , unique=False, nullable = False)
    PlenumFinish = sqlalchemy.Column(sqlalchemy.DateTime , unique=False, nullable = False)
    IsCurrent = sqlalchemy.Column(sqlalchemy.Boolean , unique=False, nullable = False)
    LastUpdatedDate = sqlalchemy.Column(sqlalchemy.DateTime , unique=False, nullable = False)

    def __repr__(self):
        return f'KNS_KnessetDates({self.KnessetDateID!r}, {self.KnessetNum!r}, {self.Name!r}, {self.Assembly!r}, {self.Plenum!r}, {self.PlenumStart!r}, {self.PlenumFinish!r}, {self.IsCurrent!r}, {self.LastUpdatedDate!r}, )'




#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":
    """
    example - get an xml file of "KNS_KnessetDates" from ("https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_KnessetDates()?")
    and print first 10 from the table
    """

    Base.metadata.create_all(engine)  # Create the database and all tables.

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    file =  urlopen("https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_KnessetDates()?")
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    data = data["feed"]["entry"]
    count_i = 0
    for i in data:
        d=i["content"]["m:properties"]
        count_i+=1
        KnessetDateID = int(d["d:KnessetDateID"]["#text"])
        KnessetNum = int(d["d:KnessetNum"]["#text"])
        Name = d["d:Name"]
        Assembly = int(d["d:Assembly"]["#text"])
        Plenum = int(d["d:Plenum"]["#text"])
        PlenumStart = datetime.strptime(d["d:PlenumStart"]["#text"][:10], '%Y-%m-%d')
        PlenumFinish = datetime.strptime(d["d:PlenumFinish"]["#text"][:10], '%Y-%m-%d')
        IsCurrent = bool(str(d["d:IsCurrent"]["#text"])=="true")
        LastUpdatedDate = datetime.strptime(d["d:LastUpdatedDate"]["#text"][:10], '%Y-%m-%d')


        KNS_kd = KNS_KnessetDates( KnessetNum=KnessetNum, Name=Name, Assembly=Assembly, Plenum=Plenum, PlenumStart=PlenumStart, PlenumFinish=PlenumFinish, IsCurrent=IsCurrent, LastUpdatedDate=LastUpdatedDate)
        session.add(KNS_kd)
    
    session.commit()
    it = session.query(KNS_KnessetDates)[:10]
    print("-------------------------------")
    print()
    print("10 first data from the table:")
    print()
    for i in it:
        print(i)

    
    