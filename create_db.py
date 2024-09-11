from database import Base, engine

# Create all the tables
Base.metadata.create_all(bind=engine)
