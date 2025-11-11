from fluent.runtime import FluentLocalization, FluentResourceLoader

class language_service:

    def __init__(self):
        locales = ["ru", "en"]
        loader = FluentResourceLoader("bot/locales/{locale}")
        self.DEFAULT_LANG = "ru"

        self._localizations = {
            lang: FluentLocalization([lang], ["messages.ftl"], loader)
            for lang in locales
        }

    def t(self, lang: str, key: str, **kwargs) -> str:
        loc = self._localizations.get(lang, self._localizations[self.DEFAULT_LANG])
        return loc.format_value(key, kwargs)

lng_service = language_service()