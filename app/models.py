from peewee import *
import os

# Create a database
from app.loadConfig import *
here = os.path.dirname(__file__)
cfg       = load_config(os.path.join(here, 'config.yaml'))
mainDB    = SqliteDatabase(cfg['databases']['dev'])

# Creates the class that will be used by Peewee to store the database
class dbModel (Model):
  class Meta:
    database = mainDB

"""
When adding new tables to the DB, add a new class here
Also, you must add the table to the config.yaml file

Example of creating a Table

class tableName (dbModel):
  column1       = PrimaryKeyField()
  column2       = TextField()
  column3       = IntegerField()

For more information look at peewee documentation
"""

class Bill(dbModel):
    bID                 = PrimaryKeyField()
    title               = TextField()
    display_num         = TextField()
    bill_type           = TextField()
    bill_type_label     = TextField()
    congress            = TextField()
    current_status      = TextField()
    current_status_date = TextField()
    link_web            = TextField()
    is_alive            = TextField()

class Salience(dbModel):
    pID                 = PrimaryKeyField()
    ID                  = ForeignKeyField(Bill)
    summary             = BooleanKeyField()
    name                = TextField()
    score               = FloatField()
    type                = TextFied()
    section             = IntegerField()
