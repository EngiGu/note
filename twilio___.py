from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACa9f144f0d9535a319e28b0e2450bc44c'
auth_token = '777e41ec59549aa67a5e08e54d7d1463'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+16673031666',
                              body='你好，世界',
                              to='+8613148304735'
                          )

print(message.sid)