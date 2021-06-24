from fastapi import HTTPException
from fastapi import status


class BadRequest(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST)


class NotFoundKrew(HTTPException):
    def __init__(self, ldap_id):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Krew(ldap_id={ldap_id}) is not exists.")
