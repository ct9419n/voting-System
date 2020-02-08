from candidates import *

candidates = candidates();

class voter:
    def __init__(self):
        self.presidentVotes = [];
        self.officerVotes = [];
        self.facultyVotes = [];
        self.presidentWinnder = "";

    def getPresidentVotes(self):
        return self.presidentVotes;

    def getOfficerVotes(self):
        return self.officerVotes;

    def getFacultyVotes(self):
        return self.facultyVotes;

    def countVoters(self):
        file = open("Voted.txt", "r");
        a = 0;
        
        for i in file:
            a += 1;

        return a;

    def printZeroVotes(self):        
        for h in range(0,3):
            if (h == 0):
                self.temp = self.presidentVotes;
                self.name = "President";
            if (h == 1):
                self.temp = self.officerVotes;
                self.name = "Officer";
            if (h == 2):
                self.temp = self.facultyVotes;
                self.name = "Faculty";
                
            for i in range(len(self.temp)):
                self.zeroCounter = 0;

                for j in range(1,5):
                    if (self.temp[i][j] == 0):
                        self.zeroCounter += 1;                    

                if (self.zeroCounter == 4):
                    for k in candidates.getCandidates(self.name):
                        if (k[0:len(k) - 1] == self.temp[i][0]):
                            print(self.name, ", ", self.temp[i][0]);
                        

    def calculateWinner(self, peeps, j):
        if (j == 6):
            pass;
        else:
            self.temp = peeps[0][j];
            print("self.temp: ", self.temp);
            self.tieBreaker = [];

            for i in range(1, len(peeps)):
                if (self.temp > peeps[i][j]):
                    pass;
                elif ( self.temp < peeps[i][j]):
                        self.temp = peeps[i][j];

            for i in range(0, len(peeps)):
                if (self.temp == peeps[i][j]):
                        self.tieBreaker.append(peeps[i]);
            print(self.tieBreaker);

            if (len(self.tieBreaker) > 1):
                if (j < 5):
                    self.calculateWinner(self.tieBreaker, j + 1);
                
                if (self.tieBreaker[0][0] == self.tieBreaker[0][1]):
                    print("It is  a prefect tie!");
            else:
                print("Winner: ", self.tieBreaker[0]);

    def checkVoted(self, userID):
        file = open("Voted.txt", "r");
        for i in file:
            print("i: ", i);
            # check if they have voted already
            if (userID == i[0:len( i) - 1]):
                print("found");
                file.close();
                return False;
                break;

        return True;

        file.close();
            
    def recordVote(self, userID):
        file = open("Voted.txt", "a");
        file.write(userID + "\n");
        file.close();
    
    def printVote(self, presidentVotes, officerVotes, facultyVotes):
        file = open ("votes.txt", "a");
        file.write("President votes:\n");
        for i in presidentVotes:
            file.write(str(i) + ") " + presidentVotes[i]);
            
        file.write("Officer Votes:\n");
        for i in officerVotes:
            file.write(str(i) + ") " + officerVotes[i]);

        file.write("Faculty Votes:\n");
        for i in facultyVotes:
            file.write(str(i) + ") " + facultyVotes[i]);
        file.write("\n");

        file.close();
        self.voted = True;

    def tallyVotes(self):
        counter = 0;

        while counter <= 2:
            if (counter == 0):
                position = "President";
                storage = self.presidentVotes;

            elif (counter == 1):
                position = "Officer";
                storage = self.officerVotes;

            elif (counter == 2):
                position = "Faculty";
                storage = self.facultyVotes;

            file = open("votes.txt", "r");
            candidates.getCandidates(position);

            storage = [["" for col in range(5)] for col in range(len(candidates.getCandidates(position)))];
            # reading the names of the candidates into the list
            for i in range(len(candidates.getCandidates(position))):
                storage[i][0] = candidates.getCandidates(position)[i][0:len(candidates.getCandidates(position)[i]) - 1];
            

            # initiating values within the president votes to 0
            for i in range(0,len(candidates.getCandidates(position))):
                for j in range(1,5):
                    storage[i][j] = 0;


            # if the name in the voting file = name in the candidate file
            for i in file:
                line = i.split(") ");
                try:
                    line[1] = line[1][0:len(line[1]) - 1];
                    for j in range(len(candidates.getCandidates(position))):
                        test = candidates.getCandidates(position)[j];
                        # the candidate in the voting file is a president candidate
                        if (line[1] == test[0:len(candidates.getCandidates(position)[j]) - 1]):
                            temp = 0;
                            # go to the candidates name in the presidentVotes list
                            for k in storage:
                                if (line[1] == k[0]):
                                    # change that persons vote according to the voting files number
                                    if (line[0] == "1"):
                                        storage[temp][int(line[0])] += 1;
                                    if (line[0] == "2"):
                                        storage[temp][int(line[0])] += 1;
                                    if (line[0] == "3"):
                                        storage[temp][int(line[0])] += 1;
                                    if (line[0] == "4"):
                                        storage[temp][int(line[0])] += 1;
                                    break;
                                temp += 1;
                                    
                except:
                    continue;

            if (counter == 0):
                self.presidentVotes = storage;

            elif (counter == 1):
                self.officerVotes = storage;

            else:                
                self.facultyVotes = storage;
                    
            file.close();
            counter += 1;
