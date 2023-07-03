import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerProject.settings')

import django
django.setup()

from jobsInfo.models import *
from faker import Faker
from random import randint

fake = Faker()

def phoneNumberGen():
    d1 = randint(6, 9)
    num = "" + str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.random_element(elements=('TCS', 'WIPRO', 'INFOSYS', 'CAPGEMINI', 'INFOBEANS'))
        feligibility = fake.random_element(elements=('B.tech', 'M.Tech', 'MCA', 'Phd'))
        ftitle = fake.random_element(elements=('Sr.Software Engineer', 'Jr.Software Engineer', 'Team Lead', 'Project Manager', 'Data Analysis'))
        faddress = fake.address()
        femail = fake.email()
        fPhoneNumber = phoneNumberGen()
        hyd_records = hydJobs.objects.get_or_create(date=fdate, company=fcompany, eligibility=feligibility,
                                                   title=ftitle, address=faddress, email=femail,
                                                   PhoneNumber=fPhoneNumber)

populate(0)

def populateOne(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.random_element(elements=('TCS', 'WIPRO', 'INFOSYS', 'CAPGEMINI', 'INFOBEANS'))
        feligibility = fake.random_element(elements=('B.tech', 'M.Tech', 'MCA', 'Phd'))
        ftitle = fake.random_element(elements=('Sr.Software Engineer', 'Jr.Software Engineer', 'Team Lead', 'Project Manager', 'Data Analysis'))
        faddress = fake.address()
        femail = fake.email()
        fPhoneNumber = phoneNumberGen()
        bag_records = BengaluruJobs.objects.get_or_create(date=fdate, company=fcompany, eligibility=feligibility,
                                                   title=ftitle, address=faddress, email=femail,
                                                   PhoneNumber=fPhoneNumber)

populateOne(0)


def populateTwo(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.random_element(elements=('TCS', 'WIPRO', 'INFOSYS', 'CAPGEMINI', 'INFOBEANS'))
        feligibility = fake.random_element(elements=('B.tech', 'M.Tech', 'MCA', 'Phd'))
        ftitle = fake.random_element(elements=('Sr.Software Engineer', 'Jr.Software Engineer', 'Team Lead', 'Project Manager', 'Data Analysis'))
        faddress = fake.address()
        femail = fake.email()
        fPhoneNumber = phoneNumberGen()
        bag_records = PuneJobs.objects.get_or_create(date=fdate, company=fcompany, eligibility=feligibility,
                                                   title=ftitle, address=faddress, email=femail,
                                                   PhoneNumber=fPhoneNumber)

populateTwo(30)