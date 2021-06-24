from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, EmailStr, Json


class MemberOut(BaseModel):
    id: int
    kakao_email: Optional[EmailStr]
    name: Optional[str]
    phone_number: Optional[str]
    created_at: datetime
    modified_at: datetime
    kakao_account_id: Optional[int]
    dsp_account_id: Optional[int]
    kakao_account: Optional[str]
    email: Optional[str]
    marketing: Optional[int]
    publicity: Optional[int]
    activated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    dormant_at: Optional[datetime]
    state: int


class KrewOut(BaseModel):
    ldap_id: str
    profile_image: Optional[str]
    identityDisplayName: Optional[str]
    deptName: Optional[str]
    deptCode: Optional[str]
    deptMainYn: Optional[str]
    displayName: Optional[str]
    personName: Optional[str]
    emailId: Optional[EmailStr]
    deptPathCode: Optional[str]
    deptPathName: Optional[str]
    parentDeptCode: Optional[str]
    parentDeptName: Optional[str]
    companyCodeAccount: Optional[str]
    # concurrentOffice = Optional[Json]
    employeeNo: Optional[str]
    gradeName: Optional[str]
    gradeLevel: Optional[int]
