import time
import flet as ft
import model as md


class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self, e):
        txtIno = self._view._txtIn.value
        if txtIno == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a sentence!"))
            return

        language = self._view.dd.value
        modality = self._view.dd_mode.value

        if language == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a language!"))
            return

        if modality == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a modality!"))
            return

        paroleErrate, time = self.handleSentence(txtIno, language, modality)

        if paroleErrate is not None:
            self._view.txtOut.controls.append(ft.Text(value=paroleErrate + " in " + str(time) + " seconds"))

        else:
            self._view.txtOut.controls.append(ft.Text(value="No errors found in " + str(time) + " seconds"))

        self._view._txtIn.value = ""
        self._view.page.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
