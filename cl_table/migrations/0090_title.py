# Generated by Django 3.0.7 on 2020-12-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0089_delete_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=50, null=True)),
                ('comp_title1', models.CharField(blank=True, db_column='Comp_Title1', max_length=50, null=True)),
                ('comp_title2', models.CharField(blank=True, db_column='Comp_Title2', max_length=50, null=True)),
                ('comp_title3', models.CharField(blank=True, db_column='Comp_Title3', max_length=50, null=True)),
                ('comp_title4', models.CharField(blank=True, db_column='Comp_Title4', max_length=50, null=True)),
                ('footer_1', models.CharField(blank=True, db_column='Footer_1', max_length=50, null=True)),
                ('footer_2', models.CharField(blank=True, db_column='Footer_2', max_length=50, null=True)),
                ('footer_3', models.CharField(blank=True, db_column='Footer_3', max_length=50, null=True)),
                ('footer_4', models.CharField(blank=True, db_column='Footer_4', max_length=50, null=True)),
                ('rec_detail', models.IntegerField(blank=True, db_column='REC_DETAIL', null=True)),
                ('rec_qty', models.IntegerField(blank=True, db_column='REC_QTY', null=True)),
                ('rec_price', models.IntegerField(blank=True, db_column='REC_PRICE', null=True)),
                ('rec_amt', models.IntegerField(blank=True, db_column='REC_AMT', null=True)),
                ('rec_title', models.IntegerField(blank=True, db_column='REC_TITLE', null=True)),
                ('rec_maintitle', models.IntegerField(blank=True, db_column='REC_MAINTITLE', null=True)),
                ('rec_print', models.IntegerField(blank=True, db_column='REC_PRINT', null=True)),
                ('coll_title', models.IntegerField(blank=True, db_column='COLL_TITLE', null=True)),
                ('coll_detail', models.IntegerField(blank=True, db_column='COLL_DETAIL', null=True)),
                ('coll_qty', models.IntegerField(blank=True, db_column='COLL_QTY', null=True)),
                ('coll_amt', models.IntegerField(blank=True, db_column='COLL_AMT', null=True)),
                ('coll_maintitle', models.IntegerField(blank=True, db_column='COLL_MAINTITLE', null=True)),
                ('coll_print', models.IntegerField(blank=True, db_column='COLL_PRINT', null=True)),
                ('daily_title', models.IntegerField(blank=True, db_column='DAILY_TITLE', null=True)),
                ('daily_detail', models.IntegerField(blank=True, db_column='DAILY_DETAIL', null=True)),
                ('daily_qty', models.IntegerField(blank=True, db_column='DAILY_QTY', null=True)),
                ('daily_amt', models.IntegerField(blank=True, db_column='DAILY_AMT', null=True)),
                ('daily_maintitle', models.IntegerField(blank=True, db_column='DAILY_MAINTITLE', null=True)),
                ('daily_print', models.IntegerField(blank=True, db_column='DAILY_PRINT', null=True)),
                ('hr_title', models.IntegerField(blank=True, db_column='HR_TITLE', null=True)),
                ('hr_time', models.IntegerField(blank=True, db_column='HR_TIME', null=True)),
                ('hr_qty', models.IntegerField(blank=True, db_column='HR_QTY', null=True)),
                ('hr_amt', models.IntegerField(blank=True, db_column='HR_AMT', null=True)),
                ('hr_maintitle', models.IntegerField(blank=True, db_column='HR_MAINTITLE', null=True)),
                ('hr_print', models.IntegerField(blank=True, db_column='HR_PRINT', null=True)),
                ('not_item', models.IntegerField(blank=True, db_column='NOT_ITEM', null=True)),
                ('not_qty', models.IntegerField(blank=True, db_column='NOT_QTY', null=True)),
                ('not_amt', models.IntegerField(blank=True, db_column='NOT_AMT', null=True)),
                ('not_title', models.IntegerField(blank=True, db_column='NOT_TITLE', null=True)),
                ('not_maintitle', models.IntegerField(blank=True, db_column='NOT_MAINTITLE', null=True)),
                ('not_print', models.IntegerField(blank=True, db_column='NOT_PRINT', null=True)),
                ('pay_title', models.IntegerField(blank=True, db_column='PAY_TITLE', null=True)),
                ('pay_detail', models.IntegerField(blank=True, db_column='PAY_DETAIL', null=True)),
                ('pay_qty', models.IntegerField(blank=True, db_column='PAY_QTY', null=True)),
                ('pay_amt', models.IntegerField(blank=True, db_column='PAY_AMT', null=True)),
                ('pay_maintitle', models.IntegerField(blank=True, db_column='PAY_MAINTITLE', null=True)),
                ('pay_print', models.IntegerField(blank=True, db_column='PAY_PRINT', null=True)),
                ('auto_detail', models.IntegerField(blank=True, db_column='AUTO_DETAIL', null=True)),
                ('auto_qty', models.IntegerField(blank=True, db_column='AUTO_QTY', null=True)),
                ('auto_price', models.IntegerField(blank=True, db_column='AUTO_PRICE', null=True)),
                ('auto_amt', models.IntegerField(blank=True, db_column='AUTO_AMT', null=True)),
                ('auto_title', models.IntegerField(blank=True, db_column='AUTO_TITLE', null=True)),
                ('auto_maintitle', models.IntegerField(blank=True, db_column='AUTO_MAINTITLE', null=True)),
                ('auto_print', models.IntegerField(blank=True, db_column='AUTO_PRINT', null=True)),
                ('product_license', models.CharField(blank=True, db_column='Product_License', max_length=20, null=True)),
                ('rno', models.IntegerField(blank=True, db_column='RNo', null=True)),
                ('rinvdesc', models.IntegerField(blank=True, db_column='RInvDesc', null=True)),
                ('rcoutstanding', models.IntegerField(blank=True, db_column='RCOutStanding', null=True)),
                ('rtopup', models.IntegerField(blank=True, db_column='RTopUp', null=True)),
                ('rnoutstanding', models.IntegerField(blank=True, db_column='RNOutStanding', null=True)),
                ('ritem', models.IntegerField(blank=True, db_column='RItem', null=True)),
                ('rup', models.IntegerField(blank=True, db_column='RUP', null=True)),
                ('rdis', models.IntegerField(blank=True, db_column='RDIS', null=True)),
                ('rnp', models.IntegerField(blank=True, db_column='RNP', null=True)),
                ('rqty', models.IntegerField(blank=True, db_column='RQTY', null=True)),
                ('rdp', models.IntegerField(blank=True, db_column='RDP', null=True)),
                ('ramt', models.IntegerField(blank=True, db_column='RAmt', null=True)),
                ('rfooter', models.IntegerField(blank=True, db_column='RFooter', null=True)),
                ('rsubfoot', models.IntegerField(blank=True, db_column='RSubFoot', null=True)),
                ('rheaderfoot', models.IntegerField(blank=True, db_column='RHeaderFoot', null=True)),
                ('rcndesc', models.IntegerField(blank=True, db_column='RCNDesc', null=True)),
                ('rcnamt', models.IntegerField(blank=True, db_column='RCNAmt', null=True)),
                ('cpl', models.IntegerField(blank=True, db_column='CPL', null=True)),
                ('rinvline1', models.IntegerField(blank=True, db_column='RInvLine1', null=True)),
                ('rinvline2', models.IntegerField(blank=True, db_column='RInvLine2', null=True)),
                ('rinvoice', models.IntegerField(blank=True, db_column='RInvoice', null=True)),
                ('rpaymode', models.IntegerField(blank=True, db_column='RPaymode', null=True)),
                ('ramount', models.IntegerField(blank=True, db_column='RAmount', null=True)),
                ('rtotamount', models.IntegerField(blank=True, db_column='RTotAmount', null=True)),
                ('rinvline3', models.IntegerField(blank=True, db_column='RInvLine3', null=True)),
                ('logo_transaction', models.TextField(blank=True, db_column='LOGO_Transaction', null=True)),
                ('trans_logo', models.BinaryField(blank=True, db_column='Trans_Logo', null=True)),
                ('trans_h1', models.CharField(blank=True, db_column='Trans_H1', max_length=500, null=True)),
                ('trans_h2', models.CharField(blank=True, db_column='Trans_H2', max_length=500, null=True)),
                ('trans_promo1', models.CharField(blank=True, db_column='Trans_Promo1', max_length=500, null=True)),
                ('trans_promo2', models.CharField(blank=True, db_column='Trans_Promo2', max_length=500, null=True)),
                ('trans_footer1', models.CharField(blank=True, db_column='Trans_Footer1', max_length=500, null=True)),
                ('trans_footer2', models.CharField(blank=True, db_column='Trans_Footer2', max_length=500, null=True)),
                ('trans_footer3', models.CharField(blank=True, db_column='Trans_Footer3', max_length=500, null=True)),
                ('trans_footer4', models.CharField(blank=True, db_column='Trans_Footer4', max_length=500, null=True)),
                ('trans_message1', models.CharField(blank=True, db_column='Trans_Message1', max_length=500, null=True)),
                ('gst_reg_no', models.CharField(blank=True, db_column='GST_REG_NO', max_length=20, null=True)),
                ('comp_title5', models.CharField(blank=True, db_column='Comp_Title5', max_length=50, null=True)),
                ('comp_title6', models.CharField(blank=True, db_column='Comp_Title6', max_length=50, null=True)),
                ('comp_title7', models.CharField(blank=True, db_column='Comp_Title7', max_length=50, null=True)),
                ('comp_title8', models.CharField(blank=True, db_column='Comp_Title8', max_length=50, null=True)),
                ('comp_title9', models.CharField(blank=True, db_column='Comp_Title9', max_length=50, null=True)),
                ('comp_title10', models.CharField(blank=True, db_column='Comp_Title10', max_length=50, null=True)),
                ('company_reg_no', models.CharField(blank=True, db_column='COMPANY_REG_NO', max_length=20, null=True)),
                ('subrpt_show_title', models.BooleanField(db_column='SubRpt_Show_Title', null=True)),
                ('subrpt_show_footer', models.BooleanField(db_column='SubRpt_Show_Footer', null=True)),
                ('subrpt_show_gst_summary', models.BooleanField(db_column='SubRpt_Show_GST_Summary', null=True)),
                ('subrpt_show_footer_tax', models.BooleanField(db_column='SubRpt_Show_Footer_Tax', null=True)),
                ('subrpt_show_footer_trmt_available', models.BooleanField(db_column='SubRpt_Show_Footer_Trmt_Available', null=True)),
                ('subrpt_show_footer_cust_sign', models.BooleanField(db_column='SubRpt_Show_Footer_Cust_Sign', null=True)),
                ('subrpt_show_footerremark', models.BooleanField(db_column='SubRpt_Show_FooterRemark', null=True)),
                ('gst_start_datetime', models.DateTimeField(blank=True, db_column='GST_Start_DateTime', null=True)),
                ('gst_end_datetime', models.DateTimeField(blank=True, db_column='GST_End_DateTime', null=True)),
                ('sst_salestax_reg_no', models.CharField(blank=True, db_column='SST_SalesTax_REG_NO', max_length=20, null=True)),
                ('sst_servicetax_reg_no', models.CharField(blank=True, db_column='SST_ServiceTax_REG_NO', max_length=20, null=True)),
                ('subrpt_show_footer_sst', models.BooleanField(db_column='SubRpt_Show_Footer_SST', null=True)),
                ('subrpt_show_tax_summary_sst', models.BooleanField(db_column='SubRpt_Show_Tax_Summary_SST', null=True)),
                ('subrpt_show_footer_tax_sst', models.BooleanField(db_column='SubRpt_Show_Footer_Tax_SST', null=True)),
                ('subrpt_show_footer_trmt_available_sst', models.BooleanField(db_column='SubRpt_Show_Footer_Trmt_Available_SST', null=True)),
                ('subrpt_show_footer_cust_sign_sst', models.BooleanField(db_column='SubRpt_Show_Footer_Cust_Sign_SST', null=True)),
                ('subrpt_show_footerremark_sst', models.BooleanField(db_column='SubRpt_Show_FooterRemark_SST', null=True)),
                ('sst_start_datetime', models.DateTimeField(blank=True, db_column='SST_Start_DateTime', null=True)),
                ('sst_end_datetime', models.DateTimeField(blank=True, db_column='SST_End_DateTime', null=True)),
                ('print_logo_position_x', models.FloatField(blank=True, db_column='Print_Logo_Position_X', null=True)),
                ('print_logo_position_y', models.FloatField(blank=True, db_column='Print_Logo_Position_Y', null=True)),
                ('logourl', models.TextField(blank=True, db_column='logoUrl', null=True)),
                ('receipttemplate', models.CharField(blank=True, db_column='ReceiptTemplate', max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('logo_pic', models.ImageField(null=True, upload_to='img')),
            ],
            options={
                'db_table': 'Title',
            },
        ),
    ]
