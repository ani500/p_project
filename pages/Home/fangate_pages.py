import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging
from pages.Home.login_pages import LoginPage


class FangatePage(SeleniumDriver):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Locators
    _dev_unlock_password = "//form[@id='devlock']//input[@type='password']"
    _dev_unlock_button = "//div[@class='form-group']//button[@type='submit']"
    _login_link = "Login"
    _email_field = "login_email"
    _password_field = "login_password"
    _login_button = "login_button"
    _stats_visits = "stats_visit_total"
    # Locators Fangate
    _share_music_link = "Share Music"
    _download_gate_button = "//a[@href='https://dev2.hypeddit.com/gate/create']"
    # source Section
    _track_url = "track_url"
    _source_next_button = "next_box1_button"
    # Genre Section
    _genre_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select genre']"
    _select_genre = "//ul[@class='dropdown-menu inner']//span[text()='Bass']"
    _genre_next_button = "next_box2_button"
    # Upload Section
    _choose_file = "inputFilemp3"
    _upload_next_button = "next_box3_button"
    # Title Section
    _artist_name = "artist_name"
    _track_title = "track_title"
    _title_next_button = "next_box4_button"
    # Design Section
    _upload_coverart_button = "selectManualCoverart"
    _dark_theme_radio_button = "//div[@class='checkbox']//label[@for='dark_theme']"
    _design_next_button = "next_box5_button"

    # Gate Steps Section

    _add_soundcloud_step = "add_soundcloud_button"
    _follow_profile = "//div[@class='checkbox']//label[@for='follow_sc']"
    _follow_sc_id = "follow_sc"
    _comment_sc = "//div[@class='checkbox']//label[@for='comment_sc']"
    _comment_sc_id = 'comment_sc'
    _like_sc = "//div[@class='checkbox']//label[@for='like_sc']"
    _like_sc_id = "like_sc"
    _repost_sc = "//div[@class='checkbox']//label[@for='repost_sc']"
    _repost_sc_id = "repost_sc"
    _skippable_sc = "//div[@class='checkbox']//label[@for='skippable_sc']"
    _skippable_sc_id = "skippable_sc"
    _add_scoundcloud_artist = "add_soundcloud_artist"
    _add_soundcloud_track = "add_soundcloud_track"
    _gate_step_next_button = "next_box6_button"
    # -------------------Youtube------------------
    _add_youtube_step = "add_youtube_button"
    _subscribe_yt_id = "subscribe_yt"
    _subscribe_yt = "//div[@class='checkbox']//label[@for='subscribe_yt']"
    _skippable_yt_id = "skippable_yt"
    _skippable_yt = "//div[@class='checkbox']//label[@for='skippable_yt']"
    _add_channel_yt_url = "add_youtube_channel_custom_url"
    _add_channel_yt_name = "add_youtube_channel_custom_name"
    # ---------------------xxxx------------------------------------------
    #------------------------Spotify------------------------------------
    _add_spotify_step = "add_spotify_button"
    _follow_sp_id = "follow_sp"
    _follow_sp = "//div[@class='checkbox']//label[@for='follow_sp']"
    _save_sp_id = "save_track_sp"
    _save_sp = "//div[@class='checkbox']//label[@for='save_track_sp']"
    _skippable_sp_id = "skippable_sp"
    _skippable_sp = "//div[@class='checkbox']//label[@for='skippable_sp']"
    _add_artist_sp = "add_spotify_artist"
    _add_track_sp = "add_spotify_track"

    #--------------------------Apple Step-----------------------------------------

    _add_apple_step = "add_apple_button"
    _like_ap_id = "like_ap"
    _like_ap = "//div[@class='checkbox']//label[@for='like_ap']"
    _save_ap_id = "save_track_ap"
    _save_ap = "//div[@class='checkbox']//label[@for='save_track_ap']"
    _skippable_ap_id = "skippable_ap"
    _skippable_ap = "//div[@class='checkbox']//label[@for='skippable_ap']"
    _add_artist_ap = "add_apple_artist"

    # ----------------------------Deezer Step------------------------
    _add_deezer_step = "add_deezer_button"
    _follow_dz_id = "follow_dz"
    _follow_dz = "//div[@class='checkbox']//label[@for='follow_dz']"
    _save_dz_id = "save_track_dz"
    _save_dz = "//div[@class='checkbox']//label[@for='save_track_dz']"
    _skippable_dz_id = "skippable_dz"
    _skippable_dz = "//div[@class='checkbox']//label[@for='skippable_dz']"
    _add_artist_dz = "add_deezer_artist"
    _add_track_dz = "add_deezer_track"

    #----------------Mixcloud Step------------------------------------

    _add_mixcloud_step = "add_mixcloud_button"
    _follow_mc_id = "follow_mc"
    _follow_mc = "//div[@class='checkbox']//label[@for='follow_mc']"
    _repost_mc_id = "repost_mc"
    _repost_mc = "//div[@class='checkbox']//label[@for='repost_mc']"
    _like_mc_id = "like_mc"
    _like_mc = "//div[@class='checkbox']//label[@for='like_mc']"
    _skippable_mc_id = "skippable_mc"
    _skippable_mc = "//div[@class='checkbox']//label[@for='skippable_mc']"
    _add_artist_mc = "add_mixcloud_artist"
    _add_track_mc = "add_mixcloud_track"

    # -----------------------twitter step--------------------------------

    _add_twitter_step = "add_twitter_button"
    _follow_tw_id = "follow_tw"
    _follow_tw = "//div[@class='checkbox']//label[@for='follow_tw']"
    _share_tw_id = "share_tw"
    _share_tw = "//div[@class='checkbox']//label[@for='share_tw']"
    _skippable_tw_id = "skippable_tw"
    _skippable_tw = "//div[@class='checkbox']//label[@for='skippable_tw']"
    _add_profile_tw = "add_twitter"

    # -----------------------Twitch---------------------------------------

    _add_twitch_step = "add_twitch_button"
    _follow_th_id = "follow_th"
    _follow_th = "//div[@class='checkbox']//label[@for='follow_th']"
    _subscribe_th_id = "subscribe_th"
    _subscribe_th = "//div[@class='checkbox']//label[@for='subscribe_th']"
    _skippable_th_id = "skippable_th"
    _skippable_th = "//div[@class='checkbox']//label[@for='skippable_th']"
    _add_artist_th = "add_twitch_artist"
    #-------------------Messenger Step ----------------------------

    _add_fb_msgr_step = "add_facebook_msgr_button"
    _subscribe_fb_msgr_id = "subscribe_fb_msgr"
    _subscribe_fb_msgr = "//div[@class='checkbox']//label[@for='subscribe_fb_msgr']"
    _skippable_fb_msgr_id = "skippable_fb_msgr"
    _skippable_fb_msgr = "//div[@class='checkbox']//label[@for='skippable_fb_msgr']"
    _chatbot_platform_caret_fb_msgr = "//button[@class='btn dropdown-toggle btn-default']//span[text()='No chatbot selected']"
    _select_chatbot_fb_msgr = "//div[@class='dropdown-menu open']//span[text()='ManyChat']"
    _add_page_fb_msgr = "add_facebook_msgr"

    #--------------------------Facebook step --------------------------------

    _add_facebook_step = "add_facebook_button"
    _share_fb_id = "share_fb"
    _share_fb = "//div[@class='checkbox']//label[@for='share_fb']"
    _like_fb_id = "like_fb"
    _like_fb = "//div[@class='checkbox']//label[@for='like_fb']"
    _skippable_fb_id = "skippable_fb"
    _skippable_fb = "//div[@class='checkbox']//label[@for='skippable_fb']"
    _add_page_fb = "add_facebook"
    #------------------------------------Instagram step-------------------
    _add_instagram_step = "add_instagram_button"
    _follow_ig_id = "follow_ig"
    _follow_ig = "//div[@class='checkbox']//label[@for='follow_ig']"
    _skippable_ig_id = "skippable_ig"
    _skippable_ig = "//div[@class='checkbox']//label[@for='skippable_ig']"
    _add_profile_ig = "add_instagram"

    # ------------------------------------Tiktok step-------------------
    _add_tiktok_step = "add_tiktok_button"
    _follow_tk_id = "follow_tk"
    _follow_tk = "//div[@class='checkbox']//label[@for='follow_tk']"
    _skippable_tk_id = "skippable_tk"
    _skippable_tk = "//div[@class='checkbox']//label[@for='skippable_tk']"
    _add_profile_tk = "add_tiktok"

    # ------------------------------------Bandcamp step-------------------
    _add_bandcamp_step = "add_bandcamp_button"
    _follow_bc_id = "follow_bc"
    _follow_bc = "//div[@class='checkbox']//label[@for='follow_bc']"
    _skippable_bc_id = "skippable_bc"
    _skippable_bc = "//div[@class='checkbox']//label[@for='skippable_bc']"
    _add_profile_bc = "add_bandcamp"

    # ------------------------------------Donation step-------------------
    _add_donation_step = "add_donation_button"
    _add_donation = "donation_id"

    #------------------------------------------------------------------------

    # Link Url Section
    _edit_custom_link = "edit_custom_link"
    _page = "custom_link_artist"
    _optional = "custom_link_title"
    _linkUrl_next_button = "next_panel_custom_link"
    # Release Settings Section
    # Release Settings Section
    _set_newRelease_public = "//div[@class='checkbox']//label[@for='set_newrelease_public']"
    _set_newRelease = "//div[@class='checkbox']//label[@for='set_newrelease']"
    _release_settings_button = "next_newreleases_panel"
    # Email Promotion Section
    _email_promotion_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Please select music']"
    _select_fangate = "//div[@class='dropdown-menu open']//span[text()='Automatically email my newest download gate']"
    _email_promotion_next_button = "next_box9_button"
    # Tracking Pixels Section
    _facebook_pixel = "facebook_pixel"
    _facebook_pixel_token = "facebook_pixel_token"
    _google_pixel = "google_pixel"
    _google_pixel_label = "google_pixel_label"
    _tracking_pixels_next_button = "gate_custom_fbpixel_button"
    # Confirmation Section
    _create_fangate_button = "btn_create_fangate"

    def clickOnTheLink(self):
        self.elementClick(self._login_link, "link")

    def emailSendKeys(self, email):
        self.sendKeys(email, self._email_field)

    def passwordSendKeys(self, password):
        self.sendKeys(password, self._password_field)

    def clickOnTheLoginButton(self):
        self.elementClick(self._login_button)

    def clickShareMusicLink(self):
        self.elementClick(self._share_music_link, "link")

    def clickGateCreateLink(self):
        self.elementClick(self._download_gate_button, "xpath")

    def trackUrlSendKeys(self, trackurl):
        self.sendKeys(trackurl, self._track_url)

    def clickOnNextSource(self):
        self.elementClick(self._source_next_button)

    def clickOnGenreCaret(self):
        self.elementClick(self._genre_caret, "xpath")

    def selectGenre(self, ):
        self.elementClick(self._select_genre, "xpath")

    def clickOnNextGenre(self):
        self.elementClick(self._genre_next_button)

    def uploadTrack(self):
        self.sendKeys("C:\\Users\\Anil\\workspace_python\\hypeddit-Project\\Files\\2sec.mp3", self._choose_file)

    def clickOnNextUpload(self):
        self.elementClick(self._upload_next_button)

    def artistNameSendKeys(self, artistname):
        self.sendKeys(artistname, self._artist_name)

    def artistTitleSendKeys(self, artisttitle):
        self.sendKeys(artisttitle, self._track_title)

    def clickOnNextTitle(self):
        self.elementClick(self._title_next_button)

    def uploadImage(self):
        self.elementClick(self._upload_coverart_button)

    def clickDarkScheme(self):
        self.elementClick(self._dark_theme_radio_button, "xpath")

    def clickOnNextDesign(self):
        self.elementClick(self._design_next_button)

    def clickScStep(self):
        self.elementClick(self._add_soundcloud_step, "xpath")

    def clickScFollow(self):
        # self.elementClick(self._follow_profile, "xpath")
        self.checkRadioElementClick(self._follow_profile, "xpath", self._follow_sc_id)

    def clickScComment(self):
        self.checkRadioElementClick(self._comment_sc, "xpath", self._comment_sc_id)

    def clickScLike(self):
        self.checkRadioElementClick(self._like_sc, "xpath", self._like_sc_id)

    def clickScRepost(self):
        self.checkRadioElementClick(self._repost_sc, "xpath", self._repost_sc_id)

    def clickScSkippable(self):
        self.checkRadioElementClick(self._skippable_sc, "xpath", self._skippable_sc_id)

    def profileScSendKeys(self, profile):
        self.sendKeys(profile, self._add_scoundcloud_artist)

    def trackScSendKeys(self, track):
        self.sendKeys(track, self._add_soundcloud_track)

    def clickYtStep(self):
        self.elementClick(self._add_youtube_step)

    def clickYtSubscribe(self):
        self.checkRadioElementClick(self._subscribe_yt, "xpath", self._subscribe_yt_id)

    def clickYtSkippable(self):
        self.checkRadioElementClick(self._skippable_yt, "xpath", self._skippable_yt_id)

    def ytChannelSendKeys(self,url):
        self.sendKeys(url, self._add_channel_yt_url)

    def ytChannelNameSendKeys(self, cName):
        self.sendKeys(cName, self._add_channel_yt_name)

    # ------------------------------xxx-------------------------------


    def clickOnNextGateSteps(self):
        self.elementClick(self._gate_step_next_button)

    def editCustomLink(self):
        self.elementClick(self._edit_custom_link)

    def pageSendKeys(self, pagename):
        self.sendKeys(pagename, self._page)

    def optionalSendKeys(self, optional):
        self.sendKeys(optional, self._optional)

    def clickOnNextLinkUrl(self):
        self.elementClick(self._linkUrl_next_button)

    def clickPublic(self):
        self.elementClick(self._set_newRelease_public, "xpath")

    def clickNewRelease(self):
        self.elementClick(self._set_newRelease, "xpath")

    def clickOnNextReleaseSettings(self):
        self.elementClick(self._release_settings_button)

    def clickOnEmailPromotionCaret(self):
        self.elementClick(self._email_promotion_caret, "xpath")

    def selectFangate(self):
        self.elementClick(self._select_fangate, "xpath")

    def clickOnNextEmailPromotion(self):
        self.elementClick(self._email_promotion_next_button)

    def facebookPixelSendKeys(self, fbpixel):
        self.sendKeys(fbpixel, self._facebook_pixel)

    def facebookTokenSendKeys(self, fbtoken):
        self.sendKeys(fbtoken, self._facebook_pixel_token)

    def clickOnNextTrackingPixels(self):
        self.elementClick(self._tracking_pixels_next_button)

    def clickOnCreate(self):
        self.elementClick(self._create_fangate_button)

    def waitFor(self):
        self.waitForElement(self._dark_theme_radio_button)

    def devUnlockPasswordSendkeys(self, passwordtext):
        self.sendKeys(passwordtext, self._dev_unlock_password, "xpath")

    def devUnlockbuttonClick(self):
        self.elementClick(self._dev_unlock_button, "xpath")

    def login(self, email="", password=""):
        self.driver.get("https://dev2.hypeddit.com")
        time.sleep(10)
        self.driver.get("https://dev2.hypeddit.com")
        self.clickOnTheLink()
        self.clearFields()
        self.emailSendKeys(email)
        self.passwordSendKeys(password)
        self.clickOnTheLoginButton()
        time.sleep(10)

    def createFangate(self, artistname="sunil", trackurl="https://soundcloud.com/makelogin/sleep-away",
                      artisttitle="verma", fbpixel=7, fbtoken=8):
        time.sleep(5)
        self.clickShareMusicLink()
        time.sleep(5)
        self.clickGateCreateLink()

        self.source(trackurl)
        time.sleep(2)
        self.genre()
        time.sleep(2)
        self.upload()
        time.sleep(2)
        self.title(artistname, artisttitle)
        time.sleep(2)
        self.design()
        self.gateSteps()
        time.sleep(2)
        self.linkUrl()
        time.sleep(2)
        self.releaseSettings()
        time.sleep(2)
        self.emailPromotion()
        time.sleep(2)
        self.trackingPixels(fbpixel, fbtoken)
        time.sleep(2)
        self.confirmation()
        time.sleep(2)

    def clearFields(self):
        element = self.getElement(self._email_field)
        element.clear()

        element = self.getElement(self._password_field)
        element.clear()

    def devUnlock(self, unlockpassword="testdev123"):
        self.devUnlockPasswordSendkeys(unlockpassword)
        self.devUnlockbuttonClick()

    def source(self, trackurl):
        self.trackUrlSendKeys(trackurl)
        time.sleep(1)
        self.clickOnNextSource()

    def genre(self):
        self.clickOnGenreCaret()
        time.sleep(1)
        self.selectGenre()
        time.sleep(1)
        self.clickOnNextGenre()

    def upload(self):
        self.uploadTrack()
        time.sleep(3)
        self.clickOnNextUpload()

    def title(self, artistname, artisttitle):
        self.artistNameSendKeys(artistname)
        time.sleep(1)
        self.artistTitleSendKeys(artisttitle)
        time.sleep(1)
        self.clickOnNextTitle()

    def design(self):
        # Skip Coverart
        # self.waitFor()
        self.clickDarkScheme()
        time.sleep(1)
        self.clickOnNextDesign()

    def gateSteps(self):
        # self.clickScStep()
        time.sleep(3)
        self.clickScFollow()
        time.sleep(3)
        self.clickScComment()
        time.sleep(3)
        self.clickScLike()
        time.sleep(3)
        self.clickScRepost()
        time.sleep(3)
        self.clickScSkippable()

        # Skip Profile SC
        # Skip Title SC


    # --------------------Youtube Step---------------------------
        time.sleep(3)
        self.clickYtStep()
        time.sleep(3)
        self.clickYtSubscribe()
        self.clickYtSkippable()
        self.ytChannelSendKeys("https://www.youtube.com/user/DoctoresseBonneto")
        self.ytChannelNameSendKeys("Cname")
        time.sleep(3)
        self.clickOnNextGateSteps()
        time.sleep(1)
        self.clickOnNextGateSteps()

        #-------------------------------Spotify Step --------------------------

        time.sleep(3)
        self.clickSpStep()
        time.sleep(3)
        self.clickSpFollow()
        self.clickSpSave()
        self.clickSpSkippable()
        self.ytChannelSendKeys("https://www.youtube.com/user/DoctoresseBonneto")
        self.ytChannelNameSendKeys("Cname")
        time.sleep(3)
        self.clickOnNextGateSteps()
        time.sleep(1)
        self.clickOnNextGateSteps()


    def linkUrl(self):
        # Skip Edit Custom Url
        # skip page text Edit
        # skip optional Edit
        self.clickOnNextLinkUrl()


    def releaseSettings(self):
        # self.clickPublic()
        time.sleep(1)
        self.clickNewRelease()
        time.sleep(1)
        self.clickOnNextReleaseSettings()

    def emailPromotion(self):
        self.clickOnEmailPromotionCaret()
        time.sleep(1)
        self.selectFangate()
        time.sleep(1)
        self.clickOnNextEmailPromotion()

    def trackingPixels(self, fbpixel, fbtoken):
        self.facebookPixelSendKeys(fbpixel)
        time.sleep(1)
        self.facebookTokenSendKeys(fbtoken)
        time.sleep(1)
        self.clickOnNextTrackingPixels()

    def confirmation(self):
        self.clickOnCreate()
