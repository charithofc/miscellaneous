# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:38:30 2019

@author: charitha
"""

def convert_source(x, result_file_type):
    if result_file_type == 'old':
        x = x.replace('new_segments', 'New Segments')
        x = x.replace('remarketing', 'Remarketing')
        
    if result_file_type == 'new':
        x = x.replace( 'New Segments','new_segments')
        x = x.replace('Remarketing','remarketing')
        
    return x

def convert_metric(x, result_file_type):
    if result_file_type == 'old':
        x = x.replace('transactions', 'Transactions')
        x = x.replace('users', 'Users')
        x = x.replace('conversion_rate', 'Conversion Rate')
        x = x.replace('bounce_rate', 'Bounce Rate')
        x = x.replace('avewrage_order_value', 'Avg. Order Value')
        
    if result_file_type == 'new':
        x = x.replace('Transactions', 'transactions',)
        x = x.replace('Users', 'users')
        x = x.replace('Conversion Rate','conversion_rate')
        x = x.replace('Bounce Rate', 'bounce_rate')
        x = x.replace('Avg. Order Value', 'average_order_value')
        
    return x
    

def old_to_new(data_frame):
    data_frame = data_frame.rename(columns = {'customerName':'client_id',
                                              'metric':'metric', 
                                              'type':'type', 
                                              'source':'source', 
                                              'siteAudienceSize':'site_audience_size',
                                              'avgMetric':'avg_metric', 
                                              'propertyTitle':'property_title', 
                                              'transactionType':'transaction_type',
                                              'backendName':'backend_name', 
                                              'interfaceName':'interface_name',
                                              'properties.0':'properties',
                                              'segmentAudienceSize':'segment_audience_size', 
                                              'transaction':'transaction',
                                              'audienceMetric':'audience_metric'})
    result_file_type = 'new'
    data_frame[['source']] = data_frame[['source']].apply(lambda x: convert_source(x, result_file_type))
    data_frame[['metric']] = data_frame[['metric']].apply(lambda x: convert_metric(x, result_file_type))
    
    return data_frame

def new_to_old(data_frame):

    
    data_frame = data_frame.rename(columns = {'client_id':'customerName',
                                              'metric':'metric', 
                                              'type':'type', 
                                              'source':'source', 
                                              'site_audience_size':'siteAudienceSize',
                                              'avg_metric':'avgMetric', 
                                              'property_title':'propertyTitle', 
                                              'transaction_type':'transactionType',
                                              'backend_name':'backendName', 
                                              'interface_name':'interfaceName',
                                              'properties':'properties.0',
                                              'segment_audience_size':'segmentAudienceSize', 
                                              'transaction':'transaction',
                                              'audience_metric':'audienceMetric'})
    result_file_type = 'old'
    data_frame[['source']] = data_frame[['source']].apply(lambda x: convert_source(x, result_file_type))
    data_frame[['metric']] = data_frame[['metric']].apply(lambda x: convert_metric(x, result_file_type))
    
    return data_frame


