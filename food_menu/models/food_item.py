# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class FoodMenu(models.Model):
    _name = 'food_menu'

    meal = fields.Selection(
        [('Breakfast', 'Bữa Sáng'), ('Lunch', 'Bữa Trưa'),
         ('Dinner', 'Bữa Tối')],
        string='Bữa ăn')
    ageGroup = fields.Many2one('age_group', string='Nhóm tuổi')
    dish = fields.Many2one('dish', string = 'Món ăn')
    serving = fields.Char(string='Khẩu phần')


# class FoodItem(models.Model):
#     _name = 'food_item'

#     dishName = fields.Many2one('dish', string='Món ăn')


class AgeGroup(models.Model):
    _name = 'age_group'

    name = fields.Char(compute = '_compute_age',string = 'Nhóm tuổi')
    ageFrom = fields.Integer(string='Từ')
    ageTo = fields.Integer(string = 'Đến')
    
    @api.multi
    @api.depends('ageFrom','ageTo')
    def _compute_age(self): 
        for request in self:
            request.name = "Từ {0} đến {1}".format(int(request.ageFrom), int(request.ageTo))


class Dish(models.Model):
    _name = 'dish'

    name = fields.Char(string='Tên món ăn')
    description = fields.Char(string='Mô tả món ăn')
    nutritions = fields.Many2one(
        'nutritions_fact', string='Thành phần dinh dưỡng')


class NutritionsFact(models.Model):
    _name = 'nutritions_fact'

    name = fields.Many2one('nutritions_value', string='Chất dinh dưỡng')
    nutritionsValue = fields.Char(string='Thành phần')


class NutritionsValue(models.Model):
    _name = 'nutritions_value'

    name = fields.Char(string='Tên')
    description = fields.Char(string='Mô tả')
