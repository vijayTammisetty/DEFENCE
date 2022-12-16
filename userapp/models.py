from django.db import models
from adminapp.models import StaffModel
# import pyqrcode 
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

# Create your models here.


class ConfidentialDataModel(models.Model):
    data_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, null=True)
    file_name = models.CharField(max_length=250)
    data_file = models.FileField(upload_to='confidential_files/',null=True)
    status = models.CharField(max_length=20, default='pending')
    published_date = models.DateField(auto_now_add=True,null=True)


    class Meta:
        db_table = 'private_data'

class Request_recordModel(models.Model):
    request_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(StaffModel, related_name='sender', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(StaffModel, related_name='receiver', on_delete=models.CASCADE)
    request_title = models.CharField(max_length=250)
    
    department = models.CharField(max_length=250)
    description = models.CharField(max_length=1000,null=True)
    request_time = models.DateTimeField(auto_now_add=True)
    # file = models.FileField(upload_to='from_receiver/',null=True)
    qr_code = models.ImageField(blank=True,upload_to='qrimges/',null=True)

    status = models.CharField(max_length=250, default='sent')

    def save(self, *args,**kwargs ):
        qr_image = qrcode.make(f'Department :{self.department}\nTitle :{self.request_title}\nDescription :{self.description}')
        qr_offset = Image.new('RGB',(520,520),'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.department}_{self.request_title}_qr.png'
        stream = BytesIO()
        qr_offset.save(stream,'PNG')
        self.qr_code.save(files_name, File(stream),save=False)
        qr_offset.close()
        super().save(*args, **kwargs)



    class Meta:
        db_table = 'request_data'


class Send_request_files(models.Model):
    send_file_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(StaffModel, related_name='sender_id1', on_delete=models.CASCADE,null=True)
    receiver_id = models.ForeignKey(StaffModel, related_name='receiver_id1', on_delete=models.CASCADE,null=True)
    name_of_the_file = models.CharField(max_length=250)
    file = models.FileField(upload_to='from_receiver/',null=True)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=250, default='sent')

    class Meta:
        db_table='files_from_request_receiver'



