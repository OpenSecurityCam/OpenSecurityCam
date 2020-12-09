from flask import flash
class Flashes:
    def LoginSuccessful():
        return flash("Successfully Logged In", "info")
    
    def AlreadyLoggedIn():
        return flash("Already Logged In")
    
    def NameChanged():
        return flash("Name changed successfully")
    
    def HaventLoggedIn():
        return flash("You haven't logged in yet")
    
    def LoggedOut():
        return flash("You have been logged out!", "info")

    def NotLoggedIn():
        return flash("You are not logged in!")