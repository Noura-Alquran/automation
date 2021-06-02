import re

# phone numbers with missing area code should presume 206
with open('./assets/potential-contacts.txt') as f:
    content= f.readlines()
    content=''.join(content)
    # Phone numbers may be in various formats.
    #(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc
    phone_numbers=re.findall(r"\d{3}[-\-\s]\d{3}[-\-\s]\d{4}|\(\d{3}\)\s*\d{3}[-\-\s]\d{4}|\d{3}[-\-\s]\d{4}", content)
    # print (phone_numbers)
    emails=re.findall(r'[\w\.-]+@[\w\.-]+',content)
    # print(emails)

    
# phone numbers should be stored in xxx-yyy-zzzz format.
# https://stackoverflow.com/questions/51227601/python-format-phone-number/66233632
formated_phone_numbers=[]
for i in phone_numbers:
    i='%s-%s-%s' % tuple(re.findall(r'\d{4}$|\d{3}|\d{2}', i))
    formated_phone_numbers.append(i)

formated_phone_numbers.sort()
with open('./assets/phone_numbers.txt','w') as f:
    f.write('\n\n'.join(formated_phone_numbers))

emails.sort()
with open('./assets/emails.txt','w') as f:
    f.write('\n\n'.join(emails))





