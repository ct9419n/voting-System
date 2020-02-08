from datetime import date

class Validation:
    def login(self, userID, userPassword):
        print(userID);
        for line in open("StudentVoters.txt", "r").readlines():
            userInfo = line.split(",")
            if userID == userInfo[0]:
                if (userPassword == userInfo[1]): 
                    return 1;
                else:
                    return 2;
                    break;
        else:
            return 3;

    def candidateSelectionCheck(self, votes):
        if (votes[1] == votes[2]):
            return False;
        if (votes[1] == votes[3]):
            return False;
        if (votes[1] == votes[4]):
            return False;
        
        if (votes[2] == votes[3]):
            return False;
        if (votes[2] == votes[4]):
            return False;

        if (votes[3] == votes[4]):
            return False;
        else:
            return True;

    def getDate(self, startDay, endDay):
        # get the current date
        today = date.today();

        # check curent date against election day/s
        if (today >= startDay and today <= endDay):
            return True;
        else:
            return False;
