''''
Install packages:
pip install pyvi
pip install https://gitlab.com/trungtv/vi_spacy/-/raw/master/vi_core_news_lg/dist/vi_core_news_lg-0.0.1.tar.gz

'''

import spacy
nlp = spacy.load('vi_core_news_lg')

text = "Tổng bí thư, Chủ tịch Trung Quốc Tập Cận Bình khẳng định Tổng bí thư Nguyễn Phú Trọng là ""người bạn tốt, chân thành"" của Trung Quốc, ""người định hướng và thúc đẩy quan hệ đối tác hợp tác chiến lược toàn diện giữa Trung Quốc và Việt Nam trong thời đại mới"". Ông nói rằng việc trao tặng huân chương cho Tổng bí thư Nguyễn Phú Trọng biểu tượng cho tình cảm sâu sắc, niềm hy vọng cùng theo đuổi tương lai tốt đẹp hơn của hai bên."

doc = nlp(text)

print("====================")
for sentence in doc.sents:
    print(sentence)
print("====================")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
print("====================")
tokens = [token.text for token in doc]
print(tokens)
