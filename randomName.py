import random
mentionList = ["@TiffanyATrump","@MileyCyrus","@HeffronDrive","@Eminem","@kendricklamar","@bellahadid","@KimKardashian","@KylieJenner","@JKCorden","@NICKIMINAJ","@jstinbieber","@ladygaga","@shakira","@katyperry","@BarackObama","@SnoopDogg","@JColeNC" ]
def getRandomName():
    data = random.sample(mentionList,3)
    return data
