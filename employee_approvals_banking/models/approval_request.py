from odoo import api, fields, models

class ApprovalRequest(models.Model):
    _inherit = "approval.request"

    has_bank_account = fields.Selection(related="category_id.has_bank_account")
    # bank_account = fields.Many2one(string="Bank Info", comodel_name="res.partner.bank")

    # Bank account fields
    acc_number = fields.Char('Account Number', required=True)
    partner_id = fields.Many2one('res.partner', 'Account Holder', ondelete='cascade', index=True, domain=['|', ('is_company', '=', True), ('parent_id', '=', False)], required=True)
    acc_holder_name = fields.Char(string='Account Holder Name', help="Account holder name, in case it is different than the name of the Account Holder")
    allow_out_payment = fields.Boolean('Send Money', help='This account can be used for outgoing payments', default=True, copy=False, readonly=False)

    # Bank fields
    bank_id = fields.Many2one(comodel_name='res.bank', string='Bank')
    b_name = fields.Char(string="Name", required=True)
    bic = fields.Char('Bank Identifier Code', index=True, help="Sometimes called BIC or Swift.")
    street = fields.Char()
    street2 = fields.Char(string="Street 2")
    zip = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=?', country)]")
    country = fields.Many2one('res.country')
    email = fields.Char()
    phone = fields.Char()


    def action_approve(self, approver=None):
        super().action_approve(approver)
        employee_id = self.env["hr.employee"].search([("user_id.id", "=", self.request_owner_id.id)])
        new_bank = self.env["res.bank"].create({
            "name": self.b_name,
            "street": self.street,
            "street2": self.street2,
            "zip": self.zip,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "email": self.email,
            "phone": self.phone
        })
        new_bank_account = self.env['res.partner.bank'].create({
            "acc_number": self.acc_number,
            "partner_id": self.partner_id,
            "acc_holder_name": self.acc_holder_name,
            "allow_out_payment": self.allow_out_payment,
            "bank_id": new_bank
        })

        employee_id.bank_account_id = new_bank_account
