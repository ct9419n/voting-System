from tkinter import *
from tkinter import ttk
from datetime import date

from validation import *
from candidates import *
from voters import *

#variable declarations
startDate = date(2020, 1, 1);
endDate = date(2020, 1, 10);

val = Validation();
candidates = candidates;
voter = voter();

# clean up the class more. perhaps create seperate functions for all the pages when they're called
class ui:    
    # function to be called to change the current top frame
    def raise_frame(self, frame):
        frame.tkraise();

    def __init__(self):
        self.root = Tk();
    
        # setting up names of the different pages
        self.EntryPage             = Frame(self.root, background = "white");
        self.loginPage             = Frame(self.root, background = "white");
        self.votePresidentPage     = Frame(self.root, background = "white");
        self.voteOfficerPage       = Frame(self.root, background = "white");
        self.voteFacultyPage       = Frame(self.root, background = "white");
        self.summaryPage           = Frame(self.root, background = "white");
        self.resultsPage           = Frame(self.root, background = "white");
        self.presidentsResultsPage = Frame(self.root, background = "white");
        self.officerResultsPage    = Frame(self.root, background = "white");
        self.facultyResultsPage    = Frame(self.root, background = "white");

        self.textWarning = StringVar();
        self.textElectionStartDate = StringVar();
        self.textElectionEndDate = StringVar();

        # setup for page defaults
        for frame in (self.EntryPage, self.loginPage, self.votePresidentPage, self.voteOfficerPage, self.voteFacultyPage, self.summaryPage, self.resultsPage
                      , self.presidentsResultsPage, self.officerResultsPage, self.facultyResultsPage):
            frame.grid(row = 0, column = 0, sticky = "news");

        self.textElectionStartDate.set(startDate);
        self.textElectionEndDate.set(endDate);
        
        # Entry Page
        Label(self.EntryPage, text = "GSU General Election", background = "white").grid(row = 0, column = 2);
        Label(self.EntryPage, text = "Election start date: ", background = "white").grid(row = 1, column = 0);
        Label(self.EntryPage, text = "Election end date: ", background = "white").grid(row = 2, column = 0);
        Label(self.EntryPage, textvariable = self.textElectionStartDate, background = "white").grid(row = 1, column = 1);
        Label(self.EntryPage, textvariable = self.textElectionEndDate, background = "white").grid(row = 2, column = 1);
        Label(self.EntryPage, text = "Select your 'role'", background = "white").grid(row = 3, column = 2);
        Button(self.EntryPage, text = "Student", command = lambda:self.EntryPageStudentButtonClick(), background = "white", borderwidth = 1).grid(row = 5, column = 2);
        Button(self.EntryPage, text = "View Results", command = lambda:self.EntryPageResultsButtonClick(), background = "white", borderwidth = 1).grid(row = 6, column = 2);
        Label(self.EntryPage, textvariable = self.textWarning, background = "white", foreground = "red").grid(row = 7, column = 2);

        # login page layout
        Label(self.loginPage, text = "GSU VOTE", background = "white").grid(row = 0, column = 1);
        Label(self.loginPage, text = "User ID:", background = "white").grid(row = 1, column = 0);
        Label(self.loginPage, text = "Password:", background = "white").grid(row = 2, column = 0);
        self.userID = Entry(self.loginPage, bd = 1);
        self.userID.grid(row = 1, column = 1);
        self.userID.focus_set();
        self.userPassword = Entry(self.loginPage, bd = 1);
        self.userPassword.grid(row = 2, column = 1);
        Button(self.loginPage, text = "login", command = lambda:self.loginButtonClick(), background = "white", borderwidth = 1).grid(row = 3, column = 2);
        Label(self.loginPage, textvariable = self.textWarning, background = "white").grid(row = 4, column = 1);
        Button(self.loginPage, text = "back", command = lambda:self.loginPageBackButtonClick(), background = "white", borderwidth = 1).grid(row = 10, column = 0);

        # vote President page layout
        Label(self.votePresidentPage, text = "Voting section", background = "white").grid(row = 0, column = 3);
        Label(self.votePresidentPage, text = "President", font = ("Helvetica", 10, "underline"), background = "white").grid(row = 1, column = 2);
        Label(self.votePresidentPage, text = "Officer", background = "white").grid(row = 1, column = 3);
        Label(self.votePresidentPage, text = "Faculty", background = "white").grid(row = 1, column = 4);
        Label(self.votePresidentPage, text = "Preferences", background = "white").grid(row = 2, column = 1);
        Label(self.votePresidentPage, text = "Candidates", background = "white").grid(row = 2, column = 3);
        Label(self.votePresidentPage, text = "1st Choice", background = "white").grid(row = 4, column = 1);
        Label(self.votePresidentPage, text = "2nd Choice", background = "white").grid(row = 5, column = 1);
        Label(self.votePresidentPage, text = "3rd Choice", background = "white").grid(row = 6, column = 1);
        Label(self.votePresidentPage, text = "4th Choice", background = "white").grid(row = 7, column = 1);
        Label(self.votePresidentPage, textvariable = self.textWarning, foreground = "red").grid(row = 8, column = 3);
        self.pres1 = ttk.Combobox(self.votePresidentPage, values = candidates.getCandidates("President"), width = 15)
        self.pres1.grid(row = 4, column = 3);
        self.pres2 = ttk.Combobox(self.votePresidentPage, values = candidates.getCandidates("President"), width = 15)
        self.pres2.grid(row = 5, column = 3);
        self.pres3 = ttk.Combobox(self.votePresidentPage, values = candidates.getCandidates("President"), width = 15)
        self.pres3.grid(row = 6, column = 3);
        self.pres4 = ttk.Combobox(self.votePresidentPage, values = candidates.getCandidates("President"), width = 15)
        self.pres4.grid(row = 7, column = 3);
        Button(self.votePresidentPage, text = "Officer vote", command = lambda:self.presidentPageClick(), background = "white").grid(row = 10, column = 5);

        # vote Officer page layout
        Label(self.voteOfficerPage, text = "Voting section", background = "white").grid(row = 0, column = 3);
        Label(self.voteOfficerPage, text = "President", background = "white").grid(row = 1, column = 2);
        Label(self.voteOfficerPage, text = "Officer", font = ("Helvetica", 10, "underline"), background = "white").grid(row = 1, column = 3);
        Label(self.voteOfficerPage, text = "Faculty", background = "white").grid(row = 1, column = 4);
        Label(self.voteOfficerPage, text = "Preferences", background = "white").grid(row = 2, column = 1);
        Label(self.voteOfficerPage, text = "Candidates", background = "white").grid(row = 2, column = 3);
        Label(self.voteOfficerPage, text = "1st Choice", background = "white").grid(row = 4, column = 1);
        Label(self.voteOfficerPage, text = "2nd Choice", background = "white").grid(row = 5, column = 1);
        Label(self.voteOfficerPage, text = "3rd Choice", background = "white").grid(row = 6, column = 1);
        Label(self.voteOfficerPage, text = "4th Choice", background = "white").grid(row = 7, column = 1);
        Label(self.voteOfficerPage, textvariable = self.textWarning, foreground = "red", background = "white").grid(row = 8, column = 3);
        self.off1 = ttk.Combobox(self.voteOfficerPage, values = candidates.getCandidates("Officer"), width = 15)
        self.off1.grid(row = 4, column = 3);
        self.off2 = ttk.Combobox(self.voteOfficerPage, values = candidates.getCandidates("Officer"), width = 15)
        self.off2.grid(row = 5, column = 3);
        self.off3 = ttk.Combobox(self.voteOfficerPage, values = candidates.getCandidates("Officer"), width = 15)
        self.off3.grid(row = 6, column = 3);
        self.off4 = ttk.Combobox(self.voteOfficerPage, values = candidates.getCandidates("Officer"), width = 15)
        self.off4.grid(row = 7, column = 3);
        Button(self.voteOfficerPage, text = "Faculty vote", command = lambda:self.officerPageClick(), background = "white").grid(row = 10, column = 5);
        Button(self.voteOfficerPage, text = "back", command = lambda:self.raise_frame(self.votePresidentPage), background = "white").grid(row = 11, column = 0);

        # vote Faculty page layout
        Label(self.voteFacultyPage, text = "Voting section", background = "white").grid(row = 0, column = 3);
        Label(self.voteFacultyPage, text = "President", background = "white").grid(row = 1, column = 2);
        Label(self.voteFacultyPage, text = "Officer", background = "white").grid(row = 1, column = 3);
        Label(self.voteFacultyPage, text = "Faculty", font = ("Helvetica", 10, "underline"), background = "white").grid(row = 1, column = 4);
        Label(self.voteFacultyPage, text = "Preferences", background = "white").grid(row = 2, column = 1);
        Label(self.voteFacultyPage, text = "Candidates", background = "white").grid(row = 2, column = 3);
        Label(self.voteFacultyPage, text = "1st Choice", background = "white").grid(row = 4, column = 1);
        Label(self.voteFacultyPage, text = "2nd Choice", background = "white").grid(row = 5, column = 1);
        Label(self.voteFacultyPage, text = "3rd Choice", background = "white").grid(row = 6, column = 1);
        Label(self.voteFacultyPage, text = "4th Choice", background = "white").grid(row = 7, column = 1);
        Label(self.voteFacultyPage, textvariable = self.textWarning, foreground = "red", background = "white").grid(row = 8, column = 3);
        self.fac1 = ttk.Combobox(self.voteFacultyPage, values = candidates.getCandidates("Faculty"), width = 15)
        self.fac1.grid(row = 4, column = 3);
        self.fac2 = ttk.Combobox(self.voteFacultyPage, values = candidates.getCandidates("Faculty"), width = 15)
        self.fac2.grid(row = 5, column = 3);
        self.fac3 = ttk.Combobox(self.voteFacultyPage, values = candidates.getCandidates("Faculty"), width = 15)
        self.fac3.grid(row = 6, column = 3);
        self.fac4 = ttk.Combobox(self.voteFacultyPage, values = candidates.getCandidates("Faculty"), width = 15)
        self.fac4.grid(row = 7, column = 3);
        Button(self.voteFacultyPage, text = "advance", command = lambda:self.facultyPageClick(), background = "white").grid(row = 10, column = 5);
        Button(self.voteFacultyPage, text = "back", command = lambda:self.raise_frame(self.voteOfficerPage), background = "white").grid(row = 11, column = 0);

        # summary page layout
        Label(self.summaryPage, text = "Confirm votes in order of preference", background = "white").grid(row = 0, column = 2);
        Label(self.summaryPage, text = "President Votes: ").grid(row = 1, column = 0);
        Label(self.summaryPage, text = "Officer Votes: ").grid(row = 2, column = 0);
        Label(self.summaryPage, text = "Faculty Votes: ") .grid(row = 3, column = 0);
        Label(self.summaryPage, text = self.pres1.get()).grid(row = 1, column = 1);#not working - cannot enter variables either
        Button(self.summaryPage, text = "confirm vote and logout", command = lambda:self.summaryPageClick(), background = "white").grid(row = 3, column = 3);

        # president results page layout
        Label(self.presidentsResultsPage, text = "Election results", padx = 25, background = "white").grid(row = 0, column = 2);
        Label(self.presidentsResultsPage, text = "President results", background = "white").grid(row = 1, column = 1);
        Button(self.presidentsResultsPage, text = "Officer results", command = lambda: self.officerResultsPageClick(), background = "white").grid(row = 1, column = 2);
        Button(self.presidentsResultsPage, text = "Faculty results", command = lambda: self.facultyResultsPageClick(), background = "white").grid(row = 1, column = 3);
        Button(self.presidentsResultsPage, text = "log out", background = "white", borderwidth = 1, command = lambda:self.raise_frame(self.EntryPage)).grid(row = 10, column = 4);

        # officer results page layout
        Label(self.officerResultsPage, text = "Election results", background = "white").grid(row = 0, column = 2);
        Button(self.officerResultsPage, text = "President results", command = lambda: self.presidentResultsPageClick(),background = "white").grid(row = 1, column = 1);
        Label(self.officerResultsPage, text = "Officer results", background = "white").grid(row = 1, column = 2);
        Button(self.officerResultsPage, text = "Faculty results", command = lambda: self.facultyResultsPageClick(),background = "white").grid(row = 1, column = 3);
        Button(self.officerResultsPage, text = "log out", background = "white", borderwidth = 1, command = lambda:self.raise_frame(self.EntryPage)).grid(row = 10, column = 4);

        # faculty results page layout
        Label(self.facultyResultsPage, text = "Election results", background = "white").grid(row = 0, column = 2);
        Button(self.facultyResultsPage, text = "President results", command = lambda: self.presidentResultsPageClick(),background = "white").grid(row = 1, column = 1);
        Button(self.facultyResultsPage, text = "Officer results", command = lambda: self.officerResultsPageClick(),background = "white").grid(row = 1, column = 2);
        Label(self.facultyResultsPage, text = "Faculty results", background = "white").grid(row = 1, column = 3);
        Button(self.facultyResultsPage, text = "log out", background = "white", borderwidth = 1, command = lambda:self.raise_frame(self.EntryPage)).grid(row = 10, column = 4);

        self.raise_frame(self.EntryPage);
        self.root.mainloop;
        

    def EntryPageStudentButtonClick(self):
        if (date.today() < startDate):
            self.textWarning.set("The election has not started yet!");
        elif (date.today() > endDate):
            self.textWarning.set("The election is over!");
        else:
            self.raise_frame(self.loginPage);

    def EntryPageResultsButtonClick(self):
        if (date.today() > endDate):
            voter.tallyVotes();
            self.raise_frame(self.presidentsResultsPage);
            self.presidentResultsPageClick();
            voter.printZeroVotes();
        else:
            self.textWarning.set("The election is not over yet!");

    def loginButtonClick(self):
        login = val.login(self.userID.get(), self.userPassword.get());

        # check if username exists
        if (login == 1):
            print(voter.checkVoted(self.userID.get()));
            if (voter.checkVoted(self.userID.get())):
                self.textWarning.set("");
                self.raise_frame(self.votePresidentPage);
            else:
                self.textWarning.set("You cannot vote again");
        elif (login == 2):
            self.textWarning.set("Password incorrect");
        else:
            self.textWarning.set("Username does not exist");

    def menuBarClick(self):
        print("hello");

    def loginPageBackButtonClick(self):
        self.raise_frame(self.EntryPage);

    def presidentPageClick(self):
        self.presidentVotes = {1 : self.pres1.get(),
                               2 : self.pres2.get(),
                               3 : self.pres3.get(),
                               4 : self.pres4.get()
                              };
                        
        if (val.candidateSelectionCheck(self.presidentVotes)):
            self.textWarning.set("");
            self.raise_frame(self.voteOfficerPage);
        else:
            self.textWarning.set("Please remove duplicates");

    def officerPageClick(self):
        self.officerVotes = {1 : self.off1.get(),
                             2 : self.off2.get(),
                             3 : self.off3.get(),
                             4 : self.off4.get()
                            };
        
        if (val.candidateSelectionCheck(self.officerVotes)):
            self.textWarning.set("");
            self.raise_frame(self.voteFacultyPage);
        else:
            self.textWarning.set("Please remove duplicates");

    def facultyPageClick(self):
        self.facultyVotes = {1 : self.fac1.get(),
                             2 : self.fac2.get(),
                             3 : self.fac3.get(),
                             4 : self.fac4.get()
                            };
        
        if (val.candidateSelectionCheck(self.facultyVotes)):
            self.textWarning.set("");
            self.raise_frame(self.summaryPage);
        else:
            self.textWarning.set("Please remove duplicates");

    def summaryPageClick(self):
        # sends the dictionary values of the votes to the voter class
        voter.printVote(self.presidentVotes, self.officerVotes, self.facultyVotes);
        voter.tallyVotes();
        self.raise_frame(self.EntryPage);
        voter.recordVote(self.userID.get());
        print(voter.getPresidentVotes());
        print(voter.getOfficerVotes());
        print(voter.getFacultyVotes());

    def presidentResultsPageClick(self):
        self.raise_frame(self.presidentsResultsPage);

        Label(self.presidentsResultsPage, text = "1st Preference", padx = 25, background = "white").grid(row = 3, column = 2);
        Label(self.presidentsResultsPage, text = "2nd Preference", padx = 25, background = "white").grid(row = 3, column = 3);
        Label(self.presidentsResultsPage, text = "3rd Preference", padx = 25, background = "white").grid(row = 3, column = 4);
        Label(self.presidentsResultsPage, text = "4th Preference", padx = 25, background = "white").grid(row = 3, column = 5);

        for i in range(len(candidates.getCandidates("President"))):
            # putting in the names
            Label(self.presidentsResultsPage, text = candidates.getCandidates("President")[i], background = "white").grid(row = 4 + i, column = 0);
            for j in range(1,5):
                Label(self.presidentsResultsPage, text = voter.getPresidentVotes()[i][j], background = "white", padx = 25).grid(row = 4 + i, column = 1 + j, sticky = "E");

        self.test = voter.getPresidentVotes();
        voter.calculateWinner(self.test, 1);

    def officerResultsPageClick(self):
        self.raise_frame(self.officerResultsPage);

        Label(self.officerResultsPage, text = "1st Preference", padx = 25, background = "white").grid(row = 3, column = 2);
        Label(self.officerResultsPage, text = "2nd Preference", padx = 25, background = "white").grid(row = 3, column = 3);
        Label(self.officerResultsPage, text = "3rd Preference", padx = 25, background = "white").grid(row = 3, column = 4);
        Label(self.officerResultsPage, text = "4th Preference", padx = 25, background = "white").grid(row = 3, column = 5);

        for i in range(len(candidates.getCandidates("Officer"))):
            # putting in the names
            Label(self.officerResultsPage, text = candidates.getCandidates("Officer")[i], background = "white").grid(row = 4 + i, column = 0);
            for j in range(1,5):
                Label(self.officerResultsPage, text = voter.getOfficerVotes()[i][j], background = "white", padx = 25).grid(row = 4 + i, column = 1 + j, sticky = "E");

        self.test = voter.getOfficerVotes();
        voter.calculateWinner(self.test, 1);

    def facultyResultsPageClick(self):
        self.raise_frame(self.facultyResultsPage);

        Label(self.facultyResultsPage, text = "1st Preference", padx = 25, background = "white").grid(row = 3, column = 2);
        Label(self.facultyResultsPage, text = "2nd Preference", padx = 25, background = "white").grid(row = 3, column = 3);
        Label(self.facultyResultsPage, text = "3rd Preference", padx = 25, background = "white").grid(row = 3, column = 4);
        Label(self.facultyResultsPage, text = "4th Preference", padx = 25, background = "white").grid(row = 3, column = 5);

        for i in range(len(candidates.getCandidates("Faculty"))):
            # putting in the names
            Label(self.facultyResultsPage, text = candidates.getCandidates("Faculty")[i], background = "white").grid(row = 4 + i, column = 0);
            for j in range(1,5):
                Label(self.facultyResultsPage, text = voter.getFacultyVotes()[i][j], background = "white", padx = 25).grid(row = 4 + i, column = 1 + j, sticky = "E");

        self.test = voter.getFacultyVotes();
        voter.calculateWinner(self.test, 1);
        

    def resultsPageLayout(self, position):
        self.resultsPage.destroy();
        self.resultsPage = Frame(self.root, background = "white");
        self.resultsPage.grid(row = 0, column = 0, sticky = "news");
        Label(self.resultsPage, text = "Election results", background = "white").grid(row = 0, column = 2);
        Button(self.resultsPage, text = "President", command = lambda:self.resultsPageLayout("President"), background = "white").grid(row = 2, column = 1);
        Button(self.resultsPage, text = "Officer", command = lambda:self.resultsPageLayout("Officer"), background = "white").grid(row = 2, column = 2);
        Button(self.resultsPage, text = "Faculty", command = lambda:self.resultsPageLayout("Faculty"), background = "white").grid(row = 2, column = 3);
        Button(self.resultsPage, text = "log out", background = "white", borderwidth = 1, command = lambda:self.raise_frame(self.EntryPage)).grid(row = 10, column = 4);
        Label(self.resultsPage, text = "1st Preference", padx = 25, background = "white").grid(row = 3, column = 2);
        Label(self.resultsPage, text = "2nd Preference", padx = 25, background = "white").grid(row = 3, column = 3);
        Label(self.resultsPage, text = "3rd Preference", padx = 25, background = "white").grid(row = 3, column = 4);
        Label(self.resultsPage, text = "4th Preference", padx = 25, background = "white").grid(row = 3, column = 5);
        self.raise_frame(self.resultsPage);
        print(voter.getPresidentVotes());
        print(voter.getPresidentVotes()[3][1]);
        
        for i in range(len(candidates.getCandidates(position))):
            # putting in the names
            Label(self.resultsPage, text = candidates.getCandidates(position)[i], background = "white").grid(row = 4 + i, column = 0);
            for j in range(1,5):
                Label(self.resultsPage, text = voter.getPresidentVotes()[i][j], background = "white", padx = 25).grid(row = 4 + i, column = 1 + j, sticky = "E");

        self.test = voter.getPresidentVotes();
        voter.calculateWinner(self.test, 1);

         # hackathon code
        if (val.getDate(startDate, endDate)):
            voter.printZeroVotes();
        
