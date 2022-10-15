class Solution:
    def mostCommonWord(self, paragraph, banned):
        # 정규식 전처리, lowercase 변환, split() 
        words = [word for word in re.sub(r'[^\w]','',paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
