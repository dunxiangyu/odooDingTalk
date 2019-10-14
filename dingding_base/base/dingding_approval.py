# -*- coding: utf-8 -*-
import logging
from odoo import models, api
from odoo.exceptions import ValidationError
from odoo.fields import Datetime

_logger = logging.getLogger(__name__)


def _commit_dingding_approval(self):
    """
    钉钉审批
    :param self:
    :return:
    """
    raise ValidationError("当前版本不支持，请购买专业版模块！")


Model = models.Model
setattr(Model, 'commit_dingding_approval', _commit_dingding_approval)
