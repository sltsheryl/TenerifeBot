from deep_translator import GoogleTranslator

languages_list = [
  "english", "chinese", "french", "german", "spanish", "japanese", "malay",
  "italian", "korean", "tamil"
]
prefix_list = ["en", "zh-CN", "fr", "de", "es", "ja", "ms", "it", "ko", "ta"]


def translate(msg, language):
  language = language.lower()
  if language not in languages_list:
    return "-1"
  target_index = languages_list.index(language)
  target_language = prefix_list[target_index]
  res = GoogleTranslator(source='auto', target=target_language).translate(msg)
  return res


def get_languages():
  return languages_list
