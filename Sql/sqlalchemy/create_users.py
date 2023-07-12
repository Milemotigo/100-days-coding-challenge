from main import User, Session, engine




users_data = [
    {
        "username":"jerry",
        "email":"jerry@company.com"
    },
    {
        "username":"Kate",
        "email":"Kate@company.com"
    },
    {
        "username":"Prec",
        "email":"PREC@company.com"
    },
    {
        "username":"TRICHA",
        "email":"TRICHA@company.com"
    },
]

Local_session = Session(bind=engine)

for k in users_data:
    users = User(username=k["username"], email=k["email"])
# add the user to the session so that we will be fully to commit our changes to the database

#Local_session.add(users_data)

#Local_session.commit()
print(users)