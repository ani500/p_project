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
    _link_gate_button = "//a[@href='https://dev2.hypeddit.com/gate/create/url']"
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
    # -------------------Email------------------

    _add_email_step ="add_email_button"
    _collect_email_id ="collect_email"
    _collect_email = "//div[@class='checkbox']//label[@for='collect_email']"
    _collect_email_names_id = "collect_email_names"
    _collect_email_names = "//div[@class='checkbox']//label[@for='collect_email_names']"
    _skippable_email_id = "skippable_email"
    _skippable_email = "//div[@class='checkbox']//label[@for='skippable_email']"

    # -------------------Soundcloud------------------

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
    _yt_profile_add_button = "youtube_profile_add_button"
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

    # -----------------------Link Gate section----------------
    # Title Step
    _link_artist_name = "artist_name"
    _link_title = "track_title"
    _link_titleSection_next_button = "next_box4_button"

    # Secret Link Step
    _link_custom_redir_url = "custom_redirection_url"
    _link_SecretLink_next_button ="gate_secret_link_button"
    # Unlock Button Text Step
    _link_button_text_dropdown = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select button text']"
    _link_menu_select_dropdown = "//div[@class='dropdown-menu open']//span[text()='Download']"
    _link_unlock_button_next_button = "next_box2_button"

    # Design Section
    _choose_coverart = "inputManualCoverart"

    # Confirmation Section Link gate
    _create_linkgate_button = "btn_create_linkgate"

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

    def clickLinkgateLink(self):
        self.elementClick(self._link_gate_button, "xpath")

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

    def clickEmCollect(self):
        self.checkRadioElementClick(self._collect_email, "xpath", self._collect_email_id)

    def clickEmCollectName(self):
        self.checkRadioElementClick(self._collect_email_names,"xpath", self._collect_email_names_id)

    def clickEmSkippable(self):
        self.checkRadioElementClick(self._skippable_email,"xpath", self._skippable_email_id)


    def clickScStep(self):
        self.elementClick(self._add_soundcloud_step)

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

    def clickYtProfileAddButton(self):
        self.elementClick(self._yt_profile_add_button)

    def clickSpStep(self):
        self.elementClick(self._add_spotify_step)

    def clickSpFollow(self):
        self.checkRadioElementClick(self._follow_sp, "xpath", self._follow_sp_id)

    def clickSpSave(self):
        self.checkRadioElementClick(self._save_sp, "xpath", self._save_sp_id)

    def clickSpSkippable(self):
        self.checkRadioElementClick(self._skippable_sp, "xpath", self._skippable_sp_id)

    def spProfileSendKeys(self, profileSp):
        self.sendKeys(profileSp, self._add_artist_sp)

    def spTrackSendKeys(self, trackSp):
        self.sendKeys(trackSp, self._add_track_sp)

    def clickApStep(self):
        self.elementClick(self._add_apple_step)

    def clickApLike(self):
        self.checkRadioElementClick(self._like_ap, "xpath", self._like_ap_id)

    def clickApSave(self):
        self.checkRadioElementClick(self._save_ap, "xpath", self._save_ap_id)

    def clickApSkippable(self):
        self.checkRadioElementClick(self._skippable_ap, "xpath", self._skippable_ap_id)

    def apTrackSendKeys(self,trackUrlAp):
        self.sendKeys(trackUrlAp,self._add_artist_ap)

    def clickDzStep(self):
        self.elementClick(self._add_deezer_step)

    def clickDzFollow(self):
        self.checkRadioElementClick(self._follow_dz, "xpath", self._follow_dz_id)

    def clickDzSave(self):
        self.checkRadioElementClick(self._save_dz, "xpath", self._save_dz_id)

    def clickDzSkippable(self):
        self.checkRadioElementClick(self._skippable_dz, "xpath", self._skippable_dz_id)

    def dzArtistSendKeys(self, artistUrlDz):
        self.sendKeys(artistUrlDz, self._add_artist_dz)

    def dzTrackSendKeys(self, trackUrlDz):
        self.sendKeys(trackUrlDz, self._add_track_dz)



    def clickMcStep(self):
        self.elementClick(self._add_mixcloud_step)

    def clickMcFollow(self):
        self.checkRadioElementClick(self._follow_mc, "xpath", self._follow_mc_id)

    def clickMcRepost(self):
        self.checkRadioElementClick(self._repost_mc, "xpath", self._repost_mc_id)

    def clickMcLike(self):
        self.checkRadioElementClick(self._like_mc, "xpath", self._like_mc_id)

    def clickMcSkippable(self):
        self.checkRadioElementClick(self._skippable_mc, "xpath", self._skippable_mc_id)

    def mcProfileSendKeys(self, profileUrlMc):
        self.sendKeys(profileUrlMc, self._add_artist_mc)

    def mcTrackSendKeys(self, trackUrlMc):
        self.sendKeys(trackUrlMc, self._add_track_mc)

    def clickTwStep(self):
        self.elementClick(self._add_twitter_step)

    def clickTwFollow(self):
        self.checkRadioElementClick(self._follow_tw, "xpath", self._follow_tw_id)

    def clickTwShare(self):
        self.checkRadioElementClick(self._share_tw, "xpath", self._share_tw_id)

    def clickTwSkippable(self):
        self.checkRadioElementClick(self._skippable_tw, "xpath", self._skippable_tw_id)

    def twProfileSendKeys(self, profileUrlTw):
        self.sendKeys(profileUrlTw, self._add_profile_tw)

    def clickThStep(self):
        self.elementClick(self._add_twitch_step)

    def clickThFollow(self):
        self.checkRadioElementClick(self._follow_th, "xpath", self._follow_th_id)

    def clickThSubscription(self):
        self.checkRadioElementClick(self._subscribe_th, "xpath", self._subscribe_th_id)

    def clickThSkippable(self):
        self.checkRadioElementClick(self._skippable_th, "xpath", self._skippable_th_id)

    def thChannelSendKeys(self, channelUrlTh):
        self.sendKeys(channelUrlTh, self._add_artist_th)

    def clickFbMsgrStep(self):
        self.elementClick(self._add_fb_msgr_step)

    def clickFbMsgrSubscription(self):
        self.checkRadioElementClick(self._subscribe_fb_msgr, "xpath", self._subscribe_fb_msgr_id)

    def clickFbMsgrSkippable(self):
        self.checkRadioElementClick(self._skippable_fb_msgr, "xpath", self._skippable_fb_msgr_id)

    def fbMsgrChatbotSendKeys(self):
        self.elementClick(self._chatbot_platform_caret_fb_msgr, "xpath")
        time.sleep(3)
        self.elementClick(self._select_chatbot_fb_msgr, "xpath")

    def fbMsgrPageSendKeys(self, pageUrlFbMsgr):
        self.sendKeys(pageUrlFbMsgr, self._add_page_fb_msgr)

    def clickIgStep(self):
        self.elementClick(self._add_instagram_step)

    def clickIgFollow(self):
        self.checkRadioElementClick(self._follow_ig, "xpath", self._follow_ig_id)

    def clickIgSkippable(self):
        self.checkRadioElementClick(self._skippable_ig, "xpath", self._skippable_ig_id)

    def igProfileSendKeys(self, profileUrlIg):
        self.sendKeys(profileUrlIg, self._add_profile_ig)

    def clickTkStep(self):
        self.elementClick(self._add_tiktok_step)

    def clickTkFollow(self):
        self.checkRadioElementClick(self._follow_tk, "xpath", self._follow_tk_id)

    def clickTkSkippable(self):
        self.checkRadioElementClick(self._skippable_tk, "xpath", self._skippable_tk_id)

    def tkProfileSendKeys(self, profileUrlTk):
        self.sendKeys(profileUrlTk, self._add_profile_tk)

    def clickBcStep(self):
        self.elementClick(self._add_bandcamp_step)

    def clickBcFollow(self):
        self.checkRadioElementClick(self._follow_bc, "xpath", self._follow_bc_id)

    def clickBcSkippable(self):
        self.checkRadioElementClick(self._skippable_bc, "xpath", self._skippable_bc_id)

    def bcProfileSendKeys(self, profileUrlBc):
        self.sendKeys(profileUrlBc, self._add_profile_bc)

    def clickFbStep(self):
        self.elementClick(self._add_facebook_step)

    def clickFbShare(self):
        self.checkRadioElementClick(self._share_fb, "xpath", self._share_fb_id)

    def clickFbLike(self):
        self.checkRadioElementClick(self._like_fb, "xpath", self._like_fb_id)

    def clickFbSkippable(self):
        self.checkRadioElementClick(self._skippable_fb, "xpath", self._skippable_fb_id)

    def fbPageSendKeys(self, pageUrlFb):
        self.sendKeys(pageUrlFb, self._add_page_fb)

    def clickDnStep(self):
        self.elementClick(self._add_donation_step)

    def dnEmailSendKeys(self, emailDn):
        self.sendKeys(emailDn, self._add_donation)

    #-------------------Link Gate----------------

    def artistNameSendkeys(self, artistname):
        self.sendKeys(artistname, self._artist_name)

    def artistTitleSendkeys(self, artistitle):
        self.sendKeys(artistitle, self._link_title)

    def clickTitleNextButton(self):
        self.elementClick(self._title_next_button)

    def secretSendKeys(self, secretLink):
        self.sendKeys(secretLink, self._link_custom_redir_url)

    def clickSecretNextButton(self):
        self.elementClick(self._link_SecretLink_next_button)

    def selectUnlockButtonText(self):
        time.sleep(2)
        self.elementClick(self._link_button_text_dropdown, "xpath")
        time.sleep(2)
        self.elementClick(self._link_menu_select_dropdown, "xpath" )

    def clickUnlockNextButton(self):
        self.elementClick(self._link_unlock_button_next_button)

    def designSendKeys(self):
        self.sendKeys("C:\\Users\\Anil\\workspace_python\\hypeddit-Project\\Files\\Tulips.jpg", self._choose_coverart)





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

    def clickOnCreatLinkGate(self):
        self.elementClick(self._create_linkgate_button)

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
                      artisttitle="verma", fbpixel=7, fbtoken=8, Fg=1 ):
        if Fg == 1:
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
        if Fg == 0:
            time.sleep(5)
            self.clickShareMusicLink()
            time.sleep(5)
            self.clickLinkgateLink()

            self.linkTitle()
            self.linkSecret()
            self.linkUnlock()
            self.linkDesignStep()

        self.gateSteps(Fg)
        time.sleep(2)
        self.linkUrl()
        time.sleep(2)
        self.releaseSettings(Fg)
        time.sleep(2)
        self.emailPromotion()
        time.sleep(2)
        self.trackingPixels(fbpixel, fbtoken)
        time.sleep(2)
        self.confirmation(Fg)
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

    def gateSteps(self, Fg):
        # ----------------Email Step------------------------------
        time.sleep(3)
        self.clickEmCollect()
        self.clickEmCollectName()
        self.clickEmSkippable()
        # -------------------Soundlcoud Step---------------------------
        if Fg == 0:
            self.clickScStep()

        time.sleep(3)
        self.clickScFollow()
        self.clickScComment()
        self.clickScLike()
        self.clickScRepost()
        self.clickScSkippable()
        if Fg == 0:
            self.profileScSendKeys("https://soundcloud.com/makelogin")
            self.trackScSendKeys("https://soundcloud.com/makelogin/sleep-away")

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
        self.clickYtProfileAddButton()

        # ---------------------Apple Step------------------------------
        time.sleep(3)
        self.clickApStep()
        time.sleep(2)
        self.clickApStep()
        self.clickApLike()
        self.clickApSave()
        self.clickApSkippable()
        self.apTrackSendKeys("https://music.apple.com/in/album/humdard/1111741333?i=1111741446")



        #-------------------------------Spotify Step --------------------------

        time.sleep(3)
        self.clickSpStep()

        self.clickSpFollow()
        self.clickSpSave()
        self.clickSpSkippable()
        self.spProfileSendKeys("https://open.spotify.com/artist/11bBHpkCZPkktTsrXAZyql")
        self.spTrackSendKeys("https://open.spotify.com/track/0VbRRS6pOgCvepxNiAz2fY")





        # ---------------------Deezer Step------------------------------
        time.sleep(3)
        self.clickDzStep()
        self.clickDzFollow()
        self.clickDzSave()
        self.clickDzSkippable()
        self.dzArtistSendKeys("https://www.deezer.com/us/artist/661247")
        self.dzTrackSendKeys("https://www.deezer.com/us/track/15211178")

        # ---------------------Mixcloud Step------------------------------
        time.sleep(3)
        self.clickMcStep()
        self.clickMcFollow()
        self.clickMcRepost()
        self.clickMcLike()
        self.clickMcSkippable()
        self.mcProfileSendKeys("https://www.mixcloud.com/gabrydemartini")
        self.mcTrackSendKeys("https://www.mixcloud.com/felixdahousecat/chicago-blakkout-episode-14/")

        # ---------------------Twitter Step------------------------------
        time.sleep(3)
        self.clickTwStep()
        self.clickTwFollow()
        self.clickTwShare()
        self.clickTwSkippable()
        self.twProfileSendKeys("https://twitter.com/csswg")

        # ---------------------Twitch Step------------------------------
        time.sleep(3)
        self.clickThStep()
        self.clickThFollow()
        self.clickThSubscription()
        self.clickThSkippable()
        self.thChannelSendKeys("sweet_anita")

        # ---------------------Messenger Step------------------------------
        time.sleep(3)
        self.clickFbMsgrStep()
        self.clickFbMsgrSubscription()
        self.clickFbMsgrSkippable()
        time.sleep(2)
        self.fbMsgrChatbotSendKeys()
        self.fbMsgrPageSendKeys('https://www.facebook.com/Test-company-109379167072055')

        # ---------------------Instagram Step------------------------------
        time.sleep(3)
        self.clickIgStep()
        self.clickIgFollow()
        self.clickIgSkippable()
        self.igProfileSendKeys("https://www.instagram.com/hypeddit")

        # ---------------------TikTok Step------------------------------
        time.sleep(3)
        self.clickTkStep()
        self.clickTkFollow()
        self.clickTkSkippable()
        self.tkProfileSendKeys("https://www.tiktok.com/hypeddit")

        # ---------------------Bandcamp Step------------------------------
        time.sleep(3)
        self.clickBcStep()
        self.clickBcFollow()
        self.clickBcSkippable()
        self.bcProfileSendKeys("https://www.bandcamp.com/hypeddit")

        # ---------------------Facebook Step------------------------------
        time.sleep(3)
        self.clickFbStep()
        self.clickFbShare()
        self.clickFbLike()
        self.clickFbSkippable()
        self.fbPageSendKeys("https://www.facebook.com/hypeddit")

        # ---------------------Donation Step------------------------------
        time.sleep(3)
        self.clickDnStep()
        self.dnEmailSendKeys("testing001web@gmail.com")

        self.clickOnNextGateSteps()
        time.sleep(1)
        self.clickOnNextGateSteps()







    def linkUrl(self):
        # Skip Edit Custom Url
        # skip page text Edit
        # skip optional Edit
        time.sleep(2)
        self.clickOnNextLinkUrl()
        time.sleep(1)
        self.clickOnNextLinkUrl()




    def releaseSettings(self,Fg):
        if Fg == 1:
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

    def confirmation(self, Fg):
        if Fg == 1:
            self.clickOnCreate()
        else:
            self.clickOnCreatLinkGate()


    def linkTitle(self):
        time.sleep(1)
        self.artistNameSendkeys("anil")
        time.sleep(1)
        self.artistTitleSendkeys("sharma")
        time.sleep(1)
        self.clickTitleNextButton()

    def linkSecret(self):
        time.sleep(1)
        self.secretSendKeys("https://www.google.com")
        time.sleep(1)
        self.clickSecretNextButton()

    def linkUnlock(self):
        time.sleep(1)
        self.selectUnlockButtonText()
        time.sleep(1)
        self.clickUnlockNextButton()

    def linkDesignStep(self):
        time.sleep(1)
        self.designSendKeys()
        time.sleep(5)
        self.clickDarkScheme()
        time.sleep(1)
        time.sleep(1)
        self.clickOnNextDesign()
        time.sleep(1)
