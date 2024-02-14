from datetime import date,datetime
def caldays():
    start_date = datetime.strftime("2022-01-01","%Y-%m-%d")
    end_date = datetime.strftime("2022-12-31","%Y-%m-%d")

    num_days = (end_date-start_date).days
    print(num_days)