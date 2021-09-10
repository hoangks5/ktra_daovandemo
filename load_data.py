import re
def __dell__(sentence):
  sentence = sentence.lower()
  sentence = re.sub(r'[~!@#$%\^&*\(\)\[\]\\|:;\'"]+', ' ', sentence)
  sentence = re.sub(r'\s+', ' ', sentence).strip()
  return sentence