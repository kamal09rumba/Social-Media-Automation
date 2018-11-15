import facebook
import csv

# Get Access Token from https://developers.facebook.com/tools/explorer/

graph = facebook.GraphAPI(access_token="ACESS_TOKEN", version="2.12")

# Get the page information
pageinfo = graph.get_object(id='me', fields='name')
pageid = pageinfo['id']
# print(pageid)
csv_file = open('notifications.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Notification Titles','Date'])
# Get notifications info
notifications = graph.get_object(f"{pageid}/notifications")
notifications = notifications['data']
for notification in notifications:
    try:
        # get notification details
        notificationTitles = graph.get_object(f"{notification['id']}?fields=title,created_time")
    except Exception as e:
        notificationTitles['title'] = None
        notificationTitles['created_time'] = None
    csv_writer.writerow([notificationTitles['title'],notificationTitles['created_time']])
csv_file.close()