
def getPersonality(one, two, three, four, five, six, seven, eight, nine, ten):
    # personality test variables
    extravert = 0
    agreeable = 0
    conscient = 0
    emotion = 0
    openess = 0
    thinker = 0
    performer = 0
    caregiver = 0

    # Question 1
    #print("I view myself as enthusiastic, extraverted")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if one == 1:
        extravert = extravert + 2
        openess = openess + 1
    elif one == 2:
        extravert = extravert + 1
        openess = openess + 1
    elif one == 3:
        emotion = emotion + 1
    elif one == 4:
        conscient = conscient + 1
    elif one == 5:
        conscient = conscient + 1

    # Question 2
    #print("I am quarrelsome, critical")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if two == 1:
        conscient = conscient + 1
        performer = performer + 2
    elif two == 2:
        conscient = conscient + 1
        performer = performer + 1
    elif two == 3:
        agreeable = agreeable + 1
    elif two == 4:
        agreeable = agreeable + 1
        openess = openess + 1
    elif two == 5:
        emotion = emotion + 1
        agreeable = agreeable + 2
        openess = openess + 1

    # Question 3
    #print("I am dependable, self disciplined")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if three == 1:
        conscient = conscient + 2
        thinker = thinker + 1
        performer = performer + 1
    elif three == 2:
        conscient = conscient + 1
        emotion = emotion + 1
        thinker = thinker + 1
        performer = performer + 1
    elif three == 3:
        emotion = emotion + 1
    elif three == 4:
        extravert = extravert + 1
    elif three == 5:
        extravert = extravert + 1

    # Question 4
    #print("I am anxious or easily upset")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if four == 1:
        emotion = emotion - 1
    elif four == 2:
        emotion = emotion - 1
    elif four == 3:
        agreeable = agreeable + 1
    elif four == 4:
        openess = openess + 1
        caregiver = caregiver + 1
    elif four == 5:
        openess = openess + 1
        caregiver = caregiver + 1

    # Question 5
    #print("I am open to new experiences, complex")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if five == 1:
        openess = openess + 2
        extravert = extravert + 1
        emotion = emotion + 1
        thinker = thinker + 2
        performer = performer + 1
    elif five == 2:
        openess = openess + 1
        extravert = extravert + 1
        agreeable = agreeable + 1
        performer = performer + 1
    elif five == 3:
        agreeable = agreeable + 1
    elif five == 4:
        conscient = conscient + 1
    elif five == 5:
        conscient = conscient + 1

    # Question 6
    #print("I am reserved, quiet")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if six == 1:
        openess = openess - 1
    elif six == 2:
        openess = openess - 1
    elif six == 4:
        extravert = extravert + 1
        thinker = thinker + 1
    elif six == 5:
        extravert = extravert + 2
        thinker = thinker + 1

    # Question 7
    #print("I am sympathetic, warm")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if seven == 1:
        emotion = emotion + 2
        caregiver = caregiver + 2
    elif seven == 2:
        emotion = emotion + 1
        caregiver = caregiver + 1

    # Question 8
    #print("I am disorganized, careless")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if eight == 1:
        extravert = extravert + 1
        openess = openess + 1
    elif eight == 2:
        extravert = extravert + 1
        openess = openess + 1
    elif eight == 3:
        agreeable = agreeable + 1
    elif eight == 4:
        emotion = emotion + 1
        conscient = conscient + 1
        performer = performer + 1
    elif eight == 5:
        emotion = emotion + 1
        conscient = conscient + 2
        performer = performer + 1

    # Question 9
    #print("I am calm, emotionally stable")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if nine == 1:
        emotion = emotion + 2
        extravert = extravert + 1
        caregiver = caregiver + 1
    elif nine == 2:
        emotion = emotion + 1
        extravert = extravert + 1
        caregiver = caregiver + 1
    elif nine == 4:
        openess = openess - 1
    elif nine == 5:
        openess = openess - 1

    # Question 10
    #print("I am conventional, uncreative")
    #print("1: strongly agree, 2: agree, 3: neutral, 4: disagree, 5: strongly disagree")

    if ten == 1:
        agreeable = agreeable + 1
        conscient = conscient + 2
    elif ten == 2:
        agreeable = agreeable + 1
        conscient = conscient + 1
    elif ten == 3:
        performer = performer + 1
    elif ten == 4:
        extravert = extravert + 1
        openess = openess + 1
        performer = performer + 1
    elif ten == 5:
        extravert = extravert + 1
        openess = openess + 1
        thinker = thinker + 1
        performer = performer + 1

    #print("Scores:\n")
    #print("Extraverted: ", extravert)
    #print("Agreeableness: ", agreeable)
    #print("Conscientiousness: ", conscient)
    #print("Emotionally Stable: ", emotion)
    #print("Openess: ", openess)
    #print("Thinker: ", thinker)
    #print("Performer: ", performer)
    #print("Care Giver: ", caregiver)

    highestScore = 0
    personality = ""

    highestScore2 = 0
    personality2 = ""

    # get first personality type

    if extravert > highestScore:
        highestScore = extravert
        personality = "Extraverted"

    if agreeable > highestScore:
        highestScore = agreeable
        personality = "Agreeable"

    if conscient > highestScore:
        highestScore = conscient
        personality = "Conscientious"

    if emotion > highestScore:
        highestScore = emotion
        personality = "Emotionally Stable"

    if openess > highestScore:
        highestScore = openess
        personality = "Open to New Experiences"

    if thinker > highestScore:
        highestScore = thinker
        personality = "Thinker"

    if performer > highestScore:
        highestScore = performer
        personality = "Performer"

    if caregiver > highestScore:
        highestScore = caregiver
        personality = "Care Giver"

    # get second personality type
    if extravert == highestScore:
        if personality != "Extraverted":
            highestScore2 = extravert
            personality2 = "Extraverted"

    if extravert > highestScore2:
        if personality != "Extraverted":
            highestScore2 = extravert
            personality2 = "Extraverted"

    if agreeable == highestScore:
        if personality != "Agreeable":
            highestScore2 = agreeable
            personality2 = "Agreeable"

    if agreeable > highestScore2:
        if personality != "Agreeable":
            highestScore2 = agreeable
            personality2 = "Agreeable"

    if conscient == highestScore:
        if personality != "Conscientious":
            highestScore2 = conscient
            personality2 = "Conscientious"

    if conscient > highestScore2:
        if personality != "Conscientious":
            highestScore2 = conscient
            personality2 = "Conscientious"

    if emotion == highestScore:
        if personality != "Emotionally Stable":
            highestScore2 = emotion
            personality2 = "Emotionally Stable"

    if emotion > highestScore2:
        if personality != "Emotionally Stable":
            highestScore2 = emotion
            personality2 = "Emotionally Stable"

    if openess == highestScore:
        if personality != "Open to New Experiences":
            highestScore2 = openess
            personality2 = "Open to New Experiences"

    if openess > highestScore2:
        if personality != "Open to New Experiences":
            highestScore2 = openess
            personality2 = "Open to New Experiences"

    if thinker == highestScore:
        if personality != "Thinker":
            highestScore2 = thinker
            personality2 = "Thinker"

    if thinker > highestScore2:
        if personality != "Thinker":
            highestScore2 = thinker
            personality2 = "Thinker"

    if performer == highestScore:
        if personality != "Performer":
            highestScore2 = performer
            personality2 = "Performer"

    if performer > highestScore2:
        if personality != "Performer":
            highestScore2 = performer
            personality2 = "Performer"

    if caregiver == highestScore:
        if personality != "Care Giver":
            highestScore2 = caregiver
            personality2 = "Care Giver"

    if caregiver > highestScore2:
        if personality != "Care Giver":
            highestScore2 = caregiver
            personality2 = "Care Giver"

    print("Personality: ", personality)
    print("Personality 2: ", personality2)

    returnArray = ["", ""]

    returnArray[0] = personality
    returnArray[1] = personality2

    return returnArray





