# Send email

## Task Link
[Rosetta Code - Send email](https://rosettacode.org/wiki/Send_email)

## Java Code
### java_code_1.txt
```java
import java.util.Properties;

import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.Message.RecipientType;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

/**
 * Mail
 */
public class Mail
{
 /**
  * Session
  */
 protected Session session;

 /**
  * Mail constructor.
  * 
  * @param host Host
  */
 public Mail(String host)
 {
  Properties properties = new Properties();
  properties.put("mail.smtp.host", host);
  session = Session.getDefaultInstance(properties);
 }

 /**
  * Send email message.
  *
  * @param from From
  * @param tos Recipients
  * @param ccs CC Recipients
  * @param subject Subject
  * @param text Text
  * @throws MessagingException
  */
 public void send(String from, String tos[], String ccs[], String subject,
        String text)
        throws MessagingException
 {
  MimeMessage message = new MimeMessage(session);
  message.setFrom(new InternetAddress(from));
  for (String to : tos)
   message.addRecipient(RecipientType.TO, new InternetAddress(to));
  for (String cc : ccs)
   message.addRecipient(RecipientType.TO, new InternetAddress(cc));
  message.setSubject(subject);
  message.setText(text);
  Transport.send(message);
 }
}

```

## Python Code
### python_code_1.txt
```python
import smtplib

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

```

### python_code_2.txt
```python
sendemail(from_addr    = 'python@RC.net', 
          to_addr_list = ['RC@gmail.com'],
          cc_addr_list = ['RC@xx.co.uk'], 
          subject      = 'Howdy', 
          message      = 'Howdy from a python function', 
          login        = 'pythonuser', 
          password     = 'XXXXX')

```

### python_code_3.txt
```python
import win32com.client

def sendmail(to, title, body):
    olMailItem = 0
    ol = win32com.client.Dispatch("Outlook.Application")
    msg = ol.CreateItem(olMailItem)
    msg.To = to
    msg.Subject = title
    msg.Body = body
    msg.Send()
    ol.Quit()

sendmail("somebody@somewhere", "Title", "Hello")

```

