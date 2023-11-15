class BrowserHistory:
    def __init__(self, homepage: str):
        self.forwardNums = [homepage]  # 前进
        self.backNums = []  # 后退

    def visit(self, url: str) -> None:
        self.forwardNums.append(url)
        self.backNums = []

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.forwardNums) > 1:
                self.backNums.append(self.forwardNums.pop())
            else:
                break
        return self.forwardNums[-1]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.backNums:
                self.forwardNums.append(self.backNums.pop())
            else:
                break
        return self.forwardNums[-1]


if __name__ == "__main__":
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    browserHistory.back(1)
    browserHistory.visit("facebook.com")
    browserHistory.forward(1)
    browserHistory.visit("linkedin.com")
    browserHistory.forward(2)
    browserHistory.back(2)
    browserHistory.back(7)
