"""servermanage URL Configuration

"""
from django.conf.urls import url
from sm.views import *

urlpatterns = [
	url(r'^server_manage/$',server_manage,name='server_manage'),
	url(r'^addserver/$',addserver,name='addserver'),
	url(r'^del_server$',del_server,name='del_server'),
	url(r'^server_manage/batch_del$',batch_del,name='batch_del'),
	url(r'^server_manage/queryIP$',queryIP,name='queryIP'),
	url(r'^edit_server$',edit_server,name='edit_server'),
	url(r'ssh_server$',ssh_server,name='ssh_server'),
	url(r'^execute_cmd$',execute_cmd,name='execute_cmd'),
	url(r'^execute_command$',execute_command,name='execute_command'),
	url(r'^create_server_config$',create_server_config,name='create_server_config'),

]
