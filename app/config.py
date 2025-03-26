class Config:
    SECRET_KEY = 'e7f470ef9fd9894a951dfa78d9dfc75955105bbfa49863bf66088d91b4b43ff9'
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@gcetconnect_app_db:5432/gcetconnectdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_PROTECTION = 'strong'
    
    
    
