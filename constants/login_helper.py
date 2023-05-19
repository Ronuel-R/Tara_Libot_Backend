from django.contrib.auth.models import User

class LoginHelper():
    def validate_email_and_password(self, email, password):
        errors = {}
        if not email:
            errors['email'] = ['Email is required.']
        if not password:
            errors['password'] = ['Password is required.']
        if email and not User.objects.filter(email=email).exists():
            errors['email'] = ['Invalid email.']
        if password and email and not LoginHelper.authenticate_user(self,email, password):
            errors['password'] = ['Invalid password.']

        return errors
    
    def authenticate_user(self, email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if not user.check_password(password):
            return None

        return user
