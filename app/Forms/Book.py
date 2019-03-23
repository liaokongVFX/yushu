# -*- coding: utf-8 -*-
# Time    : 2019/3/23 11:01
# Author  : LiaoKong

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    q = StringField(validators=[DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
