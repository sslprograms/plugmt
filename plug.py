import json, requests, threading, colorama, time, random, subprocess, os, json

dirs = ["conf", "errors", "input", "output"]
files = ["conf/settings.json", "errors/errors.txt", "input/cookies.txt", "input/proxies.txt", "output/checked_cookies.txt", "output/scraped_proxies.txt", "output/usernames.txt", "output/verified_cookies.txt", "output/refreshed_cookies.txt", "output/robux_cookies.txt", "output/scraped_proxies.txt", "output/credits.txt"]

if __name__ == '__main__':
    pass
else:
    quit()

def setup():
    if not os.path.exists("conf"):
        os.mkdir("conf")
        with open('conf/settings.json', 'w') as confFile:
            conf = {
                "settings": {
                "threads": 1,
                "key": "",
                "log_errors": True
                }
            }
            json.dump(conf, confFile, indent=4)
            confFile.close()
            
    for x in range(len(dirs)):
        if not os.path.exists(dirs[x]):
            os.mkdir(dirs[x])
    
    for x in range(len(files)):
        open(files[x], 'a')
        
        
setup()

class settings:
    def __init__(self):
        self.settings = json.loads(open('conf/settings.json', 'r').read())['settings']
        self.__settings__ = json.loads(open('conf/settings.json', 'r').read())
        self.cookies = open('input/cookies.txt', 'r').read().splitlines()
        self.proxies = open('input/proxies.txt', 'r').read()
optional_settings = settings()

cookies = optional_settings.cookies
proxies = optional_settings.proxies


class features:
    def __init__(self):
        pass
    
    def cookie_checker(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                check = session.get('https://users.roblox.com/v1/users/authenticated').json()['id']
                open('output/checked_cookies.txt', 'a').write(cookie+'\n')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_cookie_checker(self):
        threading_count = 0
        print('- Task has been activated! (Checking cookies..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.cookie_checker, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()

    def check_proxy(self, proxy):
        try:
            with requests.session() as session:
                session.proxies = {'http':proxy, 'https':proxy}
                if session.get('https://users.roblox.com/').json()['message'] == "OK":
                    open('output/checked_proxies.txt', 'a').write(proxy+'\n')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_proxy_checker(self):
        threading_count = 0
        print('- Task has been activated! (Checking proxies..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in proxies:
            threading_count +=1
            threading.Thread(target=self.check_proxy, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def check_verified(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                check = session.get('https://accountsettings.roblox.com/v1/email').json()['verified']
                if check == True:
                    open('output/verified_cookies.txt', 'a').write(cookie+'\n')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_verified_checker(self):
        threading_count = 0
        print('- Task has been activated! (Checking for verified cookies..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.check_verified, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def change_display_name(self, cookie, display_name):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                userid = session.get('https://users.roblox.com/v1/users/authenticated').json()['id']
                change = session.patch(f'https://users.roblox.com/v1/users/{userid}/display-names', json={'newDisplayName':display_name})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
        
    def select_display_name_bot(self):
        print('- Enter Display Name: ')
        display_name = input('>>> ')
        threading_count = 0
        print('- Task has been activated! (Changing cookies Display Name..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.change_display_name, args=(x,display_name,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()

    def change_description(self, cookie, description):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                change = session.post('https://accountinformation.roblox.com/v1/description', data={'description':description})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_desc_bot(self):
        print('- Enter Target Description: ')
        desc = input('>>> ')
        threading_count = 0
        print('- Task has been activated! (Changing cookies Desc...)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.change_description, args=(x,desc,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def change_gender(self, cookie, gender):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                change = session.post('https://accountinformation.roblox.com/v1/gender', data={'gender':gender})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_change_gender(self):
        print('- Select a Gender to Change: (1: None, 2: Male, 3:Women)')
        gender = input('>>> ')
        gender = int(gender)
        threading_count = 0
        print('- Task has been activated! (Changing cookies Gender...)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.change_gender, args=(x,gender,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def change_theme(self, cookie, theme):
        try:
            if theme == 1:
                theme = "Dark"
            if theme == 2:
                theme = "Light"
            if theme == 3:
                theme = random.choice(['Light', 'Dark'])
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                change = session.patch('https://accountsettings.roblox.com/v1/themes/user', json={'themeType':theme})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
            
    def select_change_theme(self):
        print('- Select a Theme to Change: (1: Dark, 2: Light, 3: Random)')
        theme = input('>>> ')
        theme = int(theme)
        threading_count = 0
        print('- Task has been activated! (Changing cookies Theme...)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.change_theme, args=(x,theme,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def change_country(self, cookie, countryId):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                change = session.post('https://www.roblox.com/account/settings/account-country', json={'countryId':countryId})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_change_country(self):
        print('- Enter a Country ID: ')
        countryID = input('>>> ')
        countryID = int(countryID)
        threading_count = 0
        print('- Task has been activated! (Changing cookies country...)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.change_country, args=(x,countryID,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()

    def change_social_networks(self, cookie, yt, twitch, facebook, twitter):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                change = session.post('https://accountinformation.roblox.com/v1/promotion-channels', json={'promotionChannelsVisibilityPrivacy':'AllUsers', 'twitch':twitch, 'twitter':twitter, 'facebook':facebook, 'youtube':yt})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_change_social(self):
        print('- Enter Youtube URL: (Leave blank if not wanted)')
        yt = input('>>> ')
        print('- Enter Twitch URL: (Leave blank if not wanted)')
        twitch = input('>>> ')
        print('- Enter Twitter URL: (Leave blank if not wanted)')
        twitter = input('>>> ')
        print('- Enter Facebook URL: (Leave blank if not wanted)')
        facebook = input('>>> ')
        threading_count = 0
        print('- Task has been activated! (Changing cookies country...)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.change_country, args=(x,yt,twitch,facebook,twitter,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()

    def check_credit(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                credit = session.get('https://billing.roblox.com/v1/credit').json()
                open('output/credits.txt', 'a').write(f'{credit} +|+ {cookie}\n')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_credit_checker(self):
        threading_count = 0
        print('- Task has been activated! (Checking cookies credit/balance..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.check_credit, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def secure_signout(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                signout = session.post('https://www.roblox.com/authentication/signoutfromallsessionsandreauthenticate', data={'__RequestVerificationToken':''})
                open('output/refreshed_cookies.txt', 'a').write(cookie + '\n')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')

    def select_secure_signout(self):
        threading_count = 0
        print('- Task has been activated! (Signing out on other devices!)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.secure_signout, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def check_robux(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                balance = session.get('https://api.roblox.com/my/balance').json()['robux']
                open('output/robux_cookies.txt', 'a').write(f'ROBUX: {balance} |+| {cookie}' + '\n')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_robux_checker(self):
        threading_count = 0
        print('- Task has been activated! (Checking robux on the cookies)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.check_robux, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()

    def select_trade_spammer(self):
        print('- Feature currently disabled or broken? (5)..')
        time.sleep(5)
        quit()

    def buy_model(self, cookie, modelID, userID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                info = session.post('https://catalog.roblox.com/v1/catalog/items/details',headers={'Content-Type':'application/json', 'Accept':'application/json'} ,data='{"items":[{"itemType":"Asset", "id":'+ f'"{modelID}"'+'}]}')
                productId = info.json()['data'][0]['productId']
                expected_price = 0
                currency = 1
                session.post(f'https://economy.roblox.com/v1/purchases/products/{productId}', data={'expectedCurrency':currency, 'expectedPrice':expected_price, 'expectedSellerId':userID})
                session.post('https://www.roblox.com/asset/delete-from-inventory', data={'assetId':modelID})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
                
    def select_buy_model(self):
        threading_count = 0
        print('- Enter a model ID: ')
        modelID = input('>>> ')
        modelID = int(modelID)
        print('- Enter a user ID: ')
        userID = input('>>> ')
        userID = int(userID)
        print('- Task has been activated! (Buying models)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.buy_model, args=( x, modelID, userID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
                
    def favorite(self, cookie, assetID, type):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                if type == "asset".lower():
                    data = {
                        'itemTargetId': f'{assetID}',
                        'favoriteType': 'Asset'
                    }
                    session.post('https://www.roblox.com/v2/favorite/toggle', data=data)
                elif type == "game".lower():
                    universeID = requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={assetID}').json()["UniverseId"]
                    data = {
                        "isFavorited": True
                    }
                    session.post(f'https://games.roblox.com/v1/games/{universeID}/favorites', data=data)
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
                
    def select_favorite(self):
        threading_count = 0
        print('- Enter favorite type (Game or Asset): ')
        type = input('>>> ')
        if not type.lower() == "game" and not type.lower() == "asset":
            print('- Invalid Type!')
            time.sleep(2)
            exit()
        print(f"- Enter the {type}'s ID: ")
        favoriteID = input('>>> ')
        print('- Task has been activated! (Adding favorites)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.favorite, args=( x, favoriteID, type)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)

        quit()
                
    def friend_req(self, cookie, userID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                session.post(f'https://friends.roblox.com/v1/users/{userID}/request-friendship')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_friend_req(self):
        threading_count = 0
        print('- Enter a user ID: ')
        userID = input('>>> ')
        userID = int(userID)
        print('- Task has been activated! (Sending friend requests)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.friend_req, args=( x, userID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
        
    def send_pm(self, cookie, userID, subject, body):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                prox = random.choice(proxies)
                proxy = {'http':prox, 'https':prox}
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                data = {
                    "userId": userID,
                    "subject": subject,
                    "body": body
                }
                session.post('https://chat.roblox.com/v1/messages/send', data=data, proxies=proxy)
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_send_pm(self):
        threading_count = 0
        print('- Enter a user ID: ')
        userID = input('>>> ')
        userID = int(userID)
        print('- Enter a PM subject: ')
        subject = input('>>> ')
        print('- Enter a PM body: ')
        body = input('>>> ')
        print('- Task has been activated! (Sending PMs)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.send_pm, args=( x, userID, subject, body)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def select_username_gen(self):
        # idk how lol
        print('- Feature currently disabled or broken? (5)..')
        time.sleep(5)
        quit()
    
    def select_proxy_scraper(self):
        try:
            print('- Task has been activated! (Scraping proxies)..)')
            print(f'+ (Window will close once finished)')
            open('output/scraped_proxies.txt', 'a').close()
            open('output/scraped_proxies.txt', 'r+').truncate(0)
            with requests.session() as session:
                proxs = session.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
                proxsList = list(proxs.text.splitlines())
                for x in range(len(proxsList)):
                    open('output/scraped_proxies.txt', 'a').write(proxsList[x] + '\n')
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_limited_sniper(self):
        # idk how lol
        print('- Feature currently disabled or broken? (5)..')
        time.sleep(5)
        quit()

    def online_bot(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                session.post('https://presence.roblox.com/v1/presence/register-app-presence')
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_online_bot(self):
        print('- Task has been activated! (Online-ifying all the cookies)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.online_bot, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def visit_bot(self, cookie, gameid):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                token = session.post('https://auth.roblox.com/v1/authentication-ticket/', headers={'referer':f'https://www.roblox.com/games/{gameid}'}).headers['rbx-authentication-ticket']
                browserId = random.randint(1000000, 10000000)
                subprocess.Popen(f"start roblox-player:1+launchmode:play+gameinfo:{token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameid}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:", shell=True)
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_visit_bot(self):
        print("- This feature launches on your PC")
        print('- Enter a game ID: ')
        gameID = input('>>> ')
        gameID = int(gameID)
        print('- Task has been activated! (Visiting games)..)')
        time.sleep(2)
        print(f'+ (CTRL-C to exit (Will run forever))')
        while True:
            threading.Thread(target=self.visit_bot, args=( random.choice(cookies), gameID)).start()
            time.sleep(5)
    
    def equip_bot(self, cookie, assetID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                session.post(f'https://avatar.roblox.com/v1/avatar/assets/{assetID}/wear')
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
                
    def select_equip_bot(self):
        print('- Enter an asset ID: ')
        assetID = input('>>> ')
        assetID = int(assetID)
        print('- Task has been activated! (Equipping assets)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.equip_bot, args=( x, assetID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def unequip_bot(self, cookie, assetID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                session.post(f'https://avatar.roblox.com/v1/avatar/assets/{assetID}/remove')
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_unequip_bot(self):
        print('- Enter an asset ID: ')
        assetID = input('>>> ')
        assetID = int(assetID)
        print('- Task has been activated! (Unequipping assets)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.unequip_bot, args=( x, assetID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def buy_asset(self, cookie, assetID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                info = session.post('https://catalog.roblox.com/v1/catalog/items/details', headers={'Content-Type':'application/json', 'Accept':'application/json'} ,data='{"items":[{"itemType":"Asset", "id":'+ f'"{assetID}"'+'}]}')
                productId = info.json()['data'][0]['productId']
                expected_price = info.json()['data'][0]['price']
                currency = 1
                session.post(f'https://economy.roblox.com/v1/purchases/products/{productId}', data={'expectedCurrency':currency, 'expectedPrice':expected_price, 'expectedSellerId':1})
                
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
                
    def select_buy_asset(self):
        print('- Enter an asset ID: ')
        assetID = input('>>> ')
        assetID = int(assetID)
        print('- Task has been activated! (Unequipping assets)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.buy_asset, args=( x, assetID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def report_bot(self, cookie, userID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                __RequestVerificationToken = session.get(f'https://www.roblox.com/abusereport/userprofile?id={userID}').cookies.get('__RequestVerificationToken')
                session.post(f'https://www.roblox.com/abusereport/userprofile?id={userID}&redirecturl=https%3a%2f%2fwww.roblox.com%2fusers%2f{userID}%2fprofile', data={'__RequestVerificationToken':__RequestVerificationToken, 'ReportCategory':1, 'Comment':'', 'Id':userID, 'RedirectUrl':f'https://www.roblox.com/abusereport/userprofile?id={userID}', 'PartyGuid':'', 'ConversationId':''})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_report_bot(self):
        print('- Enter a user ID: ')
        userID = input('>>> ')
        userID = int(userID)
        print('- Task has been activated! (Reporting player)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.report_bot, args=( x, userID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def group_ally(self, cookie, groupID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                target = random.randint(1, 9342195)
                session.post(f'https://groups.roblox.com/v1/groups/{groupID}/relationships/allies/{target}')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_group_ally(self):
        print('- Enter a group ID: ')
        groupID = input('>>> ')
        groupID = int(groupID)
        print('- Task has been activated! (Sending group allies)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.group_ally, args=( x, groupID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def cookie_killer(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                session.post('https://auth.roblox.com/v2/logout')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_cookie_killer(self):
        print("- Are you sure you want to kill all the cookies? (Ctrl-C to cancel, Enter key to continue)")
        input('>>> ')
        print('- Task has been activated! (Killing cookies)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.cookie_killer, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def desc_checker(self, cookie, desc):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                session.post('https://accountinformation.roblox.com/v1/description', data={'description':desc})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_desc_checker(self):
        print("- Enter a description: ")
        desc = input(">>> ")
        print('- Task has been activated! (Changing descriptions)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.desc_checker, args=( x, desc)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def game_join(self, cookie, gameID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                token = session.post('https://auth.roblox.com/v1/authentication-ticket/', headers={'referer':f'https://www.roblox.com/games/{gameID}'}).headers['rbx-authentication-ticket']
                browserId = random.randint(1000000, 10000000)
                subprocess.Popen(f"start roblox-player:1+launchmode:play+gameinfo:{token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameID}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:", shell=True)
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_game_join(self):
        print("- Enter a game id: ")
        gameID = input(">>> ")
        gameID = int(gameID)
        print('- Task has been activated! (Joining game)..)')
        time.sleep(2)
        threading.Thread(target=self.game_join, args=( random.choice(cookies), gameID)).start()
        quit()
    def random_avatar(self, cookie):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                userID = session.get('https://users.roblox.com/v1/users/authenticated').json()['id']
                shirt = random.choice(session.get(f'https://www.inventory.roblox.com/v1/users/{userID}/inventory/Shirt?pageNumber=1&itemsPerPage=100000').json()['data'])
                hat = random.choice(session.get(f'https://www.inventory.roblox.com/v1/users/{userID}/inventory/Hat?pageNumber=1&itemsPerPage=100000').json()['data'])
                pants = random.choice(session.get(f'https://www.inventory.roblox.com/v1/users/{userID}/inventory/Pants?pageNumber=1&itemsPerPage=100000').json()['data'])
                face = pants = random.choice(session.get(f'https://www.inventory.roblox.com/v1/users/{userID}/inventory/Face?pageNumber=1&itemsPerPage=100000').json()['data'])
                head = random.choice(session.get(f'https://www.inventory.roblox.com/v1/users/{userID}/inventory/Head?pageNumber=1&itemsPerPage=100000').json()['data'])
                avatarList = [shirt, hat, pants, face, head]
                session.post(f'https://avatar.roblox.com/v1/avatar/set-wearing-assets', data={"assetIds": avatarList})
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_random_avatar(self):
        threading_count = 0
        print('- Task has been activated! (Randomizing cookie avatars)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.random_avatar, args=( x,)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    def select_cookie_gen(self):
        #idk how lol
        print('- Feature currently disabled or broken? (5)..')
        time.sleep(5)
        quit()
    
    def select_group_join(self):
        #idk how lol
        print('- Feature currently disabled or broken? (5)..')
        time.sleep(5)
        quit()
    
    def game_follow(self, cookie, gameID):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
                userID = session.get('https://users.roblox.com/v1/users/authenticated').json()['id']
                universeID = session.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={gameID}')
                session.post(f'https://followings.roblox.com/v1/users/{userID}/universes/{universeID}')
        except Exception as error:
            if optional_settings.settings['log_errors'] == True:
                open('errors/errors.txt', 'a').write(str(error) + '\n\n')
    
    def select_game_follow(self):
        threading_count = 0
        print('- Enter a game id: ')
        gameID = input('>>> ')
        gameID = int(gameID)
        print('- Task has been activated! (Following the game)..)')
        time.sleep(2)
        thread_amt = optional_settings.settings['threads']
        print(f'+ (Window will close once finished) | Running {thread_amt}/sec')
        for x in cookies:
            threading_count +=1
            threading.Thread(target=self.game_follow, args=( x, gameID)).start()
            if threading_count >= thread_amt:
                threading_count = 0
                time.sleep(1)
        quit()
    
    def select_follow_bot(self):
        #idk how lol
        print('- Feature currently disabled or broken? (5)..')
        time.sleep(5)
        quit()
                
                
class menu():
    def __init__(self):
        pass
    
    def paid_menu():
        print(': Welcome to PLUG Multi-Purpose Tool\n')
        print('███████████████████████████████████████████████████████████████████████████')
        print('''
 ██▓███   ██▓     █    ██   ▄████ 
▓██░  ██▒▓██▒     ██  ▓██▒ ██▒ ▀█▒
▓██░ ██▓▒▒██░    ▓██  ▒██░▒██░▄▄▄░
▒██▄█▓▒ ▒▒██░    ▓▓█  ░██░░▓█  ██▓
▒██▒ ░  ░░██████▒▒▒█████▓ ░▒▓███▀▒
▒▓▒░ ░  ░░ ▒░▓  ░░▒▓▒ ▒ ▒  ░▒   ▒ 
░▒ ░     ░ ░ ▒  ░░░▒░ ░ ░   ░   ░ 
░░         ░ ░    ░░░ ░ ░ ░ ░   ░ 
             ░  ░   ░           ░
        ''')
        print('███████████████████████████████████████████████████████████████████████████')
        print('''
(1) - Cookie Checker    (2) - Proxy Checker     (3) - Verified Checker
(4) - Display Name Bot  (5) - Desc Change Bot   (6) - Gender Change
(7) - Dark/Light Change (8) - Location Change   (9) - Social Networks Change
(10) - Credit Checker   (11) - Cookie Refresher (12) - Robux Checker
(X) - Trade Spammer     (14) - Model Buy Bot    (15) - Favorite Bot
(16) - Friend Req Bot   (17) - PM Spammer       (X) - Username Gen
(19) - Proxy Scraper    (X) - Limited Sniper   (21) - Online Bot
(22) - Visit Bot        (23) - Equip Bot        (24) - Unequip Bot
(25) - Asset Buyer      (26) - Report Bot       (27) - Group Ally Bot
(28) - Cookie Killer    (29) - Desc Checker     (30) - Game Join
(31) - Random Avatar    (X) - Cookie Gen       (X) - Group Join Bot
(34) - Game Follow Bot  (X) - Follow Bot      
        ''') 
        print('███████████████████████████████████████████████████████████████████████████')
        selected = input('>>> ')
        selection_features = features()
        selections = [selection_features.select_cookie_checker, selection_features.select_proxy_checker, selection_features.select_verified_checker, selection_features.select_display_name_bot, selection_features.select_desc_bot, selection_features.select_change_gender, selection_features.select_change_theme, selection_features.select_change_country, selection_features.select_change_social, selection_features.select_credit_checker, selection_features.select_secure_signout, selection_features.select_robux_checker, selection_features.select_trade_spammer, selection_features.select_buy_model, selection_features.select_favorite, selection_features.select_friend_req, selection_features.select_send_pm, selection_features.select_username_gen, selection_features.select_proxy_scraper, selection_features.select_limited_sniper, selection_features.select_online_bot, selection_features.select_visit_bot, selection_features.select_equip_bot, selection_features.unequip_bot, selection_features.select_buy_asset , selection_features.select_report_bot, selection_features.select_group_ally, selection_features.select_cookie_killer, selection_features.select_desc_bot, selection_features.select_game_join, selection_features.select_random_avatar, selection_features.select_cookie_gen, selection_features.select_group_join, selection_features.select_game_follow, selection_features.select_follow_bot]
        selections[int(selected) - 1]()

run = menu
run.paid_menu()

