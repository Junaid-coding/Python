country_code = { 'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
print("country code for india:")
print(country_code.get('India', 'Not found'))
print("country code for Japan:")
print(country_code.get('Japan', 'Not found'))