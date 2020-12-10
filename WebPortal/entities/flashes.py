from flask import flash
class Flashes:
    def LoginSuccessful():
        return flash("Successfully Logged In", "info")
    
    def AlreadyLoggedIn():
        return flash("Already Logged In")
    
    def HaventLoggedIn():
        return flash("You haven't logged in yet")
    
    def NotLoggedIn():
        return flash("You are not logged in!")

    def LoggedOut():
        return flash("You have been logged out!", "info")
    
    def NameChanged():
        return flash("Name changed successfully")
    
    def PassNotMatch():
        return flash("Passwords don't match")
    
    def WrongPasscode():
        return flash("Wrong Passcode")
    
    def CredentialChanged():
        return flash("Credentials Changed")
    
    def InvalidOperation():
        return flash("Invalid Operation")