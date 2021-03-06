import requests  # pip install requests
import json  # pip install simplejson
import facebook  # pip install facebook-sdk

user_location = 'London,UK'
# IP API
url = 'http://ip-api.com/json'
requestLocation = requests.get(url)
if requestLocation.status_code >= 200 < 400:
    data = json.loads(requestLocation.text)
    user_location = data['city'] + ',' + data['countryCode']

# ==============================================================
# Weather API
api_key = '9bb4b43bf13147ef8628e69c31b866ad';
url = 'https://api.weatherbit.io/v2.0/current?city=' + user_location + '&key=' + api_key

request = requests.get(url)
if request.status_code >= 200 < 400:
    data = json.loads(request.text)
    city = user_location
    temp = data['data'][0]['temp']
    desc = data['data'][0]['weather']['description']

    fb_msg = ''

    main_msg = 'City: ' + city + '\n' +\
               'Temp: ' + str(temp) + '\n' +\
               'Description: ' + desc + '\n'
    print(main_msg)

    fb_msg += main_msg

    lat = data['data'][0]['lat']
    lon = data['data'][0]['lon']
    timeZone = data['data'][0]['timezone']
# =========================================== End of Weather api
# ==============================================================
# Aladhan API
    url = 'http://api.aladhan.com/v1/currentTimestamp?zone=' + timeZone
    request = requests.get(url)
    if request.status_code >= 200 < 400:
        data = json.loads(request.text)
        timeStamp = data['data']

        url = 'http://api.aladhan.com/v1/timings/+' + timeStamp \
              + '?latitude=' + str(lat) + '&longitude=' + str(lon) + '&method=2'
        request = requests.get(url)
        if request.status_code >= 200 < 400:
            data = json.loads(request.text)

            dateNum = data['data']['date']['hijri']['date']

            dataStr = str(data['data']['date']['hijri']['day']) \
                      + ' ' + str(data['data']['date']['hijri']['month']['ar']) \
                      + ' ' + str(data['data']['date']['hijri']['year'])
            print(dateNum)
            print(dataStr + '\n')

            fb_msg += (dateNum + '\n' + dataStr + '\n\n')

            fajrTime = data['data']['timings']['Fajr']
            print('Fajr: ' + fajrTime)
            fb_msg += ('Fajr: ' + fajrTime + '\n')

            sunriseTime = data['data']['timings']['Sunrise']
            print('Sunrise: ' + sunriseTime)
            fb_msg += ('Sunrise: ' + sunriseTime + '\n')

            dhuhrTime = data['data']['timings']['Dhuhr']
            print('Dhuhr: ' + dhuhrTime)
            fb_msg += ('Dhuhr: ' + dhuhrTime + '\n')

            asrTime = data['data']['timings']['Asr']
            print('Asr: ' + asrTime)
            fb_msg += ('Asr: ' + asrTime + '\n')

            sunsetTime = data['data']['timings']['Sunset']
            print('Sunset: ' + sunsetTime)
            fb_msg += ('Sunset: ' + sunsetTime + '\n')

            maghribTime = data['data']['timings']['Maghrib']
            print('Maghrib: ' + maghribTime)
            fb_msg += ('Maghrib: ' + maghribTime + '\n')

            ishaTime = data['data']['timings']['Isha']
            print('Isha: ' + ishaTime)
            fb_msg += ('Isha: ' + ishaTime + '\n')

            url = 'http://api.aladhan.com/v1/currentTime?zone=' + timeZone
            request = requests.get(url)
            if request.status_code >= 200 < 400:
                data = json.loads(request.text)

                time = data['data']
                print('\n\nTime Now: ' + time)
                fb_msg += ('\n\nTime Now: ' + time)
# ===========================================================================End of aladhan api
# ==============================================================================================
# Facebook API
                token = 'EAAG9U3KJEmMBABkL4ZAEKgXa0ebFI7jY0w1zi08Uq1lBtlvzs8ymPe6ZADDZAUNkxnCWa3g6x3FACY3nwe' \
                        'J4blbSQ5vDBUV80X8aJSWyADBqwO75LU6xY4adM4oAXagBLNxja6uCmQhvNmrtbOgWxcRBbfMsCak77ywEF' \
                        'cEktnF0RJW9RZAx'
                try:
                    fb = facebook.GraphAPI(access_token=token)
                    fb.put_object(parent_object='me', connection_name='feed', message=fb_msg)
                except:
                    print('your app Status: Live, so you can\'t post\n'
                          'go to facebook developer then go to your app and make it status : In Development\n'
                          'and make sure you have a correct Access token and page on facebook connected with app')
