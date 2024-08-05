import allure
import pytest

from utils.client import URL, allure_annotations

from tests.data.tests_data.parametrize_home_page import *

from tests.data.selectors.common_selectors import collapse_cards
from tests.data.selectors.full_price_page_selectors import title_full_price
from tests.data.selectors.part_price_page_selectors import title_part_price


@allure_annotations(
    title="Home Page",
    story="Open home page",
    description='This test checks if the home page is open with the correct URL and logo',
    tag='Positive',
    severity=allure.severity_level.BLOCKER

)
def test_home_page_open(home_page):
    assert home_page.element_state_checking.is_current_url(URL)
    home_page.waiting_conditions.wait_for_element_visible_by_locator(link_logo)
    assert home_page.element_state_checking.is_element_visible(link_logo)


@allure_annotations(
    title="Home Page",
    story="Logo click",
    description='This test checks if the logo is clickable and redirects to the main page',
    tag='Positive'
)
def test_logo_click(home_page):
    home_page.element_interaction.click_element(link_logo)
    assert home_page.element_state_checking.is_current_url(URL)
    assert home_page.element_state_checking.is_element_in_viewport(link_logo)


@allure_annotations(
    title="Home Page",
    story="Sign up click",
    description='This test checks if the sign up button is clickable and redirects to the booking form',
    tag='Positive'
)
def test_button_sign_up_click(home_page):
    home_page.element_interaction.click_element(button_sign_up_top)
    home_page.waiting_conditions.wait_for_scroll_to_element(title_booking)
    assert home_page.element_state_checking.is_element_in_viewport(title_booking)


@allure_annotations(
    title="Home Page",
    story="Anchor click",
    description='This test checks if the anchors are clickable and redirects to the correct targets',
    tag='Positive'
)
@pytest.mark.parametrize("anchor, target", anchors_top_list, ids=anchors_top_list_ids)
def test_top_anchor_click(home_page, anchor, target):
    home_page.element_interaction.click_element(anchor)
    home_page.waiting_conditions.wait_for_scroll_to_element(target)
    assert home_page.element_state_checking.is_element_in_viewport(target)


@allure_annotations(
    title="Home Page",
    story="Buy course links click",
    description='This test checks if the buy course links are clickable and redirects to the correct pages',
    tag='Positive',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.parametrize("link, target, url", buy_links_list, ids=buy_links_list_ids)
def test_buy_course_links_click(home_page, link, target, url):
    home_page.element_interaction.click_element(link)
    home_page.waiting_conditions.wait_for_element_visible_by_locator(target)
    assert home_page.element_state_checking.is_current_url(url)
    assert home_page.element_state_checking.is_element_visible(target)


@allure_annotations(
    title="Home Page",
    story="Other links click",
    description='This test checks if the other links on the home page are clickable and redirects to the correct pages',
    tag='Positive'
)
@pytest.mark.parametrize("link, target, url", other_links_list, ids=other_links_list_ids)
def test_other_links_click(home_page, link, target, url):
    home_page.scroll_wait_click_element_by_locator(link)
    home_page.waiting_conditions.wait_for_element_visible_by_locator(target)
    assert home_page.element_state_checking.is_current_url(url)
    assert home_page.element_state_checking.is_element_visible(target)


@allure_annotations(
    title="Home Page",
    story="Collapse cards click",
    description='This test checks if the collapse cards are clickable and toggles their visibility',
    tag='Positive'
)
def test_collapse_cards_click(home_page):
    home_page.utility_functions.scroll_to_element_top_of_screen(collapse_cards)
    home_page.waiting_conditions.wait_for_scroll_to_element(collapse_cards)
    home_page.click_all_collapse_elements(collapse_cards, collapse_cards_active, "collapsed")


@allure_annotations(
    title="Home Page",
    story="Button sign up right group click",
    description='This test checks if the subscribe button for the right group is clickable and redirects to the '
                + 'booking form',
    tag='Positive'
)
def test_button_sign_up_right_group_click(home_page):
    home_page.scroll_wait_click_element_by_locator(button_sign_up_right_group)
    home_page.waiting_conditions.wait_for_scroll_to_element(title_booking)
    assert home_page.element_state_checking.is_element_in_viewport(title_booking)


@allure_annotations(
    title="Home Page",
    story="Switchers click",
    description='This test checks if the toggles are clickable and verifies that the appropriate content is displayed '
                + 'for each state',
    tag='Positive'
)
def test_switchers_click(home_page):
    home_page.utility_functions.scroll_to_element(switcher_stages)
    home_page.waiting_conditions.wait_for_scroll_to_element(switcher_stages)
    assert home_page.element_state_checking.is_element_visible(title_staged_payment)
    home_page.element_interaction.click_element(switcher_entire_amount)
    assert home_page.element_state_checking.is_element_visible(title_payment_whole_course)
    home_page.element_interaction.click_element(switcher_stages)
    assert home_page.element_state_checking.is_element_not_visible(title_payment_whole_course)
    assert home_page.element_state_checking.is_element_visible(title_staged_payment)


@allure_annotations(
    title="Home Page",
    story="Pay buttons click",
    description='This test checks if the pay button are clickable and redirects to the part price page',
    tag='Positive',
    severity=allure.severity_level.CRITICAL
)
def test_button_pay_first_step_click(home_page):
    home_page.scroll_wait_click_element_by_locator(button_pay_first_step)
    home_page.waiting_conditions.wait_for_element_visible_by_locator(title_part_price)
    assert home_page.element_state_checking.is_current_url(PART_PRICE)
    assert home_page.element_state_checking.is_element_in_viewport(title_part_price)


@allure_annotations(
    title="Home Page",
    story="Pay buttons click",
    description='This test checks if the pay button are clickable and redirects to the full price page',
    tag='Positive',
    severity=allure.severity_level.CRITICAL
)
def test_button_pay_entirely_click(home_page):
    home_page.scroll_wait_click_element_by_locator(switcher_entire_amount)
    home_page.scroll_wait_click_element_by_locator(button_pay_entirely)
    home_page.waiting_conditions.wait_for_element_visible_by_locator(title_full_price)
    assert home_page.element_state_checking.is_current_url(FULL_PRICE)
    assert home_page.element_state_checking.is_element_in_viewport(title_full_price)


@allure_annotations(
    title="Home Page",
    story="Booking form submit",
    description='This test verifies a positive script for filling out and submitting the booking form, as well as '
                + 'displaying a successful booking after submitting the form and having the submitter\'s name in the '
                + 'booking confirmation text',
    tag='Positive',
    severity=allure.severity_level.BLOCKER
)
def test_booking_form_submit(home_page):
    home_page.utility_functions.scroll_to_element_top_of_screen(title_booking)
    home_page.waiting_conditions.wait_for_scroll_to_element(title_booking)
    home_page.element_interaction.send_keys(input_full_name, "Evgeny")
    home_page.element_interaction.send_keys(input_email, "test@test.com")
    home_page.element_interaction.send_keys(input_contact, "any text")
    home_page.element_interaction.send_keys(input_comment, "some text")
    home_page.element_interaction.click_element(button_sign_up)
    home_page.waiting_conditions.wait_for_element_visible_by_locator(paragraph_successful_alert)
    assert home_page.element_state_checking.is_element_visible(paragraph_successful_alert)
    assert home_page.element_state_checking.is_element_text_contains_expected_text(paragraph_successful_alert, "Evgeny")
