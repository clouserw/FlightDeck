from django.conf.urls.defaults import *

urlpatterns = patterns('jetpack.views',
	url(r'^addons/$', 'package_browser', {'type': 'a'}, name='jp_browser_addons'),
	url(r'^libraries/$', 'package_browser', {'type': 'l'}, name='jp_browser_libraries'),
	url(r'^addons/(?P<page_number>\d+)/$', 
		'package_browser', {'type': 'a'}, name='jp_browser_addons_page'),
	url(r'^libraries/(?P<page_number>\d+)/$', 
		'package_browser', {'type': 'l'}, name='jp_browser_libraries_page'),

	# display details of the PackageRevision
	url(r'^addon/(?P<id>[-\w]+)/$', 
		'package_details', {'type': 'a'}, name='jp_addon_details'),
	url(r'^library/(?P<id>[-\w]+)/$', 
		'package_details',{'type': 'l'},  name='jp_library_details'),
	url(r'^addon/(?P<id>[-\w]+)/version/(?P<version_name>.*)/$', 
		'package_details', {'type': 'a'}, name='jp_addon_version_details'),
	url(r'^library/(?P<id>[-\w]+)/version/(?P<version_name>.*)/$', 
		'package_details',{'type': 'l'},  name='jp_library_version_details'),
	url(r'^addon/(?P<id>[-\w]+)/revision/(?P<revision_number>\d+)/$', 
		'package_details', {'type': 'a'}, name='jp_addon_revision_details'),
	url(r'^library/(?P<id>[-\w]+)/revision/(?P<revision_number>\d+)/$', 
		'package_details',{'type': 'l'},  name='jp_library_revision_details'),
)

