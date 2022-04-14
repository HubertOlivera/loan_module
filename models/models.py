from odoo import models, fields, api,_
import datetime
from datetime import date, timedelta

class Head(models.Model):
    _name = 'loan_module.head_loan'
    _description = 'Head'

    description = fields.Char(compute='_nuevadescripcion',string='Descripcion')
    partner_id = fields.Many2one(string='Usuario', required=True, comodel_name='res.partner')
    date=fields.Date(string='Fecha', required=True,default=fields.Date.context_today)
    fees=fields.Integer(string='N° cuotas')
    amount_total=fields.Float(string='Monto total')
    payment_date=fields.Date(string='Fecha por cada cuota')
    amount=fields.Float(string='Monto a pagar por cada cuota')
    #line_ids = fields.One2many(string='Lines', required=True, comodel_name='loan_module.head_loan')
    @api.depends('partner_id.name', 'date')
    def _nuevadescripcion(self):
        for test in self:
            test.description = "Prestamo de "+test.partner_id.name + ' en la fecha '+str(test.date)   
    #@api.model_create_multi
    #def create(self, vals_list):
        #records=super(Head, self).create(vals_list)
        #return records
    #@api.depends('loan_module.line_loan.payment_date','loan_module.line_loan.amount','fees','amount_total')
    #def create_line_loan(self):
        #for record in self:
            #record.loan_module.line_loan.amount=record.amount_total / float(record.fees)
        #print(record.line_ids.amount)

      

    
