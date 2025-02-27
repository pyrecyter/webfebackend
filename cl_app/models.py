from django.db import models
from cl_table.models import City, State, Country, Fmspw, ItemUom, Customer
from django.conf import settings

# Create your models here.
#intial

#Final
class SiteGroup(models.Model):
    id = models.BigAutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active',default=True)  # Field name made lowercase.
    is_delete = models.BooleanField(db_column='Is_Delete', null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'Site_Group'

    def __str__(self):
        return str(self.description)


class ItemSitelist(models.Model):
    itemsite_id = models.BigAutoField(db_column='ItemSite_ID', primary_key=True)  # Field name made lowercase.
    itemsite_code = models.CharField(db_column='ItemSite_Code', max_length=20, null=True)  # Field name made lowercase.
    itemsite_desc = models.CharField(db_column='ItemSite_Desc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    itemsite_type = models.CharField(db_column='ItemSite_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_purchasedept = models.CharField(db_column='Item_PurchaseDept', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemsite_address = models.CharField(db_column='ItemSite_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemsite_postcode = models.CharField(db_column='ItemSite_Postcode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ItemSite_Cityid   = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    itemsite_city = models.CharField(db_column='ItemSite_City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ItemSite_Stateid  = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
    itemsite_state = models.CharField(db_column='ItemSite_State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ItemSite_Countryid  = models.ForeignKey(Country, on_delete=models.PROTECT,  null=True)
    itemsite_country = models.CharField(db_column='ItemSite_Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemsite_phone1 = models.CharField(db_column='ItemSite_Phone1', max_length=50,  null=True)  # Field name made lowercase.
    itemsite_phone2 = models.CharField(db_column='ItemSite_Phone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemsite_fax = models.CharField(db_column='ItemSite_Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemsite_email = models.EmailField(db_column='ItemSite_Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ItemSite_Userid = models.ForeignKey(Fmspw, on_delete=models.PROTECT, null=True)
    itemsite_user = models.CharField(db_column='ItemSite_User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemsite_date = models.DateField(db_column='ItemSite_Date', blank=True, null=True)  # Field name made lowercase.
    itemsite_time = models.DateTimeField(db_column='ItemSite_Time', blank=True, null=True)  # Field name made lowercase.
    itemsite_isactive = models.BooleanField(db_column='ItemSite_Isactive',default=True)  # Field name made lowercase.
    itemsite_refcode = models.CharField(db_column='ITEMSITE_REFCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    Site_Groupid    = models.ForeignKey(SiteGroup, on_delete=models.PROTECT, null=True)
    site_group = models.CharField(db_column='Site_Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    site_is_gst = models.BooleanField(db_column='SITE_IS_GST', null=True,default=False)  # Field name made lowercase.
    account_code = models.CharField(db_column='Account_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientindex = models.BigIntegerField(db_column='ClientIndex', blank=True, null=True)  # Field name made lowercase.
    heartbeat = models.DateTimeField(db_column='HeartBeat', blank=True, null=True)  # Field name made lowercase.
    systemlog_mdpl_update = models.BooleanField(db_column='SystemLog_MDPL_Update', null=True,default=False)  # Field name made lowercase.
    ratings = models.CharField(db_column='Ratings', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pic_path = models.TextField(db_column='pic_Path', blank=True, null=True)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sitedbconnectionurl = models.CharField(db_column='siteDbConnectionUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    geolink = models.CharField(max_length=100, blank=True, null=True)
    weekdays_timing = models.CharField(max_length=100, blank=True, null=True)
    weekend_timing = models.CharField(max_length=100, blank=True, null=True)
    holliday_timing = models.CharField(max_length=100, blank=True, null=True)
    closed_on = models.CharField(db_column='Closed_on', max_length=100, blank=True, null=True)
    picpath = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(db_column='Owner', max_length=300, blank=True, null=True)
    services = models.ManyToManyField('cl_table.Stock', blank=True) 
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    skills_list = models.CharField(max_length=1000, null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)
  
    class Meta:
        db_table = 'Item_SiteList'
        unique_together = [['itemsite_desc','itemsite_phone1','itemsite_email']]

    def __str__(self):
        return str(self.itemsite_code)


# class TempUomPrice(models.Model):
#     id = models.AutoField(db_column='ID',primary_key=True)
#     Item_Codeid = models.ForeignKey('cl_table.Stock', on_delete=models.PROTECT, db_column='itemCodeid', blank=True, null=True) 
#     item_code = models.CharField(db_column='Item_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     Cust_Codeid = models.ForeignKey('cl_table.Customer', on_delete=models.PROTECT, blank=True, null=True)
#     cust_code = models.CharField(db_column='Cust_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     cart_id = models.CharField(max_length=20,blank=True, null=True)
#     cart_date = models.DateField(db_column='Cart_Date',null=True, blank=True)
#     Item_UOMid = models.ForeignKey('cl_table.ItemUom', on_delete=models.PROTECT,null=True, blank=True)
#     item_uom = models.CharField(db_column='Item_UOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     item_price = models.FloatField(db_column='ITEM_PRICE', blank=True, null=True)  # Field name made lowercase.
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'Temp_UomPrice'

#     def __str__(self):
#         return str(self.item_uom)

class ReverseTrmtReason(models.Model):
    id = models.BigAutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    rev_no = models.CharField(db_column='Rev_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rev_desc = models.CharField(db_column='Rev_Desc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rev_remark = models.CharField(db_column='Rev_Remark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_active', blank=True, null=True,default=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Reverse_Trmt_Reason'

    def __str__(self):
        return str(self.rev_desc)    


class VoidReason(models.Model):
    id = models.AutoField(primary_key=True)
    reason_code = models.CharField(db_column='Reason_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reason_desc = models.CharField(db_column='Reason_Desc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True,default=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Void_Reason'

    def __str__(self):
        return str(self.reason_desc)    
    
# class LoggedInUser(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=40, blank=True, null=True)
#     current_key = models.CharField(max_length=40, blank=True, null=True)
    
#     class Meta:
#         db_table = 'logged_inuser'

#     def str(self):
#         return self.user.username