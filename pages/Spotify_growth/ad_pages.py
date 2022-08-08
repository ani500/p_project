import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging

class AdPage(SeleniumDriver):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver


    # Locators
    _goal_next_button = "next_box_button_choose-type"

    _page_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select page']"
    _select_page = "//ul[@class='dropdown-menu inner']//span[text()='Musical']"
    _fbaccount_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select account']"
    _select_fbaccount = "//ul[@class='dropdown-menu inner']//span[text()='1447513952355862 [Anil Sharma]']"
    _igaccount_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select account']"
    _select_igaccount = "//ul[@class='dropdown-menu inner']//span[text()='']"
    _pixelaccount_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select account']"
    _select_pixelaccount = "//ul[@class='dropdown-menu inner']//span[text()='1597053410709523 [My Pixel]']"

    _accounts_next_button = "next_box_button_facebook-account-connect"

    _spotify_url = "track_url"
    _artist_name = "artist_name"
    _artist_title = "title"
    _genre_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select genre']"
    _select_genre = "//ul[@class='dropdown-menu inner']//span[text()='Bass']"
    _music_next_button = "next_box_button_music"

    _ad_inputManualCoverart = "inputManualCoverart"
    _ad_inputFilemp3 = "inputFilemp3"
    _ad_inputFilemp4 = "inputFilemp4"
    _ad_next_button = "next_box_button_audio-video"

    _countries_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Choose a saved list to fill in countries from']"
    _select_countries = "//ul[@class='dropdown-menu inner']//span[text()='Tier One Countries']"
    _countries_next_button = "next_box_button_countries"

    _ad_spotify_artists = "add_spotify_artist"
    _interest_button = "generateInterestsButton"
    _interest_next_button ='next_box_button_interests'

    _budget_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Choose INR Per Day']"
    _select_budget = "//ul[@class='dropdown-menu inner']//span[text()='420']"
    _budget_next_button = "next_box_button_budget"

    _advance_min_age_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Min Age']"
    _select_min_age = "//ul[@class='dropdown-menu inner']//span[text()='19']"
    _advance_max_age_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Max Age']"
    _select_max_age = "//ul[@class='dropdown-menu inner']//span[text()='61']"
    _advance_gender_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='All']"
    _select_gender = "//ul[@class='dropdown-menu inner']//span[text()='Men']"
    _head_link_override = "headline_text_override"
    _advance_next_button = "next_box_button_advanced"

    _common_terms = "//div[@class='checkbox']//label[@for='common_terms']"
    _facebook_terms = "//div[@class='checkbox']//label[@for='facebook_terms']"
    _hypeddit_terms = "//div[@class='checkbox']//label[@for='hypeddit_terms']"
    _save_draft_button = "next_box_button_confirmation"

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











































































