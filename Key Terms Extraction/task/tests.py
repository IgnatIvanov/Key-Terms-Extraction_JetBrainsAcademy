from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from test.news import news_text

answer = {'Brain Disconnects During Sleep:': ["sleep", "cortex", "consciousness", "tononi", "tm"],
          'New Portuguese skull may be an early relative of Neandertals:': ["skull", "fossil", "europe", "trait",
                                                                            "genus"],
          'Living by the coast could improve mental health:': ["health", "coast", "mental", "living", "household"],
          'Did you knowingly commit a crime? Brain scans could tell:': ["brain", "suitcase", "study", "security",
                                                                        "scenario"],
          'Computer learns to detect skin cancer more accurately than doctors:': ["dermatologist", "skin", "melanoma",
                                                                                  "cnn", "lesion"],
          'US economic growth stronger than expected despite weak demand:': ["rate", "growth", "quarter", "economy",
                                                                             "investment"],
          'Microsoft becomes third listed US firm to be valued at $1tn:': ["microsoft", "share", "cloud", "market",
                                                                           "company"],
          "Apple's Siri is a better rapper than you:": ["siri", "rhyme", "smooth", "rizzo", "producer"],
          'Netflix viewers like comedy for breakfast and drama at lunch:': ["netflix", "day", "comedy", "viewer", "tv"],
          'Loneliness May Make Quitting Smoking Even Tougher:': ["smoking", "loneliness", "smoke", "quit", "lead"]}


class KTETest(StageTest):
    def generate(self):
        with open('news.xml', 'w') as file:
            file.write(news_text)
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        while ("" in lines):
            lines.remove("")
        headers = lines[::2]
        text = lines[1::2]
        news_text = []
        for row in text:
            row = row.split(' ')
            while ("" in row):
                row.remove("")
            news_text.append(row)
        news = {}
        if len(news_text) != len(headers):
            return CheckResult.wrong(feedback="The number of headers should be equal "
                                              "to the number of lines with keywords.\n"
                                              "Please check the output of your program.")
        for i in range(len(headers)):
            news[headers[i]] = news_text[i]
        wrong_news = 0
        wrong_head = 0
        ans = list(answer.items())
        new = list(news.items())
        for i in range(len(ans)):
            # ?????????? ???????????????? ???? ???? ????????????????, ?????? ?? ?? ???????????? ????????????
            if len(answer) != len(news):
                return CheckResult.wrong(
                    feedback="Something is wrong with output. Probably, you have forgotten to print some news? Try again")
            if set(ans[i][1]) != set(new[i][1]):
                wrong_news += 1
            if ans[i][0] != new[i][0]:
                wrong_head += 1
        if len(answer) != len(news):
            return CheckResult.wrong(
                feedback="Something is wrong with output. Probably, you have forgotten to print some news? Try again")
        elif wrong_head != 0:
            return CheckResult.wrong(
                feedback='Incorrect. Probably, something is wrong with the headers? Try again!'.format(wrong_head,
                                                                                                       len(news)))
        elif wrong_news != 0:
            return CheckResult.wrong(
                feedback='Keywords found incorrectly in {} of {} news texts. Try again!'.format(wrong_news, len(news)))

        return CheckResult.correct()


if __name__ == '__main__':
    KTETest().run_tests()
