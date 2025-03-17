import pandas as pd
from core.models import Customer, Loan

def run():
    df = pd.read_excel("assignment files/customer_data.xlsx")
    