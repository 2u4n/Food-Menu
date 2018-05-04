# # -*- coding: utf-8 -*-
# from odoo import models, fields, api
# import logging

# _logger = logging.getLogger(__name__)


# class FoodMenu(models.Model):
#     _name = 'food_menu'

#     meal = fields.Selection(
#         [('Breakfast', 'Bữa Sáng'), ('Lunch', 'Bữa Trưa'),
#          ('Dinner', 'Bữa Tối')],
#         string='Bữa ăn')
#     ageGroup = fields.Many2one('age_group', string='Nhóm tuổi')
#     dish = fields.Many2one('food_item', string = 'Món ăn')
#     serving = fields.Char(string='Khẩu phần')
