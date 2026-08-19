import uuid
from allauth.account.adapter import DefaultAccountAdapter


# Generate defualt username 
class AccountAdapter(DefaultAccountAdapter):

     def populate_user(self, request, sociallogin, data):
        print(data)
        user = super().populate_user(request, sociallogin, data)
        if not user.username:
            user.username = f"user_{uuid.uuid4().hex[:10]}"
        return user