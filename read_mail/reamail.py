from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import email

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

aaa = None

def main():
   
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])
    

    if not messages:
        print ("No messages found.")
    else:
        print ("Message snippets:")
        message = messages[3]
        msg = service.users().messages().get(userId='me', id = message['id']).execute()
        for k, v in msg.items():
            print(k)
        
        print(msg['payload'])
    
        global aaa
        aaa = msg

if __name__ == '__main__':
    main()