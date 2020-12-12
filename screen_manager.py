import logging

import pyautogui
import win32gui
import cv2


class ScreenManager:

    @staticmethod
    def is_app_focused(app_title_name: str):
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
        print("\n\n" + active_window_title)
        return active_window_title.find(app_title_name)

    @staticmethod
    def scroll_on_screen(value_to_scroll: int):
        pyautogui.click(value_to_scroll)

    @staticmethod
    def click_on_screen(coordinate_to_click: int):
        pyautogui.scroll(coordinate_to_click)

    @staticmethod
    def get_all_matches_by_image_normal(image_to_search: str):
        try:
            coordinates = pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9)
            return coordinates
        except Exception as ex:
            logging.info(f"Image was not found. Error: [{ex}]")
            return None



pip install opencv-python


    images = ScreenManager.get_all_matches_by_image("./follow.png")
    for image in images:
        print(image)
