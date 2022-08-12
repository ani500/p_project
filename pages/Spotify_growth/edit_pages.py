import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging
import time

class EditPage(SeleniumDriver):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver


    # Locators
    _goal_next_button = "next_box_button_choose-type"

    _page_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select page']"
    _select_page = "//ul[@class='dropdown-menu inner']//span[text()='Musical']"
    _fbaccount_caret = "//button[@data-id='ads_account_id']//span[text()='Select account']"
    _select_fbaccount = "//ul[@class='dropdown-menu inner']//span[text()='1447513952355862 [Anil Sharma]']"
    _igaccount_caret = "//button[@data-id='instagram_account_id']//span[text()='Select account']"
    _select_igaccount = "//ul[@class='dropdown-menu inner']//span[text()='']"
    _pixelaccount_caret = "//button[@data-id='facebook_pixel_id']//span[text()='Select account']"
    _select_pixelaccount = "//ul[@class='dropdown-menu inner']//span[text()='1597053410709523 [My Pixel]']"

    _accounts_next_button = "next_box_button_facebook-account-connect"

    _spotify_url = "track_url"
    _artist_name = "artist_name"
    _artist_title = "title"
    _genre_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Bass']"
    _select_genre = "//ul[@class='dropdown-menu inner']//span[text()='Future House']"
    _music_next_button = "next_box_button_music"

    _ad_inputManualCoverart = "inputManualCoverart"
    _ad_inputFilemp3 = "inputFilemp3"
    _ad_inputFilemp4 = "inputFilemp4"
    _ad_next_button = "next_box_button_audio-video"

    _countries_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Choose a saved list to fill in countries from']"
    _select_countries = "//ul[@class='dropdown-menu inner']//span[text()='Tier Three Countries']"
    _countries_next_button = "next_box_button_countries"

    _ad_spotify_artists = "add_spotify_artist"
    _interest_button = "generateInterestsButton"
    _interest_next_button ='next_box_button_interests'

    _budget_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='420']"
    _select_budget = "//ul[@class='dropdown-menu inner']//span[text()='500']"
    _budget_next_button = "next_box_button_budget"

    _advance_min_age_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='18']"
    _select_min_age = "//div[@class='btn-group bootstrap-select form-control dropup open']//span[text()='19']"
    _advance_max_age_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='65']"
    _select_max_age = "//div[@class='btn-group bootstrap-select form-control dropup open']//span[text()='61']"
    _advance_gender_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Men']"
    _select_gender = "//ul[@class='dropdown-menu inner']//span[text()='Women']"
    _head_link_override = "headline_text_override"
    _advance_next_button = "next_box_button_advanced"

    _common_terms = "//div[@class='checkbox']//label[@for='common_terms']"
    _common_terms_id = "common_terms"
    _facebook_terms = "//div[@class='checkbox']//label[@for='facebook_terms']"
    _facebook_terms_id = "facebook_terms"
    _hypeddit_terms = "//div[@class='checkbox']//label[@for='hypeddit_terms']"
    _hypeddit_terms_id = "hypeddit_terms"
    _save_draft_button = "next_box_button_confirmation"

    _loader_image = "//img[@title='Loading']"
    _music_loader_image = "//div[@class='loader select-loading'][contains(@style,'display: block')]"
    _interest_loader_image = "//div[@id='related_artists_interest_main'][contains(@class,'hide')]"

    #facebook Window Locators
    _facebook_button = "AdsFacebookLogin"
    _facebook_confirm_button = "//span[text()='Continue as Anil Sharma']"
    _facebook_email = "email"
    _facebook_pass = "pass"
    _facebook_login_button = "//input[@value='Log In']"


    def clickGoalNextButton(self):
        self.elementClick(self._goal_next_button)

    def clickOnFbPage(self):
        self.elementClick(self._page_caret, "xpath")

    def selectFbPage(self):
        self.elementClick(self._select_page, "xpath")

    def clickOnFbPageAccount(self):
        self.elementClick(self._fbaccount_caret, "xpath")

    def selectFbPageAccount(self):
        self.elementClick(self._select_fbaccount, "xpath")

    def clickOnPixelAccount(self):
        self.elementClick(self._pixelaccount_caret, "xpath")

    def selectPixelAccount(self):
        self.elementClick(self._select_pixelaccount, "xpath")

    def clickAccountNextButton(self):
        self.elementClick(self._accounts_next_button)

    def spUrlSendKeys(self, spUrl):
        self.sendKeys(spUrl, self._spotify_url)

    def artistSendKeys(self, artistName):
        self.sendKeys(artistName, self._artist_name)

    def titleSendKeys(self, artistTitle):
        self.sendKeys(artistTitle, self._artist_title)

    def clickArtistField(self):
        self.elementClick(self._artist_name)

    def clickOnGenre(self):
        self.elementClick(self._genre_caret, "xpath")

    def selectGenre(self):
        self.elementClick(self._select_genre, "xpath")

    def clickMusicNextButton(self):
        self.elementClick(self._music_next_button)

    def mp3SendKeys(self, filePathmp3):
        self.sendKeys(filePathmp3, self._ad_inputFilemp3)

    def mp4SendKeys(self, filePathmp4):
        self.sendKeys(filePathmp4, self._ad_inputFilemp4)

    def clickAdNextButton(self):
        self.elementClick(self._ad_next_button)

    def clickOnCountryList(self):
        self.elementClick(self._countries_caret, "xpath")

    def selectCountries(self):
        self.elementClick(self._select_countries, "xpath")

    def clickCountriesNextButton(self):
        self.elementClick(self._countries_next_button)

    def spArtistSendKeys(self, artistName):
        self.sendKeys(artistName, self._ad_spotify_artists)

    def clickGenerateInterestButton(self):
        self.elementClick(self._interest_button)

    def clickInterestNextButton(self):
        self.elementClick(self._interest_next_button)

    def clickOnBudget(self):
        self.elementClick(self._budget_caret, "xpath")

    def selectBudgetAmount(self):
        self.elementClick(self._select_budget, "xpath")

    def clickBudgetNextButton(self):
        self.elementClick(self._budget_next_button)

    def clickOnSelectMinAge(self):
        self.elementClick(self._advance_min_age_caret, "xpath")

    def selectMinAge(self):
        self.elementClick(self._select_min_age, "xpath")

    def clickOnSelectMaxAge(self):
        self.elementClick(self._advance_max_age_caret, "xpath")

    def selectMaxAge(self):
        self.elementClick(self._select_max_age, "xpath")

    def clickOnSelectGender(self):
        self.elementClick(self._advance_gender_caret, "xpath")

    def selectGender(self):
        self.elementClick(self._select_gender, "xpath")

    def overRideTextSendKeys(self, overridetext):
        self.sendKeys(overridetext, self._head_link_override)

    def clickAdvancetNextButton(self):
        self.elementClick(self._advance_next_button)

    def clickCommonTerms(self):
        self.checkRadioElementClick(self._common_terms, "xpath", self._common_terms_id)

    def clickFbTerms(self):
        self.checkRadioElementClick(self._facebook_terms, "xpath", self._facebook_terms_id)

    def clickHypedditTerms(self):
        self.checkRadioElementClick(self._hypeddit_terms, "xpath", self._hypeddit_terms_id)

    def clickDraftNextButton(self):
        self.elementClick(self._save_draft_button)

    def waitFl(self,loc,lid="id"):
        self.waitForElement(loc,lid,50,.5)

    def checkLoaderElement(self,loc,ltype="id"):
        return self.isElementPresent(loc,ltype)

    # facebook window

    def clickFbConnectButton(self):
        self.elementClick(self._facebook_button)

    def fbEmailSendKeys(self, fbEmail):
        self.sendKeys(fbEmail, self._facebook_email)

    def fbPassSendKeys(self, fbEmail):
        self.sendKeys(fbEmail, self._facebook_pass)

    def clickFbLoginButton(self):
        self.elementClick(self._facebook_login_button, "xpath")

    def clickFbConfirmButton(self):
        self.elementClick(self._facebook_confirm_button, "xpath")




    def editAd(self):
        self.driver.get("https://dev2.hypeddit.com/ads/edit/2ea2f8e2-8308-467a-bb50-94f004461dda")

        self.goal()
        self.accountprofile()
        self.music()
        self.ad()

        self.countries()
        self.waitFl(self._interest_button)
        self.interest()

        self.budget()

        self.advance()
        self.confirmation()
        time.sleep(50)




    def goal(self):
        self.clickGoalNextButton()

    def accountprofile(self):

        #self.clickFbConnectButton()
        #time.sleep(2)
        #self.switchWindowHander(0)
        #time.sleep(2)
        #self.fbEmailSendKeys("anilangira@gmail.com")
        #time.sleep(2)
        #self.fbPassSendKeys("Uid@12345")
        #time.sleep(2)
        #self.clickFbLoginButton()
        #self.waitFl(self._facebook_confirm_button,"xpath")
        #self.clickFbConfirmButton()
        #time.sleep(10)
        #self.driver.close()
        #self.switchWindowHander(1)




        #self.waitFl(self._page_caret, "xpath")
        #self.clickOnFbPage()
        #self.selectFbPage()
        #self.waitFl(self._fbaccount_caret, "xpath")
        #self.clickOnFbPageAccount()
        #self.selectFbPageAccount()
        #self.waitFl(self._pixelaccount_caret, "xpath")
        #self.clickOnPixelAccount()
        #self.selectPixelAccount()
        self.clickAccountNextButton()

    def music(self):
        self.getElement(self._spotify_url).clear()
        self.spUrlSendKeys("https://open.spotify.com/track/7GJ5HPftvNgAoeaA1uzJUL?si=c5bba297375548e4")
        self.clickArtistField()

        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._music_loader_image,"xpath") == False:
                self.artistSendKeys("Gold10")
                self.titleSendKeys("Gold20")
                self.waitFl(self._genre_caret, "xpath")
                self.clickOnGenre()
                self.selectGenre()
                self.clickMusicNextButton()
                break



    def     ad(self):
        self.mp3SendKeys("C:\\Users\\Anil\\workspace_python\\hypeddit-Project\\Files\\45 sec.mp3")
        #self.mp4SendKeys("C:\\Users\\Anil\\workspace_python\\hypeddit-Project\\Files\\Hazard Lights - SGE Cover - Preview 1.mp4")
        time.sleep(5)
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._loader_image, "xpath") == False:
                self.clickAdNextButton()
                print("next button clicked")
                break


    def countries(self):
        self.waitFl(self._countries_caret, "xpath")
        self.clickOnCountryList()
        self.selectCountries()
        time.sleep(1)
        self.clickCountriesNextButton()

    def interest(self):
        self.clickGenerateInterestButton()

        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._interest_loader_image, "xpath") == False:
                self.clickInterestNextButton()
                break


    def budget(self):
        self.waitFl(self._budget_caret, "xpath")
        self.clickOnBudget()
        self.selectBudgetAmount()
        self.clickBudgetNextButton()

    def advance(self):
        time.sleep(2)
        self.waitFl(self._advance_min_age_caret, "xpath")
        self.clickOnSelectMinAge()
        self.selectMinAge()
        time.sleep(2)
        self.waitFl(self._advance_max_age_caret, "xpath")
        self.clickOnSelectMaxAge()
        self.selectMaxAge()
        time.sleep(2)
        self.waitFl(self._advance_gender_caret, "xpath")
        self.clickOnSelectGender()
        self.selectGender()
        self.overRideTextSendKeys("Rock music")
        self.clickAdvancetNextButton()

    def confirmation(self):
        #self.clickCommonTerms()
        #self.clickFbTerms()
        #self.clickHypedditTerms()
        self.clickDraftNextButton()



















































































































