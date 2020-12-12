import random
import time

import keyboard

from screen_manager import ScreenManager


def run():
    total_follows_count = 0

    while True:
        if ScreenManager.is_app_focused(app_title_name="instagram - google chrome"):
            follow_buttons_found = ScreenManager.get_all_matches_by_image_normal("./follow.png")

            for follow_button in follow_buttons_found:
                total_follows_count = total_follows_count + 1
                ScreenManager.click_on_screen(coordinate_to_click=follow_button)
                time.sleep(random.randint(1, 2))

            ScreenManager.scroll_screen(value_to_scroll=-400)
            time.sleep(random.randint(1, 2))

        if keyboard.is_pressed('ESC'):
            print('Saindo do programa InstagramBot')
            break

        print("Total de follows realizados até o momento: " + str(1 + total_follows_count))


run()
