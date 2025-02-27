from django.contrib import admin
from .models import (Gender, Employee, Fmspw, Attendance2, Customer, Images, Treatment, Stock,
                     Systemloginlog, EmpSitelist, ItemClass, ItemRange, ItemDept, ItemDiv, ItemType, ControlNo,
                     Treatment_Master,
                     Appointment, GstSetting, Securities, PosTaud, Paytable, PayGroup, PosHaud, PosDaud, PosTaud,
                     TreatmentAccount,
                     ItemStatus, Source, CustomerClass, Systemlog, ScheduleHour, ScheduleMonth, ApptType, ItemHelper,
                     Multistaff,
                     DepositType, ItemUomprice, TmpItemHelper, ItemUom, PackageDtl, PosDisc, FocReason, DepositAccount,
                     PrepaidAccount, PrepaidAccountCondition, VoucherCondition, Title, Systemsetup, PackageHdr,
                     ItemBatch, Stktrn, Workschedule, Securitycontrollist, Securitylevellist, MenuSecurity,
                     MenuSecuritylevellist, Skillstaff, CustomerFormControl
                     )
from cl_app.models import ItemSitelist, SiteGroup

# # Register your models here.
admin.site.register(SiteGroup)
admin.site.register(ItemSitelist)
admin.site.register(Gender)
admin.site.register(Employee)
admin.site.register(Fmspw)
admin.site.register(Attendance2)
admin.site.register(Stock)
admin.site.register(Customer)
admin.site.register(Images)
admin.site.register(Treatment)
admin.site.register(Systemloginlog)
admin.site.register(Systemlog)
admin.site.register(EmpSitelist)
admin.site.register(ItemClass)
admin.site.register(ItemRange)
admin.site.register(ItemDept)
admin.site.register(ControlNo)
admin.site.register(Treatment_Master)
admin.site.register(Appointment)
admin.site.register(ApptType)
admin.site.register(ItemDiv)
admin.site.register(GstSetting)
admin.site.register(Securities)
admin.site.register(Paytable)
admin.site.register(PayGroup)
admin.site.register(PosHaud)
admin.site.register(PosDaud)
admin.site.register(PosTaud)
admin.site.register(TreatmentAccount)
admin.site.register(ItemStatus)
admin.site.register(Source)
admin.site.register(CustomerClass)
admin.site.register(ScheduleHour)
admin.site.register(ScheduleMonth)
admin.site.register(ItemHelper)
admin.site.register(Multistaff)
admin.site.register(DepositType)
admin.site.register(ItemType)
admin.site.register(ItemUomprice)
admin.site.register(TmpItemHelper)
admin.site.register(ItemUom)
admin.site.register(PackageDtl)
admin.site.register(PosDisc)
admin.site.register(FocReason)
admin.site.register(DepositAccount)
admin.site.register(PrepaidAccount)
admin.site.register(PrepaidAccountCondition)
admin.site.register(VoucherCondition)
admin.site.register(Title)
admin.site.register(Systemsetup)
admin.site.register(PackageHdr)
admin.site.register(ItemBatch)
admin.site.register(Stktrn)
admin.site.register(Workschedule)
admin.site.register(Securitycontrollist)
admin.site.register(Securitylevellist)
admin.site.register(MenuSecurity)
admin.site.register(MenuSecuritylevellist)
admin.site.register(Skillstaff)
admin.site.register(CustomerFormControl)
