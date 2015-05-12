# -*- coding: utf-8 -*-
from openerp import models, fields

class author(models.Model):
    _name = 'mylibrary3.author'
    _rec_name = 'lastname'
    firstname = fields.Char('FirstName', required=True)
    lastname = fields.Char('LastName', required=True) 
    cin = fields.Char('CIN')
    book_ids = fields.One2many('mylibrary3.book','author_id','Books')
    ville_id = fields.Many2one('mylibrary3.ville','ville')
class book(models.Model):
    _name = 'mylibrary3.book'
    title = fields.Char('Title', required=True)
    genre = fields.Char('Genre', required=True)
    code = fields.Char('code', required=True)
    author_id = fields.Many2one('mylibrary3.author','Author',ondelete='cascade')
    
class ville(models.Model):
    _name = 'mylibrary3.ville'
    name= fields.Char('ville', required=True)
    author_id = fields.One2many('mylibrary3.author','ville_id','Authors')
    