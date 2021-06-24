import tortoise
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Member(tortoise.Model):
    id = fields.BigIntField(pk=True)
    kakao_email = fields.CharField(max_length=128, null=True)
    name = fields.CharField(max_length=32, null=True)
    phone_number = fields.CharField(max_length=24, null=True)
    created_at = fields.DatetimeField()
    modified_at = fields.DatetimeField()
    kakao_account_id = fields.BigIntField()
    dsp_account_id = fields.BigIntField()
    kakao_account = fields.CharField(max_length=128, null=True)
    email = fields.CharField(max_length=128, null=True)
    marketing = fields.SmallIntField(null=True)
    publicity = fields.SmallIntField(null=True)
    activated_at = fields.DatetimeField(null=True)
    deleted_at = fields.DatetimeField(null=True)
    dormant_at = fields.DatetimeField(null=True)
    state = fields.SmallIntField()

    class Meta:
        app = "member"
        table = "members"

    pydantic_schema = None

    @classmethod
    def get_pydantic(cls):
        if cls.pydantic_schema is None:
            cls.pydantic_schema = pydantic_model_creator(Member, name="Member")
        return cls.pydantic_schema
