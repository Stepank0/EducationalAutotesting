import time

import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT

        assert expected_links == actual_links, 'Validating Nav Links text'
        # homepage_nav.get_nav_link_by_name('Beauty').click()


    def test_nav(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.driver.delete_cookie('ak_bmsc')
        for index in range(13):
            homepage_nav.get_nav_links()[index].click()
            homepage_nav.driver.delete_cookie('ak_bmsc')


