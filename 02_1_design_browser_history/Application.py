from BrowserHistory import BrowserHistory

if __name__ == "__main__":
    browser_history = BrowserHistory('0')
    browser_history.visit('1')
    browser_history.visit('2')
    browser_history.visit('3')

    print(browser_history.back(1) == '2')
    print(browser_history.back(1) == '1')
    print(browser_history.forward(1) == '2')

    browser_history.visit('100')

    print(browser_history.forward(2) == '100')
    print(browser_history.back(2) == '1')

    print(browser_history.back(7) == '0')