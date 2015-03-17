
# coding: utf-8

# In[1]:

from fogbugz import FogBugz
import pandas as pd
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
# import mpld3
# mpld3.enable_notebook()
import seaborn as sb
import matplotlib.patches as mpatches
import numpy as np
import statsmodels.api as sm


# In[2]:

### create holders for website and token ##
URL = 'https://yesenergy.fogbugz.com'
TOKEN = 'v01lckss2fpbbtmsuo1ojd8lu2ftig'


# In[3]:

## create bunch of empty variables to append to ##
title13 = []
status13 = []
opened_by13 = []
case_num13 = []
resolved_by13 = []
closed_by13 = []
priority13 = []
customer_email13 = []
mailbox13 = []
date_opened13 = []
date_resolved13 = []
date_closed13 = []
release_notes13 = []
category13 = []
tags13 = []
project13 = []


# In[4]:

## open gateway? do something ##
fb = FogBugz(URL,TOKEN)


# In[5]:

inq_call_2013 = fb.search(q='opened:"6/1/2013..12/31/2013" category:Inquiry',  cols="ixBug,sTitle,sStatus,ixPersonOpenedBy,ixPersonResolvedBy,ixPersonClosedBy,ixPriority,sCustomerEmail,ixMailbox,sCategory,dtOpened,dtResolved,dtClosed,sReleaseNotes,tags,sProject")


# In[6]:

for case in inq_call_2013.cases.findAll('case'):
    case_num13.append(case.ixbug.string) 
    title13.append(case.stitle.string.encode('UTF-8'))
    status13.append(case.sstatus.string.encode('UTF-8'))
    opened_by13.append(case.ixpersonopenedby.string)
    resolved_by13.append(case.ixpersonresolvedby.string)
    closed_by13.append(case.ixpersonclosedby.string)
    priority13.append(case.ixpriority.string)
    try:
        customer_email13.append(case.scustomeremail.string.encode('UTF-8'))
    except AttributeError:
        customer_email13.append(case.scustomeremail.string)
    mailbox13.append(case.ixmailbox.string)
    date_opened13.append(case.dtopened.string)
    date_resolved13.append(case.dtresolved.string)
    date_closed13.append(case.dtclosed.string)
    release_notes13.append(case.sreleasenotes.string)
    category13.append(case.scategory.string.encode('UTF-8'))
    project13.append(case.sproject.string.encode('UTF-8'))
    try:
        tags13.append(case.tags.string.encode('UTF-8'))
    except AttributeError:
        tags13.append(case.tags.string)
    


# In[7]:

d2013 = {'case_num' : case_num13,
	 'title' : title13,
	 'status' : status13,
	 'opened_by' : opened_by13,
	 'resolved_by' : resolved_by13,
	 'closed_by' : closed_by13,
	 'priority' : priority13,
	 'customer_email' : customer_email13,
	 'mailbox' : mailbox13,
	 'date_opened' : date_opened13,
	 'date_closed' : date_closed13,
     'date_resolved' : date_resolved13,
	 'release_notes' : release_notes13,
	 'category' : category13,
	 'tags' : tags13,
	 'project' : project13}

df2013 = pd.DataFrame(d2013)


# In[8]:

df2013.date_opened = df2013.date_opened.apply(lambda d: datetime.strptime(d, "%Y-%m-%dT%H:%M:%SZ" ))


# In[9]:

df2013['month'] = df2013.date_opened.apply(lambda d: datetime(d.year, d.month, 1))


# In[10]:

def f(row, column):
    if row[column] is None:
        val =0
    elif row[column] is not None:
        val = 1
    return val
def fx(row, column):
    if row[column] =='^Closed':
        val =0
    elif row[column] != '^Closed':
        val = 1
    return val


# In[11]:

df2013g = df2013
df2013g['total'] = df2013.apply(lambda x: f(x, 'case_num'), axis =1)
df2013g['resolved'] = df2013.apply(lambda x: f(x, 'date_resolved'), axis=1)
df2013g['closed'] = df2013.apply(lambda x: f(x, 'date_closed'), axis=1)


# In[12]:

df2013g = df2013g.groupby(['month']).sum()


# In[13]:

df2013g.index = pd.to_datetime(df2013g.index)


# In[14]:

df2013g = df2013g.reindex(index = [date(2013,1,1), date(2013,2,1), date(2013,3,1), date(2013,4,1), date(2013,5,1), date(2013,6,1), date(2013,7,1), date(2013,8,1), date(2013,9,1), date(2013,10,1), date(2013,11,1), date(2013,12,1)], columns = ['total', 'resolved', 'closed'])


# In[15]:

df2013g = df2013g.reset_index()


# In[16]:

title14 = []
status14 = []
opened_by14 = []
case_num14 = []
resolved_by14 = []
closed_by14 = []
priority14 = []
customer_email14 = []
mailbox14 = []
date_opened14 = []
date_resolved14 = []
date_closed14 = []
release_notes14 = []
category14 = []
tags14 = []
project14 = []


# In[17]:

inq_call_2014 = fb.search(q='opened:"01/1/2014..12/31/2014" category:Inquiry',  cols="ixBug,sTitle,sStatus,ixPersonOpenedBy,ixPersonResolvedBy,ixPersonClosedBy,ixPriority,sCustomerEmail,ixMailbox,sCategory,dtOpened,dtResolved,dtClosed,sReleaseNotes,tags,sProject")


# In[18]:

for case in inq_call_2014.cases.findAll('case'):
    case_num14.append(case.ixbug.string) 
    title14.append(case.stitle.string.encode('UTF-8'))
    status14.append(case.sstatus.string.encode('UTF-8'))
    opened_by14.append(case.ixpersonopenedby.string)
    resolved_by14.append(case.ixpersonresolvedby.string)
    closed_by14.append(case.ixpersonclosedby.string)
    priority14.append(case.ixpriority.string)
    try:
        customer_email14.append(case.scustomeremail.string.encode('UTF-8'))
    except AttributeError:
        customer_email14.append(case.scustomeremail.string)
    mailbox14.append(case.ixmailbox.string)
    date_opened14.append(case.dtopened.string)
    date_resolved14.append(case.dtresolved.string)
    date_closed14.append(case.dtclosed.string)
    release_notes14.append(case.sreleasenotes.string)
    category14.append(case.scategory.string.encode('UTF-8'))
    project14.append(case.sproject.string.encode('UTF-8'))
    try:
        tags14.append(case.tags.string.encode('UTF-8'))
    except AttributeError:
        tags14.append(case.tags.string)
    


# In[19]:

d2014 = {'case_num' : case_num14,
	 'title' : title14,
	 'status' : status14,
	 'opened_by' : opened_by14,
	 'resolved_by' : resolved_by14,
	 'closed_by' : closed_by14,
	 'priority' : priority14,
	 'customer_email' : customer_email14,
	 'mailbox' : mailbox14,
	 'date_opened' : date_opened14,
	 'date_closed' : date_closed14,
     'date_resolved' : date_resolved14,
	 'release_notes' : release_notes14,
	 'category' : category14,
	 'tags' : tags14,
	 'project' : project14}

df2014 = pd.DataFrame(d2014)


# In[20]:

df2014.date_opened = df2014.date_opened.apply(lambda d: datetime.strptime(d, "%Y-%m-%dT%H:%M:%SZ" ))


# In[21]:

df2014['month'] = df2014.date_opened.apply(lambda d: datetime(d.year, d.month, 1))


# In[22]:

df2014g = df2014
df2014g['total'] = df2014.apply(lambda x: f(x, 'case_num'), axis =1)
df2014g['resolved'] = df2014.apply(lambda x: f(x, 'date_resolved'), axis=1)
df2014g['closed'] = df2014.apply(lambda x: f(x, 'date_closed'), axis=1)


# In[23]:

df2014g = df2014.groupby(['month']).sum()


# In[24]:

df2014g = df2014g.reset_index()


# In[25]:

df2014g = df2014g.drop(df2014g.index[12])


# In[26]:

title15 = []
status15 = []
opened_by15 = []
case_num15 = []
resolved_by15 = []
closed_by15 = []
priority15 = []
customer_email15 = []
mailbox15 = []
date_opened15 = []
date_resolved15 = []
date_closed15 = []
release_notes15 = []
category15 = []
tags15 = []
project15 = []


# In[27]:

inq_call_2015 = fb.search(q='opened:"01/1/2015..today" category:Inquiry',  cols="ixBug,sTitle,sStatus,ixPersonOpenedBy,ixPersonResolvedBy,ixPersonClosedBy,ixPriority,sCustomerEmail,ixMailbox,sCategory,dtOpened,dtResolved,dtClosed,sReleaseNotes,tags,sProject")


# In[28]:

for case in inq_call_2015.cases.findAll('case'):
    case_num15.append(case.ixbug.string) 
    title15.append(case.stitle.string.encode('UTF-8'))
    status15.append(case.sstatus.string.encode('UTF-8'))
    opened_by15.append(case.ixpersonopenedby.string)
    resolved_by15.append(case.ixpersonresolvedby.string)
    closed_by15.append(case.ixpersonclosedby.string)
    priority15.append(case.ixpriority.string)
    try:
        customer_email15.append(case.scustomeremail.string.encode('UTF-8'))
    except AttributeError:
        customer_email15.append(case.scustomeremail.string)
    mailbox15.append(case.ixmailbox.string)
    date_opened15.append(case.dtopened.string)
    date_resolved15.append(case.dtresolved.string)
    date_closed15.append(case.dtclosed.string)
    release_notes15.append(case.sreleasenotes.string)
    category15.append(case.scategory.string.encode('UTF-8'))
    project15.append(case.sproject.string.encode('UTF-8'))
    try:
        tags15.append(case.tags.string.encode('UTF-8'))
    except AttributeError:
        tags15.append(case.tags.string)


# In[29]:

d2015 = {'case_num' : case_num15,
	 'title' : title15,
	 'status' : status15,
	 'opened_by' : opened_by15,
	 'resolved_by' : resolved_by15,
	 'closed_by' : closed_by15,
	 'priority' : priority15,
	 'customer_email' : customer_email15,
	 'mailbox' : mailbox15,
	 'date_opened' : date_opened15,
	 'date_closed' : date_closed15,
     'date_resolved' : date_resolved15,
	 'release_notes' : release_notes15,
	 'category' : category15,
	 'tags' : tags15,
	 'project' : project15}

df2015 = pd.DataFrame(d2015)


# In[30]:

df2015.date_opened = df2015.date_opened.apply(lambda d: datetime.strptime(d, "%Y-%m-%dT%H:%M:%SZ" ))


# In[31]:

df2015['month'] = df2015.date_opened.apply(lambda d: datetime(d.year, d.month, 1))


# In[32]:

df2015g = df2015
df2015g['total'] = df2015.apply(lambda x: f(x, 'case_num'), axis =1)
df2015g['resolved'] = df2015.apply(lambda x: f(x, 'date_resolved'), axis=1)
df2015g['closed'] = df2015.apply(lambda x: f(x, 'date_closed'), axis=1)


# In[33]:

df2015g = df2015.groupby(['month']).sum()


# In[34]:

df2015g.index = pd.to_datetime(df2015g.index)


# In[35]:

df2015g = df2015g.reindex(index = [date(2015,1,1), date(2015,2,1), date(2015,3,1), date(2015,4,1), date(2015,5,1), date(2015,6,1), date(2015,7,1), date(2015,8,1), date(2015,9,1), date(2015,10,1), date(2015,11,1), date(2015,12,1)], columns = ['total', 'resolved', 'closed'])


# In[36]:

df2015g = df2015g.reset_index()


# In[37]:

n_groups = 12
index = np.arange(n_groups)
width = .30
fig = plt.figure(figsize=(12,12))
#ax = plt.subplots()
ax = fig.add_subplot(111)
year_13 = ax.bar(index, df2013g['total'], width, color = '#F48022')
year_14 = ax.bar(index+width, df2014g['total'], width, color = '#1ABFD9')
year_15 = ax.bar(index+width+width, df2015g['total'], width, color = '#5A582C')
ax.set_xticks(index+width+width)
ax.set_xticklabels(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ), color = '#5A582C' )
ax.tick_params(labelsize ='medium', labelcolor = '#5A582C')
# ax.set_xlabel('')
ax.set_ylabel('Number of Cases', color = '#5A582C')
ax.set_title('Looking back at Support', color = '#5A582C', fontsize='15')
blue_patch = mpatches.Patch(color='#F48022', label = '2013')
orange_patch = mpatches.Patch(color='#1ABFD9', label = '2014')
green_patch = mpatches.Patch(color='#5A582C', label = '2015')
l =ax.legend(handles=[blue_patch, orange_patch, green_patch])
for text in l.get_texts():
    text.set_color('#5A582C')
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['top'].set_color('none')
### add path to where you want to save image of your file here ##
 plt.savefig('C:/Users/Geo3/support_month_year.png', dpi=None, facecolor = 'w', edgecolor='w', orientation = 'landscape', papertype=None, format='png', transparent=False, bbox_inches=None, pad_inches=.1, frameon=None)



# In[ ]:



