from database import engine

try:
    with engine.connect() as connection:
        print(" DB connected successfull")
except Exception as e:
    print("Not connected",e)
    

