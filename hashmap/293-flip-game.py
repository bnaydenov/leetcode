Class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        # https://youtu.be/Nz4x9Vw-N98
        # https://goodtecher.com/leetcode-293-flip-game/

        result = []

        for i in range(0, len(currentState) - 1):
            sub = currentState[i:i+2]

            if sub == "++":
                flip = currentState[:i] + "--" + currentState[i+2:]
                result.append(flip)

        return result
