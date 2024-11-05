# -*- coding: utf-8 -*-
from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class XpatWorkTypes(models.Model):
    _name = "visa.fees"
    _description = "Xpat work types"

    @api.model
    def default_get(self, fields):
        res = super(XpatWorkTypes, self).default_get(fields)
        if (self.env.context.get('active_id')):
            regId = self.env.context.get('active_id')

            result = self.env['hr.applicant'].browse(regId)

            # res['visa_app_id'] = regId
            res['name'] = result.partner_name
            res['wp_expiry'] = result.wp_expiry


            return res

    name = fields.Char(string="Name", required=True)
    date_paid = fields.Date(string="Paid Date", default=lambda self: fields.Datetime.now())
    wp_expiry = fields.Date(string="WP Expiry")
    paid_until = fields.Date(string="Paid Until")
    description = fields.Char(string="Description")
    rate = fields.Float(string="Rate", default=350)
    months = fields.Integer(string="Months", default=3)
    amount = fields.Float(string="Amount")
    visa_app_id = fields.Many2one('hr.applicant', string="Visa Application")
    state = fields.Selection([
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ],
        string='State',
        default='paid')

    @api.onchange('rate', 'months')
    def onchange_months(self):
        if (self.visa_app_id):
            self.amount = self.rate * self.months
            self.description = self.description = "Visa fee paid for " + str(self.months) + " with total amount of " + str(self.amount)
            # Convert string date value to datetime object
            if(self.wp_expiry):
                current_date = fields.Datetime.from_string(self.wp_expiry)
                # Increment the added_date by given months
                self.paid_until = current_date + relativedelta(months=self.months)




    @api.model_create_multi
    def create(self, vals_list):
        active_id = self.env.context.get('active_id')
        paid_until = ""

        for val in vals_list:
            paid_until = val['paid_until']

        vals1 = {
            'wp_expiry': paid_until,
        }
        self.env['hr.applicant'].browse(active_id).write(vals1)

        return super().create(vals_list)



class XpatWorkSlotFees(models.Model):
    _name = "slot.fees"
    _description = "Xpat work types"

    @api.model
    def default_get(self, fields):
        res = super(XpatWorkSlotFees, self).default_get(fields)
        if (self.env.context.get('active_id')):
            regId = self.env.context.get('active_id')

            result = self.env['hr.applicant'].browse(regId)

            res['slot_app_id'] = regId
            res['name'] = result.partner_name
            res['slot_expiry'] = result.slot_expiry

            return res


    name = fields.Char(string="Name", required=True)
    date_paid = fields.Date(string="Paid Date", default=lambda self: fields.Datetime.now())
    slot_expiry = fields.Date(string="Slot Expiry")
    paid_until = fields.Date(string="Paid Until")
    description = fields.Char(string="Description")
    rate = fields.Float(string="Rate", default=167.66)
    months = fields.Integer(string="Months", default=3)
    amount = fields.Float(string="Amount")
    slot_app_id = fields.Many2one('hr.applicant', string="Slot Application")
    state = fields.Selection([
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ],
        string='State',
        default='paid')

    @api.onchange('rate', 'months')
    def onchange_months(self):
        if (self.slot_app_id):
            self.amount = self.rate * self.months
            self.description = self.description = "Slot fee paid for " + str(
                self.months) + " with total amount of " + str(self.amount)
            # Convert string date value to datetime object
            if (self.slot_expiry):
                current_date = fields.Datetime.from_string(self.slot_expiry)
                # Increment the added_date by given months
                self.paid_until = current_date + relativedelta(months=self.months)

    @api.model_create_multi
    def create(self, vals_list):
        active_id = self.env.context.get('active_id')
        paid_until = ""

        for val in vals_list:
            paid_until = val['paid_until']

        vals1 = {
            'slot_expiry': paid_until,
        }
        self.env['hr.applicant'].browse(active_id).write(vals1)

        return super().create(vals_list)




class VisaFeeInheritApplicant(models.Model):
    _inherit = 'hr.applicant'

    visa_app_ids = fields.One2many('visa.fees', 'visa_app_id', string="Visa Fees")
    slot_app_ids = fields.One2many('slot.fees', 'slot_app_id', string="Slot Fees")


    def pay_visa_fee(self):
        print("visa fee click")

