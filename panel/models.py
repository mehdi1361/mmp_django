from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'State'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    state = models.ForeignKey(State)

    class Meta:
        db_table = 'City'

    def __str__(self):
        return self.name

class Prefix(models.Model):
    prefix_num = models.CharField(max_length=10, verbose_name='prefix_num_col')
    city = models.ForeignKey(City)
    class Meta:
        db_table = 'PrefixNum'

    def __str__(self):
        return self.prefix_num

class Service(models.Model):
    name = models.CharField(max_length=40,verbose_name='Service_name', help_text= _('service english name'))
    name_persian = models.CharField(max_length=40,verbose_name='service_name_persian',help_text= _('service persian name'))
    service_id = models.CharField(max_length=20)
    service_id_free = models.CharField(max_length=20)
    short_code = models.CharField(max_length=20)
    short_code_free = models.CharField(max_length=20)
    subscribe_keyword = models.CharField(max_length=20)
    unsubscribe_keyword = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mo_url = models.CharField(max_length=300)
    unsubscribe_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField()
    help_messge_visible = models.BooleanField()
    wsdl_visible = models.BooleanField()
    report_visible = models.BooleanField()

    class Meta:
        db_table = 'services'
        ordering = ['id']
    def __str__(self):
        return self.name_persian

class User(models.Model):
    mobile = models.CharField(db_index=True,max_length=15,verbose_name='mobile_number')
    service = models.ForeignKey(Service)
    subscribe = models.BooleanField(default=True)
    description = models.CharField(max_length=255,null=True)
    user_deleted_key = models.BooleanField(default=False,verbose_name='deleted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    prefix_code = models.ForeignKey(Prefix,null=True)
    black_list = models.BooleanField(default=False)
    black_list_desc = models.CharField(null=True,max_length=200)
    class Meta:
        db_table = 'users'
        ordering = ['id']
        unique_together = ('mobile', 'service')

    def __str__(self):
        return self.mobile

class Keyword(models.Model):
    keyword = models.CharField(max_length=20,unique=True)
    service = models.ForeignKey(Service, verbose_name='service_id')
    unsubscribe = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'keywords'
        ordering = ['id']

    def __str__(self):
        return self.service.name + '->' + self.keyword

class Statistic(models.Model):
    service = models.ForeignKey(Service)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    inbound = models.IntegerField(default=0)
    outbound_free = models.IntegerField(default=0)
    outbound_od = models.IntegerField(default=0)
    outbound_ac = models.IntegerField(default=0)
    delivered_free = models.IntegerField(default=0)
    delivered_od = models.IntegerField(default=0)
    delivered_ac = models.IntegerField(default=0)
    subscribe = models.IntegerField(default=0)
    unsubscribe = models.IntegerField(default=0)
    active_user = models.IntegerField(default=0)
    prepaid_subscribers_count = models.IntegerField(verbose_name='prepaidSubscribersCount', default=0)
    postpaid_subscribers_count = models.IntegerField(verbose_name='postpaidSubscribersCount', default=0)
    prepaid_activation_count = models.IntegerField(verbose_name='prepaidActivationCount', default=0)
    postpaid_activation_count = models.IntegerField(verbose_name='postpaidActivationCount', default=0)
    prepaid_deactivation_count = models.IntegerField(verbose_name='prepaidDeactivationCount', default=0)
    postpaid_deactivation_count = models.IntegerField(verbose_name='postpaidDeactivationCount', default=0)
    prepaid_sent_message_count = models.IntegerField(verbose_name='prepaidSentMessageCount', default=0)
    postpaid_sent_message_count = models.IntegerField(verbose_name='postpaidSentMessageCount', default=0)
    failed_message = models.IntegerField(verbose_name='failed_message', default=0)
    class Meta:
        db_table = 'statistics'
        ordering = ['id']

    def __str__(self):
        return self.service

class History(models.Model):
    user = models.ForeignKey(User)
    action = models.CharField(max_length=20)
    by = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    short_code = models.CharField(max_length=20)
    mo_message = models.CharField(max_length=20)
    class Meta:
        db_table = 'history'

    def __str__(self):
        return self.id
