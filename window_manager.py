import pygetwindow as gw



import ctypes
import win32gui

SW_MINIMIZE = 6

def list_all_windows():
    """List all current window titles."""
    def window_enumeration_handler(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(window_enumeration_handler, windows)
    print("Available windows:")
    for hwnd, title in windows:
        print(f"- Handle: {hwnd}, Title: '{title}'")
    return windows

def minimise_window(window_title):
    """Minimise a window by its title using Windows API."""
    windows = list_all_windows()
    target_window = None

    # Prioritize exact matches
    for hwnd, title in windows:
        if title.strip().lower() == window_title.lower():
            target_window = hwnd
            break

    # If no exact match, try partial match
    if not target_window:
        for hwnd, title in windows:
            if window_title.lower() in title.lower():
                target_window = hwnd
                break

    if target_window:
        ctypes.windll.user32.ShowWindow(target_window, SW_MINIMIZE)
        print(f"Minimized: '{win32gui.GetWindowText(target_window)}'")
    else:
        print(f"No window found with title containing: '{window_title}'")






def maximize_window(window_title):
    """Maximize a window by its title."""
    window = gw.getWindowsWithTitle(window_title)
    if window:
        try:
            window[0].maximize()
            print(f"Maximized: {window_title}")
        except Exception as e:
            print(f"Failed to maximize the window: {window_title}. Error: {e}")
    else:
        print(f"No window found with title: {window_title}")
