import re
from amkr_studio.settings import MASTER_REGEX
from pydantic import BaseModel, Field, field_validator
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

# Validate name
def validateName(value: str) -> str:
	if not re.match(MASTER_REGEX['name']['regex'], value):
		raise ValueError(MASTER_REGEX['name']['desc'])
	return value

# Validate username
def validateUsername(value: str) -> str:
	if not re.match(MASTER_REGEX['usnm']['regex'], value):
		raise ValueError(MASTER_REGEX['usnm']['desc'])
	return value

# Validate email
def validateEmail(value: str) -> str:
	if not re.match(MASTER_REGEX['emal']['regex'], value):
		raise ValueError(MASTER_REGEX['emal']['desc'])
	return value

# Validate password
def validatePassword(value: str) -> str:
	if not re.match(MASTER_REGEX['pswd']['regex'], value):
		raise ValueError(MASTER_REGEX['pswd']['desc'])
	return value

# Annotated validation types
AnnotatedName 	  = Annotated[str, AfterValidator(validateName)]
AnnotatedUsername = Annotated[str, AfterValidator(validateUsername)]
AnnotatedEmail 	  = Annotated[str, AfterValidator(validateEmail)]
AnnotatedPassword = Annotated[str, AfterValidator(validatePassword)]

class UserLoginValidator(BaseModel):
	''' This model is used to validate request for UserLogin API '''
	username: AnnotatedUsername = Field(..., description='The user\'s username')
	password: AnnotatedPassword = Field(..., description='The user\'s password')

class RegisterUserValidator(BaseModel):
	''' This model is used to validate request for RegisterUser API '''
	firstName: AnnotatedName 	= Field(..., description='The user\'s first name')
	lastName: AnnotatedName 	= Field(..., description='The user\'s last name')
	username: AnnotatedUsername = Field(..., description='The username for the user')
	email: AnnotatedEmail 		= Field(..., description='The email address of the user')
	password: AnnotatedPassword = Field(..., description='The user\'s password')
	userId: int 				= Field(..., description='The user ID of the creator of this user account')
