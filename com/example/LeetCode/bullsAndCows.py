__author__ = 'summer'
def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    A = 0
    B = 0
    newGuess = []
    newSecret = []
    for i in xrange(len(guess)):
        if secret[i] == guess[i]:
            A += 1
        else:
            newGuess.append(guess[i])
            newSecret.append(secret[i])
    guess = "".join(newGuess)
    secret = "".join(newSecret)

    for j in xrange(len(guess)):
        if guess[j] in secret:
            B += 1
            secret = secret.replace(guess[j], "", 1)

    result = str(A) + "A" + str(B) + "B"
    return result

print getHint("1807", "7810")
