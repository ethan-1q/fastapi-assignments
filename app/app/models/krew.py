import tortoise
from tortoise import fields


class Krew(tortoise.Model):
    ldap_id = fields.CharField(max_length=128, pk=True)
    profile_image = fields.CharField(max_length=128, null=True)
    identityDisplayName = fields.CharField(max_length=128, null=True)
    deptName = fields.CharField(max_length=32, null=True)
    deptCode = fields.CharField(max_length=32, null=True)
    deptMainYn = fields.CharField(max_length=32, null=True)
    displayName = fields.CharField(max_length=32, null=True)
    personName = fields.CharField(max_length=32, null=True)
    emailId = fields.CharField(max_length=128, null=True)
    deptPathCode = fields.CharField(max_length=128, null=True)
    deptPathName = fields.CharField(max_length=128, null=True)
    parentDeptCode = fields.CharField(max_length=32, null=True)
    parentDeptName = fields.CharField(max_length=32, null=True)
    companyCodeAccount = fields.CharField(max_length=32, null=True)
    concurrentOffice = fields.JSONField(null=True)
    employeeNo = fields.CharField(max_length=32, null=True)
    gradeName = fields.CharField(max_length=32, null=True)
    gradeLevel = fields.SmallIntField(null=True)

    class Meta:
        app = "krew"
