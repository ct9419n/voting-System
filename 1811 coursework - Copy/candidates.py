class candidates:
    
    def getCandidates(self, position):
        file = open("GSUCandidates.txt", "r");
        result = [];
        
        # reads lines from text file into list
        lines = file.readlines();

        # searches the list for names that match the sent position
        for i in lines:
            if (i.split(",")[0] == position):
                result.append(i.split(",")[1] + " " + i.split(",")[2]);

        return result;

